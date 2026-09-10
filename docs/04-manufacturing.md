# Enna. Manufacturing, BOM and Channel Economics (Round 2)

> **Superseded in part.** The architecture, BOM and tooling figures here
> predate the modular rebuild. See `08-modular-architecture.md` for current
> numbers.

Budget confirmed: **₹15 lakh for tooling**, with investor co-funding available.
That is enough for real production tooling, not just soft tooling.

## 1. Supplier shortlist. Bangalore

These are **directory-sourced leads, not vetted vendors.** Nobody here has been
called, audited or quoted. Treat this as a call list.

### Injection moulding and tool room (Bangalore)

| Vendor | Location | Why shortlisted |
|---|---|---|
| **Kruger Industries** | Peenya Industrial Area | ISO 9001:2015, operating since 2004, nine moulding machines, **in-house product design and mould-flow analysis**, the mould-flow capability matters for the pump body and counter housing |
| **Fortune Group of Industries** | Peenya | Explicitly quotes **5 g, 90 g engineering plastics**, which is exactly our part-weight band |
| **Mathru Toolings & Components** | Abbigere | Tool development plus moulding, useful if we want the tool and the parts from one place |
| **Shree Sampath Plastics** | Peenya Industrial Estate | Established contract moulder, good fallback for second-source |

Peenya is the right cluster. It is Bangalore's engineering-manufacturing belt
and everything above sits within a few kilometres.

### Stainless steel body, probably not Bangalore

Honest finding: **India's stainless bottle industry is not in Bangalore.** It is
concentrated in Maharashtra (Palghar/Wada), Gujarat and Delhi NCR. Names that
surfaced: **Eagle Consumer Products**, **NIRLON Kitchenware** (Palghar). Expect
to split the supply chain, plastics in Bangalore, deep-drawn steel elsewhere,
assembly wherever we do final QC.

This is worth accepting rather than forcing. Deep drawing a Ø70 × 155 mm body
with a threaded mouth at both ends is a specialist operation, and the vendors
who do it at volume already do it for vacuum flasks.

### Qualification checklist before any of them get a rupee

1. Ask for a food-contact-grade material declaration and prior BIS/IS work.
2. Ask what they have tooled at our part size, see actual samples, not a deck.
3. Ask for their scrap rate on a comparable part.
4. Get a **T1 sample timeline in writing**, first-shot date, not "6, 8 weeks".
5. Insist on tool ownership in the PO. The tool is ours; we must be able to move it.
6. Second-source at least the nozzle and the seals from day one.

## 2. Indicative BOM, the set, at 10,000 sets

The product is now **two pieces sold as one SKU**: a 250 ml sprayer (Enna Spray)
and a 750 ml decanter (Enna Store). 250 + 750 = exactly one litre, one pouch,
nothing left over. Crucially it is **one box, one EAN, one marketplace listing**,
so the quick-commerce listing fee is paid once, not twice.

**Estimates, not quotes.** Every line needs a real number from a real vendor.

| Part | Process | Est. ₹/set |
|---|---|---|
| **Sprayer**, body, 18/8 SS, Ø58 × 118 | Deep draw + thread + polish | 78 |
| Base cap, SS, threaded | Deep draw + thread | 28 |
| Wide-mouth collar, SS | Formed | 24 |
| Pump cartridge (sourced pre-compression head) | Bought-in | 180 |
| Dose counter module | Injection moulded + assembly | 45 |
| Dip tube + intake basket, SS 316 | Tube + mesh forming | 34 |
| Fine screen, SS 316 | Stamped mesh | 12 |
| Silicone grip ring + 2 face gaskets | LSR moulded | 30 |
| Nozzle collar | Anodised alu or POM | 18 |
| Sprayer assembly, leak test, QC | Labour | 42 |
| **Decanter**, body, 18/8 SS, Ø82 × 165 | Deep draw + thread | 112 |
| Wide cap + drip-free pour spout | Formed + moulded | 40 |
| Silicone base ring | LSR moulded | 16 |
| Decanter assembly + QC | Labour | 14 |
| Set packaging, carton, insert, manual | Print + convert | 68 |
| **Ex-works subtotal** | | **741** |
| Tooling amortised (₹15 L over 25,000 sets) | | 60 |
| **Landed cost** | | **≈ 801** |

The **sourced pump head is 24% of the BOM** and remains the single biggest
lever, and the supplier negotiation is still the most valuable hour of work in
this project.

## 3. Channel economics at ₹1,799 per set

| Channel | Platform take | Net to us | Gross margin |
|---|---|---|---|
| D2C (own site) | ~2% gateway + ₹90 ship + 4% returns | ≈ ₹1,565 | **₹764 · 49%** |
| Amazon / Flipkart | ~25% all-in | ≈ ₹1,349 | **₹548 · 41%** |
| Quick commerce | 30, 45% all-in | ₹990, 1,259 | **₹189, 458 · 11, 29%** |

### The quick-commerce number nobody mentions

**Blinkit charges ₹25,000 per SKU per state as a listing fee** (returned as ad
wallet credit with a 12-month expiry). Zepto and Instamart run comparable
structures. Commission is 15, 22%, and total take reaches 30, 45% once you add
dynamic commission, ~₹50/order fulfilment, ~₹5/unit inwarding and ₹1, 2/unit/day
storage.

Selling the sprayer and the decanter as **one boxed SKU** is what makes the
two-piece system survive this. Two separate SKUs would double the fee in every
single state.

Even so, at ~₹300 margin each state costs roughly **420 sets of sales just to
clear the listing fee.** So:

1. **D2C plus Amazon/Flipkart first.** Build review velocity where margin is
   41, 49%, not 11, 29%.
2. **Quick commerce in phase two, in two metros, not eight.** A ₹1,799 durable
   is a considered purchase; quick commerce is built for impulse replenishment.
   The one genuinely quick-commerce-shaped moment is gifting season.

### Prerequisites for any marketplace or quick-commerce listing

- Registered entity with active **GSTIN**
- **GS1 EAN barcode**, one for the set
- Whether an **FSSAI licence** applies is genuinely unclear for an empty
  food-contact utensil (as opposed to a food product), **ask a compliance
  consultant, do not assume either way.** BIS food-contact conformity for the
  plastic and elastomer parts is required regardless.

## 4. What ₹15 lakh buys

| Item | Est. ₹ |
|---|---|
| Sprayer plastics tooling, pump housing, counter, nozzle (multi-cavity) | 5,00,000 |
| Sprayer SS body + base cap, forming and threading tools | 3,20,000 |
| Decanter SS body + cap tooling | 2,20,000 |
| LSR tooling, grip ring and three gaskets | 1,30,000 |
| Prototype rounds (SLA + machined, 3 iterations) | 1,60,000 |
| Migration, leak and clog testing | 90,000 |
| Contingency | 80,000 |
| **Total** | **15,00,000** |

**The contingency is too thin at ₹80,000.** First tools almost always need a
correction cut, and ₹80k does not cover one. Two ways out:

- **Recommended: don't tool the decanter.** A 750 ml opaque stainless bottle
  with a wide mouth is a commodity, vendors in Palghar and Gujarat make them by
  the container load. Source it, brand it, and put the entire ₹2.2 lakh back
  into contingency. **The sprayer is the invention; the decanter is a bottle.**
  This also shortens the timeline, because only one product needs new tools.
- Or raise the tooling budget to ₹17 lakh using the investor co-funding already
  on the table.

Taking the first option puts contingency at ₹3 lakh, which is a realistic
number for a first tooling programme.
