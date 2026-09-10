# Enna. Market & Teardown Research (Round 1)

Date: 2026-09-10. Desk research pass before design work begins.

## 1. The mechanism landscape

Every cooking-oil sprayer on the market is one of four architectures. Choosing
between them is the single highest-leverage decision in this project.

| Architecture | Example | How it works | Strengths | Failure modes |
|---|---|---|---|---|
| **Pump-pressurised bottle** | Misto (aluminium) | User pumps 10, 30 strokes to pressurise the headspace; a button releases air-driven flow | Continuous hands-free spray; cheap; few moving parts | Pressure decays mid-use → spray quality drifts; pumping is a chore; headspace air accelerates oxidation/rancidity |
| **Trigger pump** | Evo, most Amazon/Temu units | Each trigger squeeze pumps a metered shot through a nozzle | Instant, no pre-pumping; big output per stroke | Hand fatigue; spray quality depends on squeeze speed → sputter/jet instead of fan; most clog-prone |
| **Pre-compression trigger** | Flairosol (AFA Dispensing, NL) | Trigger fills a *pressure chamber* behind a dome valve with a preset cracking pressure. Valve only opens above that pressure, so output is constant regardless of squeeze speed. Repeat pumping = continuous mist | Aerosol-quality mist without propellant; consistent; leak-free by design; tolerant of viscosity | Complex, more parts, licensed/patented |
| **Bag-on-valve (BOV)** | La Tourangelle, commercial sprays | Oil in a sealed inner bag, compressed air outside it | Zero oxidation, 99% evacuation, perfect mist | Not refillable by the consumer, kills the whole premise |

**The key technical insight:** the *pre-compression valve* is why the Flairosol
mists consistently and cheap sprayers sputter. In a plain trigger pump the
nozzle sees whatever pressure your hand produces; below the atomisation
threshold you get a squirt, not a mist. A dome/pre-compression valve puts a
pressure floor under every discharge. Flairosol also ships a **built-in filter**, a reviewer reported eight months of thick oils without a clog.

Relevant patents to read for freedom-to-operate:
- US8905271B2 / US20120048959A1, "Sprayer device with aerosol functionality (Flairosol)"
- US9714133 / US20130112766A1, "Flairosol II", metered + active
- EP2566629B1. European equivalent
- US5455055 / US5650185, "Non-aerosol, uniform spray dispersion system for oil-based products" (the original Evo-lineage patents, filed early 1990s, **almost certainly expired**, so the base non-aerosol oil trigger concept is public domain)
- US5467900 / US5730335, precompression valve for trigger sprayer (1990s, expired)
- WO2016077114A1, "Spray nozzle for high viscosity (e.g. oil) spray applications with uniform spray distribution", directly on point, must be reviewed
- US6283335, oil sprayer with hand-operated air pump (the Misto lineage)

Preliminary read: the 1990s precompression and non-aerosol oil-spray patents
have lapsed. The live risk is AFA's Flairosol family (2010, 2013 priority, live
until ~2030, 2033). Our design must either design around the dome-valve claim
set or license it.

## 2. Documented failure modes (what customers actually complain about)

Compiled from Amazon/Walmart/QVC review analysis of Evo, Misto and the generic
imports:

1. **Clogging, the #1 cause of death.** Oil residue polymerises in the nozzle
   and dip tube. Worse with thick, unfiltered or infused oils. Units reported
   dead in under 10 uses; one Evo clogged "useless" in two weeks.
2. **Spray pattern degradation.** Works once, then sprays two jets at ~90° or a
   straight stream instead of a fan.
3. **Leaking at the closure.** Oil weeps where the head twists onto the body;
   cross-threading is common; one reviewer had the head separate mid-spray and
   dump the contents.
4. **Impossible to clean.** Evo's flared body geometry cannot be reached; an oil
   sheen remains after washing; users fear rancidity they can't wash out.
5. **Mechanical fatigue.** Nozzle pops up when pumped, spray force falls, nozzle
   seizes, typically at ~1 month.
6. **Heat distortion.** A plastic-topped unit left near a hot hob deformed and
   then leaked.
7. **Messy refills.** Narrow necks; "oil gets everywhere when refilling."
8. **No support.** Repeated unanswered warranty contacts.

Every one of these is an addressable design requirement, not bad luck.

## 3. India-specific constraints nobody has designed for

- **Solidification.** Coconut oil solidifies below ~24 °C. It *will* clog any
  sprayer in a Bengaluru or north-Indian winter. Ghee is solid at room
  temperature for much of the year. Any honest India-first product must either
  handle this or state the boundary clearly.
- **Viscosity spread.** Indian kitchens rotate mustard, groundnut, sesame
  (gingelly), sunflower, rice bran, coconut and ghee, a far wider viscosity and
  particulate range than the olive-oil-only Western use case a sprayer is tuned for.
