# Enna. Strategy Decisions (Round 1)

> **Superseded in part.** The architecture, BOM and tooling figures here
> predate the modular rebuild. See `08-modular-architecture.md` for current
> numbers.

Decisions taken with the founder on 2026-09-10.

## Mechanism: "sourced engine, invented gut"

The founder rejected both extremes: an 18-month in-house pump programme is too
slow, and a plain off-the-shelf head is too easy to copy. The middle path:

**Buy the engine, invent the gut.** Source a proven pre-compression trigger head, the foundational precompression-valve patents (US5467900, US5730335) and the
non-aerosol oil-spray patents (US5455055, US5650185) are 1990s filings and have
lapsed, so generic pre-compression heads exist outside AFA's live Flairosol
claims (US8905271B2, US9714133, EP2566629B1, live to ~2030, 33).

Invent the **wetted path**, which is where the Indian problem actually lives:

1. Elevated / anti-sediment intake with a 9 mm standoff.
2. Serviceable 600 µm bayonet intake basket.
3. 150 µm fine screen immediately before the orifice.
4. Wide-mouth Ø46 mm four-start closure with a silicone face seal.

These are small, cheap to tool, fast to iterate, and independently patentable.
**Timeline 6, 9 months rather than 18.**

## Defensibility: four moats, not one

Copying is inevitable in kitchenware. Stack them:

1. **Patent** on the filtration + raised-intake system (provisional first).
2. **Design registration** on the form under the Designs Act 2000, ₹1,000 government fee for a startup/small entity with Form-24, plus
   ₹5,000, 8,000 attorney. 10 years, extendable by 5.
3. **Trademark** "Enna" in class 21, plus classes 8 and 11 as relevant.
4. **Supply-chain exclusivity**, negotiate India category exclusivity with the
   pump-head supplier. This is the most underrated lever available to a
   first-time hardware brand and can be secured in weeks, not years.

A fifth, softer moat: openly sold spares and a real warranty. A copycat can
clone a shape; it cannot clone a service commitment.

## Positioning: ₹1,299, 1,799, indicative retail ₹1,499

Above the crowded ₹200, 600 import floor, well below Evo's ≈₹2,600. Targets urban
health-conscious households who already own an air fryer. Leaves margin to fund
tooling, compliance and IP.

## Solid fats: design for liquid oils, and say so

Optimise for mustard, groundnut, gingelly, sunflower and rice bran. State the
coconut-oil (<24 °C) and ghee limits openly on the packaging and the site.
No sprayer atomises a solid; every competitor pretends otherwise. The honesty
is itself a trust signal and it is now a section on the website.

## Capacity: 180 ml, deliberately

Oil in an open bottle should be finished in three to four weeks. The 470, 500 ml
units flooding the market are selling a rancidity problem as a value feature.
This is a claim we should be willing to defend publicly.

## Deliverable status

- `site/index.html`, showcase website with a scroll-driven exploded 3D view of
  all nine parts, built with procedural Three.js geometry (no external model
  assets, so it works under the artifact CSP).
- Published artifact: https://claude.ai/code/artifact/09756877-f5a6-4c56-b48c-87dc95b8ce1e

## Still open

- Bill of materials and costed manufacturing plan.
- Freedom-to-operate read of the live Flairosol claim set and WO2016077114A1.
- Pump-head supplier shortlist and viscosity qualification protocol.
- Whether the level indicator (window strip) survives cost-down.

---

# Round 2 decisions (2026-09-10)

## The set: 250 ml sprayer + 750 ml decanter

The 500 ml pivot was right about the problem (Indians buy 1 L pouches and need
somewhere to put them) and wrong about the solution: a 500 ml sprayer weighs
855 g full, and squeezing a trigger on that is tiring by the third pan.

**Split it, then sell it as one SKU.** *Enna Spray* holds 250 ml (530 g full, comfortable). *Enna Store* holds 750 ml in opaque steel. 250 + 750 = exactly one
litre: one pouch in, nothing folded shut on the shelf going rancid.

One box, one EAN, one marketplace listing. This is what makes a two-piece system
survive quick-commerce economics, where the listing fee is ₹25,000 **per SKU per
state**. Two separate SKUs would double that in every state.

It also restores the shelf-life argument honestly: 250 ml is about four weeks of
cooking, which is the right open-bottle window. The decanter keeps the rest dark.

## Both openings stay

Wide top for filling, removable base for cleaning. Both get captive LSR face
gaskets; both gaskets go in the spares kit. The base seal is **static and
unpressurised**, the pump pressurises only the chamber in the head, and 118 mm
of oil exerts about 0.011 bar on the base. This is the same sealing duty as a
moka pot or a vacuum flask, not a hard problem, but it must be validated:
24 h inverted at 45 °C, and 500 open/close cycles.

## Counter: strokes remaining, coarse segmented bar

Counts down from 1,250 (250 ml ÷ 0.20 ml) like an inhaler dose counter. Reads as
a fuel gauge at a glance, cheapest mechanism, resets with a twist ring on refill.
Calories stay on the packaging and the website rather than on the part, a
calorie read-out on someone's oil bottle risks reading as judgement rather than
information.

## Beachhead: three audiences, one insight

Diabetic and PCOS households, air-fryer owners, and calorie/macro trackers.
They share exactly one thing: **every one of them already measures something.**
Enna does not ask them to start a new habit, it plugs into the one they have.
That is the positioning line, *for people who already measure.*

Launch **geography** is a separate question from launch **audience**. These three
segments are pan-India; the name, the joke and the oils all argue for Tamil Nadu
as the first state on the shelf, which also means one state's quick-commerce
listing fee, not eight.

## Marketing: the enna / ennai pun

The brand name is the punchline of a comedy scene every Tamil household can
recite, a shopkeeper and a customer stuck in a loop because *enna* ("what") and
*ennai* ("oil") sound alike. It resolves into the shopkeeper listing three oils:
gingelly, groundnut and coconut. Two of them Enna sprays perfectly; the third is
the one we are honest about, because coconut oil sets below 24 °C.

**Rights caution:** the pun itself is language and free to use, but the film
clip, the dialogue as written, and the actors' names and likenesses are not.
Do not use the clip or name the actors in commercial marketing without a
licence. The site therefore stages the exchange with unnamed generic speakers.
