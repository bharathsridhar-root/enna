# Enna, Round 5: the modular rebuild

New governing principles, stated by the founder: **modular, simple, repairable.**
Cost is computed bottom up from the design rather than constraining it.

This document supersedes the architecture and BOM sections of
`03-strategy.md` and `04-manufacturing.md`.

## Eight decisions

| # | Decision | Chosen |
|---|---|---|
| 1 | Part strategy | **Six modules**, each a stocked spare with a part number |
| 2 | Spray pattern | **One fixed mist nozzle.** No mode dial |
| 3 | Dose counter | **Optional clip-on accessory**, sold separately |
| 4 | Removable base | **Kept** |
| 5 | Head module | **Sourced pump core in our own housing** |
| 6 | Repairability | **Published drawings, 10 year parts, zero adhesives** |
| 7 | Decanter | **Tooled to match**, not sourced |
| 8 | Interface | **Published specification** |

## What the fixed nozzle changed, and why it was right

Removing the multi position collar killed two backlog features, PURGE and
DRIZZLE. The architecture replaced both without a mechanism:

- **Clearing a clog** was going to be a PURGE detent. It is now: pull the head
  module, flush it, click it back. Five seconds, no tools, no bypass channel.
- **Pouring a spoonful** was going to be a DRIZZLE detent. It is now what the
  decanter is for. The second vessel answers the 2 in 1 objection that a single
  bottle needed a dial to answer.

A rotating collar puts a moving seal in the oil path, which is both a wear part
and a leak path, and it needs internal channels that make the head harder to
mould and impossible to service. It failed all three principles at once.

## The six modules

| Ref | Module | Contains | Spare |
|---|---|---|---|
| MOD-01 | Head assembly | Sourced pump core in our housing, dome valve, collar, top gasket | ₹549 |
| MOD-02 | Nozzle | Single fixed mist orifice, bayonet | ₹99 |
| MOD-03 | Intake cartridge | Dip tube, 600 µm basket, 150 µm screen, carrier | ₹199 |
| MOD-04 | Body | 250 ml opaque tube, threaded both ends, etched fill line and QR | ₹449 |
| MOD-05 | Base cap | Cap, captive gasket, spare gasket recess, vent membrane | ₹179 |
| MOD-06 | Grip ring | LSR, anti slip, drip catcher, dry erase | ₹99 |
| ACC-01 | Dose counter | Clip on ratchet, 1,250 strokes, resettable | ₹399 |

Eleven individually replaceable parts was maximally repairable and practically
useless: eleven SKUs to stock, eleven things to lose in a sink, and a customer
who has to work out which one failed. Six is where repairability stops being a
slogan.

Module prices are set so repairing is always obviously cheaper than replacing,
and no single failure costs more than a third of a new set. If a price ever
breaks that rule, the module boundary is wrong, not the price.

## Bottom up BOM at 10,000 sets

| Module | ₹ |
|---|---|
| MOD-01 head assembly (pump core ₹150 of it) | 228 |
| MOD-02 nozzle | 16 |
| MOD-03 intake cartridge | 61 |
| MOD-04 body | 92 |
| MOD-05 base cap | 44 |
| MOD-06 grip ring | 22 |
| Sprayer final assembly, leak test, QC | 38 |
| **Enna Spray ex works** | **501** |
| Enna Store, 750 ml decanter | 174 |
| Set packaging incl. printed exploded drawing | 72 |
| **Ex works, the set** | **747** |
| Tooling amortised, ₹16 L over 25,000 sets | 64 |
| **Landed** | **≈ 811** |

**The head assembly is 46% of the sprayer**, and ₹150 of that is the sourced
pump core alone. Everything else in this product is cheap. Two consequences: the
supplier negotiation is where the margin lives, and pricing MOD-01 at ₹549 as a
spare is defensible rather than greedy.

At ₹1,799 the set: **55% gross margin before channel**, 49% direct, 41% on
marketplaces, 11 to 29% on quick commerce.

## Tooling: ₹16 lakh, which is ₹1 lakh over budget

Building our own head housing and tooling the decanter both cost money the
earlier plan did not spend.

| Item | ₹ |
|---|---|
| Head housing, nozzle, intake carrier (POM, multi cavity) | 4,60,000 |
| Sprayer body and base cap (SS forming, threading) | 3,20,000 |
| Decanter body and cap (SS forming) | 2,20,000 |
| Grip rings ×2, gaskets ×3 (LSR) | 1,40,000 |
| Prototype rounds ×3 | 1,60,000 |
| Validation testing | 90,000 |
| Contingency | 2,10,000 |
| **Subtotal** | **16,00,000** |
| ACC-01 counter tooling, deferrable | 90,000 |

**Recommendation: defer the counter.** It is an accessory with its own price and
its own demand and does not need to exist on day one. That lands the programme
at ₹16 lakh against a ₹15 lakh budget, with the ₹1 lakh gap covered by the
investor co funding already on the table. Contingency at ₹2.1 lakh is realistic
for a first tooling programme and cutting it to make the total look better is
how first tooling programmes fail.

## The repairability commitment

Written as it will be published, because it constrains the design rather than
describing it:

1. A public exploded drawing and part number for every module. A dimensioned
   drawing, not a marketing render.
2. Parts stocked ten years from last shipment. If we ever cannot supply one, we
   publish the drawing in enough detail for somebody else to.
3. **No adhesives, no ultrasonic welds, no rivets, nothing captive.** Threads and
   snap fits only. This is the constraint that does real work: it rules out the
   cheapest assembly method at almost every joint, and it is why the head is a
   housing around a pump core rather than a pump potted into a shell.
4. A repair QR on the body resolving to the drawing set and reorder page.

It is **not** open source hardware. We publish what a repairer needs, not the
full CAD, tolerances and process notes an import factory would need to clone the
geometry. That distinction should be held.

## The published interface

The head to body interface gets a version number and a public specification:
body mouth thread (four start, Ø48 mm, pitch, lead, tolerance band), face seal
land and flatness, nozzle bayonet form, intake cartridge register and clearance.

**What it buys:**
- **Future sizes cost one body tool.** A 500 ml body, or a 1 litre professional
  body, reuses MOD-01, 02, 03, 05 and 06 unchanged. The head becomes the platform
  and the bottle becomes the variable, which inverts how every competitor in this
  category is structured.
- **The food service version stops being a different product** and becomes a
  different body.
- Third party accessories become reach we did not pay for.

**The risk, stated plainly:** a published thread makes it easier for an import to
make a compatible body and undercut MOD-04. Accept it. The body is ₹92 of BOM and
the head is ₹228, and a customer who buys a cheap third party body still needs
our head, our nozzle and our intake cartridge. Publishing the interface concedes
the cheap half to defend the expensive half.

Versioning: a commitment not to break it, and if it ever must change, both
versions ship in parallel for two years.

## Still open

Top of the backlog: a **500 ml body module**, which proves the interface was
worth publishing and answers the only recurring objection to a 250 ml sprayer for
the price of one tool; and **nesting the set**, which costs nothing extra now the
decanter is being tooled and is the difference between a bundle and a system.