- **Reused / filtered oil.** Reuse after frying is normal practice. Carried-over
  particulate (besan, crumbs, masala) is the direct cause of clogs. This is the
  single biggest India-specific engineering problem and the clearest place to win.
- **Refill culture.** Bottles are refilled repeatedly from a larger tin, so
  fill ergonomics and cleanability matter far more than in the West.
- **Heat.** Bottles live next to the hob. Plastic tops distort.
- **Price anchoring.** Amazon.in / Flipkart mass market sits at roughly ₹200, ₹600
  (Perfect Pricee, CRIYALE, Shopbox, Ramkuwar, SITOVI, TrendPlain, Rushwak);
  a ₹500, ₹1,000 band exists but is thin. Evo is ~$30 (≈₹2,600) and not really
  sold here. There is an unoccupied premium slot.

## 4. Materials

- **Stainless 18/8**, opaque, blocks ~99% of light, roughly doubles oil shelf
  life vs. clear containers; will not shatter; will not distort near the hob.
  Best body candidate.
- **Glass**, the Japanese market favours heat-resistant (JFSL370) glass with a
  filter tube; but it breaks, which the brief rules out.
- **Tritan**, safe from a verified supplier but degrades under prolonged UV and
  offers no light protection. Acceptable only as a small level window, not a body.
- **Conclusion:** opaque SS body; a narrow Tritan/borosilicate level strip if a
  fill indicator is wanted; food-grade silicone for seals and base; POM/PP for
  the pump internals.

## 5. Japanese market signals

Amazon.co.jp bestsellers converge on: heat-resistant glass, ~250 ml, mist spray,
explicit **no-drip** design, an **oil tube with an integral filter**, "zero
residue", and **2-in-1 spray + pour**. The filter-in-the-dip-tube idea is
already validated there. It is simply absent from the Indian market.

## 6. Regulatory (India)

- Food-contact plastics must conform to the applicable Indian Standard. IS 10146 for polyethylene, with sibling standards for PP, PS etc., per the
  FSS (Packaging & Labelling) Regulations.
- FSSAI 2.4.1: food-contact material must not transfer substances that endanger
  health or alter the food's composition or sensory character.
- BIS logo + licence number alongside FSSAI marks on primary packaging where the
  FBO route applies.
- Migration testing on the plastic and elastomer components will be needed.

## 7. IP (India)

- **Design registration** (Designs Act 2000): protects appearance only.
  ₹1,000/design government fee for individuals, startups and small entities
  (Form-24 + MSME/DPIIT proof), ₹4,000 otherwise; ₹5,000, ₹8,000 attorney fee.
  10 years, extendable by 5. Typically 6, 12 months.
- **Patent**: needed for the functional novelty, the filtration + anti-sediment
  intake + viscosity-adaptive nozzle. Provisional first, then complete within
  12 months.
- **Trademark**: "Enna" (from எண்ணெய் / *ennai*, Tamil for oil), class 21
  (kitchen utensils and containers) primarily, plus class 8/11 as relevant.

## 8. Manufacturing economics (India)

- Injection-mould tooling: ₹2 lakh, ₹30 lakh+ depending on cavitation and
  complexity; India runs 40, 60% below EU/US for equivalent quality.
- Part cost ₹1, ₹60+ depending on material, geometry and volume.
- Worked example from the trade: PP part, 5 lakh/yr, 8-cavity tool at ₹5 lakh,
  ₹5/pc production → ₹1/pc amortised tooling → ₹6/pc effective.
- The pump assembly is the cost driver, not the bottle. Options: license a
  Flairosol-class head, buy an off-the-shelf trigger head and re-engineer the
  wetted path, or tool our own head (highest cost, highest defensibility).

## Sources

- https://cleangreensimple.com/article/best-olive-oil-sprayers/
- https://www.globalaerosols.com/aerosol-vs-pump-spray-vs-trigger-spray-technical-comparison/
- https://patents.google.com/patent/US8905271B2/en
- https://patents.google.com/patent/WO2016077114A1/zh
- https://reviews.cookistry.com/2014/12/evo-oil-sprayer.html
- https://www.walmart.com/reviews/product/49423461
- https://community.qvc.com/t5/Kitchen/EVO-oil-sprayer/td-p/7916313
- https://chopchic.com/how-to-clean-oil-sprayer/
- https://www.amazon.co.jp/gp/bestsellers/kitchen/10477955051
- https://www.amazon.in/Cooking-Oil-Sprayers/b?ie=UTF8&node=27972572031
- https://www.flipkart.com/kitchen-cookware-serveware/oil-sprayer~type/pr?sid=upp
- https://www.khlaw.com/insights/regulation-food-contact-materials-india
- https://www.intepat.com/blog/industrial-design-e-filing-fee-structure-in-india
- https://www.moldrite.in/blog/injection-molding-cost-india
- https://blog.jivo.in/is-it-safe-to-use-cooking-oil-after-it-turns-solid-in-winter/
