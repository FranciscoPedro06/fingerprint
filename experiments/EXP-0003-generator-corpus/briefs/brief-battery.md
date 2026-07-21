# EXP-0003 — Brief Battery

**Status:** Sealed 2026-07-18. Do not add style vocabulary to any brief.

Twelve neutral briefs, ordered along the **expressive → functional** spectrum. Each brief
states only *what the interface is for, who it serves, what content it must contain, and the
one primary action.* No colors, fonts, moods, adjectives of taste, or design references — a
brief that says "modern," "clean," "minimal," "bold," or names any aesthetic is out of spec.

Each brief is run through every in-scope generator (AI side) and matched to real interfaces in
each of the three human classes (human side). The genre label is used for matching; it is
**not** part of the prompt given to a generator.

---

### Expressive end

**B01 — Coffee roaster.** A single homepage for an independent coffee roaster that sells bags
of beans and runs a small subscription. Must contain: what they sell, how the subscription
works, where to buy. Primary action: start a subscription.

**B02 — Photographer portfolio.** A portfolio homepage for a freelance photographer. Must
contain: a body of work, the kind of work they take on, how to reach them. Primary action:
get in touch.

**B03 — Hardware product launch.** A launch page for a new physical consumer gadget. Must
contain: what the product is and does, its key specifications, its price, availability.
Primary action: pre-order.

**B04 — Music festival.** A homepage for a multi-day music festival. Must contain: dates and
location, the lineup, ticket tiers. Primary action: buy tickets.

### Mixed

**B05 — B2B analytics SaaS.** A marketing homepage for a business analytics product. Must
contain: what problem it solves, its main capabilities, social proof, a way to try it.
Primary action: start a trial.

**B06 — Project-management pricing.** A pricing page for a project-management app. Must
contain: the plan tiers, what each includes, the differences between them. Primary action:
choose a plan.

**B07 — Dental clinic.** A homepage for a local dental clinic. Must contain: the services
offered, the practitioners, location and hours, how to book. Primary action: book an
appointment.

**B08 — Budgeting app.** A landing page for a personal budgeting / money app. Must contain:
what it helps you do, how it works, trust and security information. Primary action: download
the app.

### Functional end

**B09 — Fleet dashboard.** The main dashboard screen of a logistics fleet-monitoring tool.
Must contain: fleet status at a glance, a list of vehicles with their state, alerts needing
attention. Primary action: open a vehicle's detail.

**B10 — E-commerce checkout.** The checkout step of an online store. Must contain: an order
summary, contact and shipping fields, payment entry, the total. Primary action: place the
order.

**B11 — Account settings.** The account/settings page of a web application. Must contain:
profile fields, security options, notification preferences, billing. Primary action: save
changes.

**B12 — API documentation home.** The landing page of a developer API's documentation. Must
contain: what the API does, a quickstart, navigation into the reference, an example request.
Primary action: get an API key.

---

## Sealing note

These twelve are the fixed battery for the first corpus. Changing a brief after sealing
invalidates comparability across samples already collected under it; a changed brief becomes a
new id (e.g. `B05a`) rather than an edit. New genres are added as `B13+`, never by rewriting an
existing brief.
