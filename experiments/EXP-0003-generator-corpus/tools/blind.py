#!/usr/bin/env python3
"""Build the observer-facing blind set from the sealed corpus.

Run by the COLLECTOR, never by the judge (EXP-0003 protocol, "Independence").

Reads  _sealed/<source-class>/<brief-id>/{01-hero-*.png, 02-fullpage-*.png}
Writes samples/S-XXXX-{hero,full}.png   (observer-facing, provenance-free)
       _sealed/manifest.csv             (the provenance key, gitignored)

Two leak vectors this closes beyond renaming:

1. **PNG metadata.** Ancillary chunks (tEXt, tIME, pHYs, iCCP, eXIf) can carry
   the rendering engine, a timestamp, or a colour profile that differs per arm.
   Two arms captured on different days by different engines would be separable
   from bytes alone, with no design judgement involved. Only the critical
   chunks needed to render are copied through.
2. **Ordering.** Sample-ids are assigned from a shuffled list, so id order
   carries no arm or brief signal.

What it cannot close: file size. A page's byte size is a property of the page.
Log it as a known residual channel rather than pretending otherwise.
"""

import csv
import hashlib
import random
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEALED = ROOT / "_sealed"
SAMPLES = ROOT / "samples"
MANIFEST = SEALED / "manifest.csv"

# Chunks required to decode the image. Everything else is dropped.
KEEP = {b"IHDR", b"PLTE", b"IDAT", b"IEND", b"tRNS", b"gAMA", b"cHRM", b"sRGB"}

SHOTS = {"hero": "01-hero-1280x800.png", "full": "02-fullpage-1280x4200.png"}


def strip_png(src: Path, dst: Path) -> None:
    """Copy a PNG keeping only critical chunks, dropping all metadata."""
    raw = src.read_bytes()
    if raw[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"not a PNG: {src}")
    out, pos = bytearray(raw[:8]), 8
    while pos < len(raw):
        (length,) = struct.unpack(">I", raw[pos : pos + 4])
        ctype = raw[pos + 4 : pos + 8]
        end = pos + 12 + length
        if ctype in KEEP:
            out += raw[pos:end]
        pos = end
        if ctype == b"IEND":
            break
    dst.write_bytes(bytes(out))


def main(seed: int | None = None) -> int:
    if not SEALED.is_dir():
        print(f"no sealed corpus at {SEALED}", file=sys.stderr)
        return 1

    units = []  # (source_class, brief_id, dir)
    for arm in sorted(p for p in SEALED.iterdir() if p.is_dir()):
        for brief in sorted(p for p in arm.iterdir() if p.is_dir()):
            missing = [n for n in SHOTS.values() if not (brief / n).exists()]
            if missing:
                print(f"SKIP {arm.name}/{brief.name}: missing {missing}", file=sys.stderr)
                continue
            units.append((arm.name, brief.name, brief))

    if not units:
        print("no complete samples found", file=sys.stderr)
        return 1

    seed = random.randrange(2**32) if seed is None else seed
    order = list(range(len(units)))
    random.Random(seed).shuffle(order)

    SAMPLES.mkdir(exist_ok=True)
    for p in SAMPLES.glob("S-*.png"):
        p.unlink()

    rows = []
    for sid_num, unit_idx in enumerate(order, start=1):
        arm, brief_id, d = units[unit_idx]
        sid = f"S-{sid_num:04d}"
        digests = {}
        for label, fname in SHOTS.items():
            out = SAMPLES / f"{sid}-{label}.png"
            strip_png(d / fname, out)
            digests[label] = hashlib.sha256(out.read_bytes()).hexdigest()[:12]
        rows.append(
            {
                "sample-id": sid,
                "brief-id": brief_id,
                "genre": "",  # filled from the brief battery at scoring
                "source-class": arm,
                "generator-or-site": arm,
                "capture-params": "1280x800 hero + 1280x4200 fullpage, "
                "chromium-headless, scale 1",
                "match-quality": "n/a (AI arm)",
                "sha256-hero": digests["hero"],
                "sha256-full": digests["full"],
                "notes": f"shuffle-seed={seed}",
            }
        )

    rows.sort(key=lambda r: r["sample-id"])
    with MANIFEST.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    print(f"{len(rows)} samples -> {SAMPLES}")
    print(f"manifest (SEALED) -> {MANIFEST}")
    print("classes:", ", ".join(sorted({r['source-class'] for r in rows})))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(int(sys.argv[1]) if len(sys.argv) > 1 else None))
