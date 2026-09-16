# Enna: Combined Patentability Assessment and Draft Patent Specification

**Version 3, 16 September 2026. Supersedes versions 1 and 2. Draft for
instructing a patent attorney. Not legal advice.**

I am not a patent attorney. This is a technically detailed draft and a reasoned
assessment, written so a registered agent can take it, run a proper search, and
file. Claim language must be reviewed by a professional before filing.

**Version 3 demotes the powered thermal family.** Version 2 led with a USB
heating element. On review that is the wrong product: it adds a controller, a
sensor, a heater, a power input and an electrical certification programme to
solve a problem that a single rotating collar solves with one moving part and no
power at all. The thermal aspects are **retained in the specification and in the
claims**, because keeping them in the priority filing is nearly free and they may
matter for a professional model later, but they are no longer the lead invention.

The lead invention is now the combination in Part B4: a **manual viscosity
calibration collar** whose setting is taught to the user by the interlock itself.

---

# PART A. Legal position

## A1. The website is now password protected

Noted, and it was the right move. Two qualifications.

**It stops further disclosure accruing. It does not undo disclosure that already
happened.** If the site was publicly reachable for any period, that publication
stands against you in Europe and India, where there is effectively no grace
period. The remedy is not retroactive.

**You still need the first-public date.** Ask the attorney's opinion on the facts,
and gather the evidence now while it exists:

- the Amplify deployment log, which timestamps when each branch first went live
- whether a custom domain was ever pointed at it
- whether Google or Bing indexed it, checkable with a `site:` search and in
  Search Console
- whether the URL was ever shared in a message, post or email, and when
- the Wayback Machine, which is the most likely third party record

If the honest answer is that it was live and indexed for some weeks, the position
is: **the US remains available for twelve months from that date, Europe and India
are compromised for the features that were published, and the thermal and
metering inventions below are unaffected because they were never disclosed.**

## A2. Section 39 still dictates the filing order

Unchanged and non negotiable. If any inventor is resident in India, you may not
file abroad unless an Indian application for the same invention was filed **at
least six weeks earlier**, or Form 25 permission has been granted. Section 118
provides imprisonment up to two years, or a fine, or both, and the Indian
application may be deemed abandoned and a granted patent revoked.

**File the Indian provisional first. Everything else follows from that.**

## A3. What is clean and what is not

I audited the repository and the site again for version 2.

| Subject matter | Published before filing | Status |
|---|---|---|
| Raised intake standoff, 9 mm | Yes, on the site | At risk in EPO and India |
| Two stage filtration, 600 and 150 µm | Yes | At risk in EPO and India |
| Pre-compression valve, 2.4 bar | Yes | At risk in EPO and India |
| Body open at both ends, face seals | Yes | At risk in EPO and India |
| 0.20 ml metered dose, stroke counter | Yes | At risk in EPO and India |
| **Fill completion interlock** | **No** | **Clean everywhere** |
| **Refill time as viscosity measurement** | **No** | **Clean everywhere** |
| **Heating the metered charge only** | **No** | **Clean everywhere** |
| **Closed loop viscosity normalisation** | **No** | **Clean everywhere** |
| **Solid fat melt mode** | **No** | **Clean everywhere** |
| **Filter obstruction self diagnosis** | **No** | **Clean everywhere** |

Every one of the six strongest inventive concepts is clean. The compromised
material is the part that was always the weaker patent subject matter anyway,
and most of it belongs in a design registration.

---

# PART B. Patentability assessment

## B1. The problem, restated

A hand actuated positive displacement pump delivers its nominal swept volume only
if the metering chamber completely refills between strokes. Refill is driven by a
return spring drawing liquid through the intake, and that flow follows
approximately

```
Q  ≈  π · ΔP · r⁴  /  (8 · μ · L)
```

so **refill time is directly proportional to dynamic viscosity**. Edible oil
viscosity roughly doubles for each 20 °C fall in temperature and varies again
between oils, so a device may encounter a threefold range in ordinary use.

A user actuates at a habitual cadence and does not vary it by oil. When refill
time exceeds the interval between strokes, the chamber is partly charged and the
delivered volume falls, **with no perceptible change in the action**. Volume can
fall by forty percent unnoticed. For a product whose proposition is portion
control and a stated energy per stroke, the printed number is then wrong for half
the year.

## B2. Why the known art does not solve it

**Pre-compression and discharge regulation.** US 5,467,900, US 5,730,335,
US 8,905,271, US 9,714,133, EP 2,566,629.

> A pre-compression valve regulates the conditions under which the metering
> chamber empties. It has no effect whatever on whether the chamber was full when
> emptying began. The volumetric error is created during the return stroke,
> before the discharge valve participates at all. This distinction should be
> stated explicitly in the specification because it is the cleanest separation
> from the closest commercial art.

**Nozzle assemblies for viscous liquids.** US 6,659,369, which expressly concerns
trigger sprayers and cooking oil, and WO 2016/077114. These improve atomisation
quality, not delivered volume.

**Powered and programmable metering.** US 5,022,556; DE 10 2012 100 306, expressly
a method for adapting a metering pump to the viscosity of the medium, which
recognises that viscous media need longer intake and delivery times;
US 4,518,105. Each requires power, control apparatus or operator configuration,
and each addresses viscosity by **adapting the pump to the fluid**.

**The inventive direction here is the opposite of that last group**, and the
distinction is worth making expressly: rather than adapting the machine to
whatever viscosity arrives, the present invention **normalises the fluid to a
target viscosity** and lets a fixed geometry machine do the rest.

## B3. Aspect 1: the mechanical base, unpowered

**The observation.** During the return stroke the piston can advance only as fast
as liquid enters behind it. **The position of the piston is therefore a direct
measure of the state of charge of the chamber**, whatever the viscosity.

**The invention.** A fill completion interlock holds the actuator blocked and
releases only when the piston reaches its return stop. The device physically
cannot fire on a partial charge. Delivered volume becomes a function of geometry
alone, and the viscosity error moves off the axis the user cannot perceive, which
is volume, onto one they can, which is a short delay.

This aspect requires no power at all, and it is what the first product ships.

## B4. Aspect 2: the manual viscosity calibration collar

This is the preferred embodiment and the one that should be built.

### B4.1 The variable to adjust is flow resistance, not swept volume

The obvious proposal is a collar, marked per oil, which alters the swept volume of
the metering chamber. **The instinct is correct and the variable is wrong.**

If the collar shrinks the swept volume so that a viscous liquid fills the chamber
completely within the available interval, the chamber does fill, but the delivered
volume is then the shrunken volume. At three times viscosity the device delivers
0.067 ml in place of 0.20 ml. **That is precisely the error the invention exists to
remove, made repeatable rather than random.** Repeatably wrong is an improvement on
randomly wrong, and it is not the objective.

What the collar must adjust is the resistance the refill flow encounters, since
that is what viscosity acts upon. From

```
t  ∝  mu / ( dP · r⁴ )
```

there are two available levers, with very different economics.

| Viscosity range to be covered | By driving pressure | By inlet radius | By inlet area |
|---|---|---|---|
| 2 times | 2.00 times | **1.19 times** | 1.41 times |
| 3 times | 3.00 times | **1.32 times** | 1.73 times |
| 4 times | 4.00 times | **1.41 times** | 2.00 times |

**Driving pressure compensates linearly.** Trebling it requires trebling the return
spring force, and the user compresses that same spring on every delivery stroke, so
the squeeze effort trebles with it. This lever is ergonomically capped.

**Inlet radius compensates as the fourth root.** A threefold viscosity range
requires the aperture to be opened by thirty two percent. That spans every edible
oil in ordinary Indian use across the whole year, costs nothing in squeeze effort,
and occupies a small, precise arc of collar rotation.

**The fourth power dependence is the whole design.** It is the reason this works as
a hand set collar rather than as a control system.

### B4.2 Construction

A collar is rotatably mounted on the head assembly and carries an arcuate port of
progressively varying width which registers with the inlet passage. Rotation of the
collar therefore varies the effective flow area of the inlet without altering the
swept volume of the metering chamber, the stroke of the piston, or the force of the
return spring.

Detents define discrete positions. Indicia adjacent each detent identify a class of
liquid, for example gingelly, groundnut, sunflower, or a season, for example warm
and cool. The collar may additionally act as the closure which secures the head
assembly to the reservoir, so that it introduces no additional part at all.

A thermally responsive element may bias the collar's effective aperture with
ambient temperature, so that the collar's markings address the class of oil and the
element addresses the season automatically.

### B4.3 The interlock teaches the collar setting, at no cost

This is the feature which makes the arrangement self explanatory, and it is
emergent rather than designed in.

If the collar is set for a liquid thinner than the one present, the metering chamber
will not have charged when the user attempts the next delivery stroke, and **the
fill completion interlock of Aspect 1 blocks the actuator and imposes a perceptible
pause.** If the collar is set correctly, the chamber charges within the user's
natural cadence and **no pause occurs at all.**

A user who perceives a pause therefore advances the collar by one detent until the
pause ceases. **That is the entire instruction for use**, and it requires no
display, no sensor, no indication and no written manual.

The arrangement is functionally the same closed loop as the powered embodiment of
Part B5, with the user performing the role of controller and the interlock
performing the role of sensor. It is achieved with **two additional components**.

### B4.4 Parts count, which is the commercial argument

| Approach | Added components | Power | Certification |
|---|---|---|---|
| **Collar plus interlock** | **2: a latch and a collar** | **None** | Food contact only |
| Powered normalisation | 6 or more: heater, thermistor, stroke sensor, controller, power input, energy store | USB | Electrical safety, possibly BIS registration, possibly cell certification |

## B5. Aspect 3 onwards: what a heating element would additionally unlock

**Retained for the priority filing, not for the first product.** The analysis below
stands on its merits and the claims are worth holding, but nothing here should be
built until the collar has been proven on the bench and the unpowered product has
shipped.

A USB powered heating element, worked through, produces four further inventive
concepts which interlock with Aspect 1 rather than merely sitting alongside it. **That functional interaction
matters a great deal at the EPO**, where a mere collocation of features is not
inventive but a genuine synergy is.

### B5.1 Heat the charge, not the bottle

The naive implementation heats the reservoir. The numbers make that untenable and
make the alternative obvious once stated:

| What is heated | Mass | Energy for +25 °C | Time at 15 W |
|---|---|---|---|
| Whole 250 ml reservoir | 230 g | 11,500 J | **12.8 minutes** |
| **One 0.20 ml metered charge** | **0.18 g** | **9.2 J** | **0.61 seconds** |

A factor of **1,250**. Heating the reservoir is an appliance that must be switched
on a quarter of an hour before cooking, and which holds the entire contents warm,
accelerating oxidation of oil that will not be used for weeks.

**Heating only the charge already isolated in the metering chamber is feasible on
ordinary USB power, happens within the time the user is already holding the
device, and leaves the bulk oil cold and unoxidised throughout its life.** This is
a claim in its own right.

### B5.2 The pump is already a viscometer

Aspect 1 gives the device a return stroke whose duration is proportional to
viscosity, and an interlock that already detects the end of that stroke. This is
the same signal the user reads by feel in Part B4.3, read instead by a timer.

**Therefore the duration between the start of the return stroke and the release of
the interlock is a direct measurement of the viscosity of whatever liquid is in
the device**, obtained with no viscometer, no added sensor beyond a timer, no user
input and no oil type selection.

The device can identify the fluid it has been filled with, by itself, from a
function it was already performing.

### B5.3 Closed loop normalisation to a target viscosity

Combining B5.1 and B5.2 closes a loop:

1. Time the return stroke. That is the viscosity.
2. Compare with a target duration corresponding to a target viscosity.
3. Heat the next charge by the amount needed to close the gap.
4. Repeat.

The pump then always sees the same viscosity, so **both the delivered volume and
the atomisation quality become constant**, across every oil and every season,
without the user knowing any of it happened. The heater is bounded at a
conservative ceiling, 60 °C in the draft, far below any smoke point and low
enough that brief exposure does not meaningfully oxidise the charge.

Note the synergy, and put it in the specification explicitly: **the interlock
creates a dwell; the dwell is the measurement; the dwell is also the window in
which the heating occurs; and the heating shortens the dwell.** The features are
not merely combined, they feed one another.

### B5.4 Solid fat mode

If the piston does not move at all when the return spring is released, the
contents are not a viscous liquid, they are a solid. Coconut oil below about
24 °C and ghee for much of the Indian year.

The controller can detect exactly that condition, from the same signal, and run a
melt cycle on the intake path before attempting to charge. **The limitation the
product page currently states honestly, that solid fats cannot be sprayed, becomes
addressable rather than permanent.**

### B5.5 The device diagnoses its own filter

Refill time depends on viscosity and on the flow resistance of the intake path. If
the measured refill time is longer than the measured temperature can account for,
**the additional resistance is an obstruction**, and the device can say so.

A dispenser that tells the user its filter needs cleaning, before the spray
degrades, is a genuinely novel answer to the failure mode that kills every product
in this category.

## B5. Honest weaknesses to put to the attorney

1. **Interlocks are old.** Dose interlocks exist in inhalers and injection pens.
   The inventive step rests on purpose and combination: an interlock used to make
   delivered volume independent of fluid viscosity. Expect a citation of an
   inhaler lockout; the answer is that those meter a pre loaded charge and address
   dose counting or end of life lockout, not the refill dynamics of a viscous
   liquid.
2. **Obviousness of waiting.** An examiner may say it is obvious to wait for the
   chamber to fill. The rebuttal is that the art consistently solved viscosity by
   adding power and control, per DE 10 2012 100 306, which is evidence that the
   simple mechanical route was not obvious to the skilled person.
3. **Inferring viscosity from a timing is not new in the abstract.** Capillary and
   falling body viscometry are ancient. The novelty is doing it with the dispensing
   pump itself, as a by product of an interlock provided for a different purpose,
   in a hand actuated dispenser.
4. **Heated dispensers exist**, for chocolate, wax, adhesives and cosmetics. The
   search must specifically cover heated dispensing. The distinguishing features
   are heating the metered charge in isolation rather than the reservoir, and
   heating to a viscosity target rather than a temperature target.
5. **Unity of invention is a real risk.** See Part E3. This document contains at
   least six inventive concepts and a PCT examiner may well object.
6. **Claim 1 must not be limited to edible oil.** Claim the fluid class broadly
   and make edible oil dependent.
7. **Adjustable dispensers are a crowded field**, and the search must cover
   adjustable dose pumps, adjustable flow restrictors and multi position outlet
   selectors thoroughly. **The distinguishing feature to press is that the
   calibration member varies flow resistance while holding swept volume,
   stroke and spring force constant.** Almost every adjustable pump in the art
   varies the dose; this one exists specifically in order not to.
8. **The collar and the interlock should be claimed both together and
   separately.** Claim 63 is the valuable one because the emergent feedback is
   the inventive heart, but claim 55 must stand alone in case 63 is attacked.

---

# PART C. Draft specification

## Title

**A dispenser and method for delivering metered volumes of liquid substantially
independently of liquid viscosity**

## Technical field

Manually actuated dispensers for liquids, and in particular hand operated pump
dispensers delivering a metered volume of a liquid of variable and unknown
viscosity, such as an edible oil, per actuation.

## Background

*As set out in Part B1 and B2 above; the attorney should render those passages
into the formal background section, expressly distinguishing pre-compression
valves, viscous nozzle assemblies, and powered adaptive metering pumps.*

## Summary of the invention

According to a **first aspect** there is provided a manually actuated dispenser
comprising a reservoir, a metering chamber of fixed swept volume, a metering
piston, a manually operable actuator, a return spring, an inlet valve and a
discharge valve, **characterised by a fill completion interlock** operatively
coupled between the metering piston and the actuator and arranged to prevent the
actuator from executing a delivery stroke until the metering piston has attained a
predetermined fill position corresponding to the fixed swept volume.

The invention proceeds from the recognition that **the position of the metering
piston during the return stroke is itself a direct measure of the state of charge
of the metering chamber**, because the piston can advance only as rapidly as
liquid enters behind it. Interlocking the actuator to that position converts a
volumetric error, which the user cannot perceive, into a short delay, which they
can.

According to a **second aspect** there is provided such a dispenser further
comprising a heating element arranged to heat **the liquid within the metering
chamber**, in thermal isolation from liquid remaining in the reservoir. Because
the metered charge is of the order of one thousandth of the reservoir contents, it
may be raised through a useful temperature interval within a fraction of a second
using power available from a USB supply, whereas heating the reservoir would
require of the order of a thousand times the energy and would hold the entire
contents warm, accelerating oxidative degradation of liquid not yet used.

According to a **third aspect** there is provided such a dispenser comprising a
controller arranged to determine a parameter indicative of the viscosity of the
liquid from **the duration of the return stroke**, that duration being measured
between commencement of the return stroke and attainment of the predetermined fill
position. No viscometer, no additional sensing of the fluid, and no user input or
selection of liquid type is required.

According to a **fourth aspect** the controller is arranged to regulate the
heating element **in dependence upon said duration**, so as to drive the duration
towards a target duration corresponding to a target viscosity. The metering
chamber then receives liquid of substantially constant viscosity irrespective of
the liquid supplied or the ambient temperature, so that both the delivered volume
and the atomisation quality are rendered constant.

According to a **fifth aspect** the controller is arranged to determine, from an
absence of movement of the metering piston upon release of the return spring, that
the contents are not in a flowable state, and in response to energise the heating
element in a melt mode prior to attempting to charge the metering chamber.

According to a **sixth aspect** the controller is arranged to compare the measured
return stroke duration with a duration predicted from a measured temperature, and
to generate an obstruction indication where the measured duration exceeds the
predicted duration by more than a threshold, thereby indicating obstruction of a
filter element.

## Brief description of the drawings

- **Figure 1** sectional elevation of the dispenser.
- **Figure 2** enlarged section of the metering chamber and fill completion interlock, blocking configuration, chamber partially charged.
- **Figure 3** as Figure 2, chamber fully charged, releasing configuration.
- **Figure 4** enlarged section of the differential pressure responsive inlet valve showing the progressive seat profile.
- **Figure 5** section of the removable intake cartridge showing the raised inlet opening and the two filter elements.
- **Figure 6** exploded view showing the separable modules.
- **Figure 7** graph of delivered volume against liquid viscosity, invention and conventional dispenser.
- **Figure 8** schematic of the heating element, temperature sensor, stroke sensor, controller and power input.
- **Figure 9** control flow diagram of the closed loop viscosity normalisation, melt mode and obstruction detection.
- **Figure 10** graph of return stroke duration against liquid temperature for three edible oils, showing the target duration band.
- **Figure 11** section through the calibration collar and its arcuate port, at the least and greatest flow area settings.

## Detailed description

### Overall arrangement, Figure 1

A tubular reservoir (10) having a floor (11) is closed at a first end by a head
closure (12) and at a second end by a base closure (13), each sealed by an axial
face seal (14) compressed by a multi start thread, so that the reservoir may be
opened at both ends.

Within the head closure (12) is a metering chamber (20) of fixed swept volume,
having an inlet (21), an outlet (22) and a metering piston (23) slidable between a
discharge position and a fill position. A return spring (24) urges the piston
towards the fill position. An inlet valve (25) admits liquid during the return
stroke. A discharge valve (26), preferably a pre-compression valve of predetermined
cracking pressure between 1.5 and 4 bar and in one embodiment 2.4 bar, communicates
with a discharge orifice (27).

A manually operable actuator (30), a trigger pivoted at (31), carries a drive
member (32) bearing on a piston rod (33). Liquid is drawn through an intake
conduit (50).

In one embodiment the swept volume is between 0.1 and 0.5 ml, in a particular
embodiment 0.20 ml, corresponding to approximately 0.18 g and approximately
1.7 kilocalories of a typical edible oil.

### The fill completion interlock, Figures 2 and 3

A latch member (41) is pivotally mounted within the head closure (12) and
resiliently biased into a blocking configuration in which its nose lies in the
path of the drive member (32) and engages a detent surface (42) thereon. In that
configuration no delivery stroke can occur.

The piston rod (33) carries a release cam (44). As the return spring (24) drives
the piston (23) towards the fill position, liquid is drawn in through the inlet
valve (25). **The piston advances only as rapidly as liquid enters behind it.** The
rate of advance is governed by viscosity; the final position is not.

When, and only when, the piston (23) abuts a return stop (43) defining the fill
position, the release cam (44) displaces the latch member (41) clear of the drive
member (32) and a delivery stroke becomes possible, expelling the full swept
volume.

Preferably the latch (41) and detent surface (42) are profiled to permit a small
lost motion of the actuator whilst blocked, so that the user perceives a short
positive resistance rather than a rigid obstruction, and release produces a
tactile and audible detent signalling that a complete dose is available.

With a low viscosity liquid the chamber charges within a small fraction of a
second and the interlock is imperceptible. With a cold or viscous liquid the delay
is of the order of a second. **In neither case does the delivered volume change.**

### Passive viscosity compensation, Figure 4

The inlet valve (25) comprises a poppet resiliently biased against a seat having a
progressive profile, such that the annular flow area increases more than linearly
with poppet lift. Poppet lift is a function of the pressure differential across
the valve; for a given flow a more viscous liquid generates a greater differential
and therefore opens a larger area. The valve compensates passively and in the
correct direction, without sensing, power or adjustment.

A thermally responsive element (80), a bimetallic or shape memory alloy element,
may be disposed in the inlet path and arranged to reduce the bias upon the poppet
as temperature falls, anticipating rather than merely responding to the associated
rise in viscosity.

These passive features operate in embodiments having no power source at all, and
also serve in powered embodiments to shorten the interval that the heating element
must bridge.

### Intake and filtration, Figure 5

The intake conduit (50) terminates in an inlet opening (51) held at a standoff
(52) of between 5 and 15 mm, in one embodiment 9 mm, above the floor (11),
defining beneath it a settling volume (53) into which particulate descends and
from which it is not drawn. A first filter element (54) of aperture between 400
and 800 µm, in one embodiment 600 µm, is disposed at the inlet opening. A second
filter element (55) of smaller aperture, between 100 and 200 µm and in one
embodiment 150 µm, is disposed upstream of the discharge orifice (27). Preferably
the conduit and both filter elements are carried on a common carrier (56) and are
removable as a single cartridge.

### Thermal subsystem, Figure 8

A heating element (100), for example a positive temperature coefficient ceramic
element or a thin film resistive element, is disposed in thermal contact with the
metering chamber (20) and arranged to heat liquid **within that chamber**. A
thermal break (105) of low thermal conductivity separates the metering chamber
from the intake conduit (50) and from the reservoir (10), so that heat is not
conducted into the bulk liquid.

A temperature sensor (101), for example a thermistor, senses the temperature of
liquid in or adjacent the metering chamber. A stroke sensor (104) detects
attainment of the predetermined fill position; conveniently this is a switch or
optical detector actuated by the release cam (44) or the latch member (41), so
that the interlock provided for the first aspect also serves as the sensing
element.

A controller (102) receives signals from the sensors (101, 104) and regulates the
heating element (100). Electrical power is received at a power input (103),
suitably a USB Type C receptacle. An energy store (106), a capacitor or cell, may
buffer the supply so that a charge may be heated at a power exceeding the
instantaneous supply capability. An indicator (107) conveys state to the user. A
grip sensor (108) may initiate preheating on the device being picked up.

**Energy budget.** A metered charge of 0.20 ml has a mass of approximately 0.18 g.
At a specific heat capacity of approximately 2.0 J/g/K, raising it by 25 K requires
approximately 9.2 J, achieved in approximately 0.61 s at 15 W. Raising the whole
of a 250 ml reservoir through the same interval would require approximately
11,500 J and approximately 12.8 minutes at the same power, a factor of
approximately 1,250. **This disparity is what makes charge only heating practical
and reservoir heating impractical**, and it is additionally what preserves the
quality of liquid that will not be dispensed for some weeks.

The controller limits the temperature of the charge to a predetermined maximum,
preferably not exceeding 60 °C, which is far below the smoke point of edible oils
and low enough that the brief exposure of an individual charge does not
meaningfully promote oxidation.

### Viscosity determination and closed loop normalisation, Figures 9 and 10

Upon release of the actuator (30) the return spring (24) drives the return stroke.
The controller (102) starts a timer and stops it upon the stroke sensor (104)
indicating attainment of the fill position. **The elapsed duration is a monotonic
function of the viscosity of the liquid**, the geometry of the intake path and the
force of the return spring both being fixed and known.

The controller compares that duration with a target duration corresponding to a
target viscosity, and regulates the energy delivered to the heating element (100)
for the succeeding charge so as to drive the measured duration towards the target.
The loop converges over a small number of strokes.

The consequence is that the metering chamber, the discharge valve and the orifice
all receive liquid at substantially constant viscosity, **whatever liquid has been
placed in the reservoir and whatever the ambient temperature**. Delivered volume
and atomisation quality are both thereby stabilised.

There is a functional synergy between the aspects which should be noted. The
interlock of the first aspect creates a dwell between strokes; the duration of
that dwell constitutes the viscosity measurement of the third aspect; the dwell is
also the interval during which heating under the second aspect is performed; and
that heating shortens the dwell. **The features are not merely collocated, they
each enable and modify the others.**

### Melt mode

Where, upon release of the return spring (24), the stroke sensor (104) indicates
no movement of the piston (23) within a predetermined interval, the controller
determines that the contents are not in a flowable state. It then energises the
heating element (100) in a melt mode, directed to the intake path, until movement
commences or a timeout expires. This permits use with fats which are solid at
ambient temperature, such as coconut oil below approximately 24 °C, and clarified
butter.

### Obstruction detection

The controller stores a relationship between temperature and expected return
stroke duration for an unobstructed intake path. Where the measured duration
exceeds the duration predicted from the measured temperature by more than a
predetermined threshold, the controller determines that a filter element (54, 55)
is obstructed and generates an indication via the indicator (107). **The dispenser
thereby warns of an impending clog before spray quality is affected**, the clog
being the predominant failure mode of dispensers of this class.

### Further features

A counter (60) registers delivery strokes and indicates volume remaining and, for
a liquid of known energy density, energy dispensed. In unpowered embodiments the
counter is mechanical and may be a separable module; in powered embodiments it may
be implemented in the controller (102).

A vent (70) comprising a hydrophobic membrane admits air to the reservoir while
excluding moisture and airborne particulate. An internal fill line is formed on
the inner wall of the reservoir, visible through the opened head closure.

### Performance, Figure 7

For a conventional dispenser, delivered volume falls progressively as viscosity
rises above the design value. For a dispenser according to the first aspect,
delivered volume remains substantially constant, the effect of viscosity appearing
as an increase in the minimum interval between actuations. For a dispenser
according to the fourth aspect, **both the delivered volume and that interval
remain substantially constant**, the effect of viscosity being absorbed by the
thermal loop.

---

# PART D. Claims

> **Format and cost note for the attorney.** Claim 1 is in EPO two part form. For
> the United States recast in single part form, since the two part form can
> operate as an implied admission regarding the preamble, and avoid means plus
> function language under 35 USC 112(f) unless deliberately intended.
>
> **This set is deliberately extensive and should not be filed as is at every
> office.** The PCT charges by page rather than by claim, and an Indian
> provisional need not contain claims at all, so breadth is nearly free at those
> stages and the full set preserves options. **The EPO charges a fee for each
> claim from the 16th, and a substantially higher fee for each from the 51st.**
> The United States basic fee covers 20 claims including 3 independent. Prune to
> approximately 15 for EPO entry and approximately 20 with 3 independent for the
> US, selecting on the basis of the international search report.

## Aspect 1: fill completion interlock

**1.** A manually actuated dispenser for delivering a metered volume of a liquid,
comprising a reservoir (10); a metering chamber (20) having a fixed swept volume,
an inlet (21) in communication with the reservoir and an outlet (22); a metering
piston (23) movable within the metering chamber between a discharge position and a
fill position; a manually operable actuator (30) arranged to drive the metering
piston through a delivery stroke; a return spring (24) arranged to urge the
metering piston through a return stroke so as to draw liquid from the reservoir
into the metering chamber; an inlet valve (25) permitting flow into the metering
chamber during the return stroke and preventing reverse flow during the delivery
stroke; and a discharge valve (26) downstream of the outlet,

**characterised in that** the dispenser further comprises a fill completion
interlock (40) operatively coupled to the metering piston (23) and to the actuator
(30), arranged to adopt a blocking configuration preventing the actuator from
driving the metering piston through a delivery stroke, and to adopt a releasing
configuration only upon the metering piston attaining a predetermined fill position
corresponding to said fixed swept volume,

whereby the volume delivered per delivery stroke is determined by the fixed swept
volume and is substantially independent of the viscosity of the liquid.

**2.** A dispenser according to claim 1, wherein the interlock comprises a latch
member (41) resiliently biased into the blocking configuration and arranged therein
to engage a detent surface (42) associated with the actuator.

**3.** A dispenser according to claim 2, wherein the metering piston carries a
release cam (44) arranged to displace the latch member to the releasing
configuration upon the piston abutting a return stop (43) defining said fill
position.

**4.** A dispenser according to any preceding claim, wherein the interlock permits
a lost motion of the actuator whilst in the blocking configuration.

**5.** A dispenser according to any preceding claim, wherein transition to the
releasing configuration generates a tactile signal, an audible signal, or both.

**6.** A dispenser according to any preceding claim, wherein the inlet valve (25)
has a flow area which increases with the pressure differential across it.

**7.** A dispenser according to claim 6, wherein the inlet valve comprises a poppet
biased against a seat having a profile such that the flow area increases more than
linearly with poppet lift.

**8.** A dispenser according to any preceding claim, further comprising a thermally
responsive element (80) arranged to increase the flow area of the inlet valve as
temperature decreases.

**9.** A dispenser according to claim 8, wherein the thermally responsive element
comprises a bimetallic element or a shape memory alloy element.

**10.** A dispenser according to any preceding claim, wherein the discharge valve
(26) is a pre-compression valve having a predetermined cracking pressure.

**11.** A dispenser according to claim 10, wherein the cracking pressure is between
1.5 and 4 bar, preferably between 2.0 and 3.0 bar.

**12.** A dispenser according to any preceding claim, wherein the fixed swept volume
is between 0.1 and 0.5 ml, preferably between 0.15 and 0.25 ml.

**13.** A dispenser according to any preceding claim, arranged such that the volume
delivered per delivery stroke varies by no more than 15 percent, preferably no more
than 8 percent, across a kinematic viscosity range of 20 to 100 centistokes.

**14.** A dispenser according to any preceding claim, further comprising an intake
conduit (50) having an inlet opening (51) at a standoff distance (52) above a floor
(11) of the reservoir defining a settling volume (53) therebelow.

**15.** A dispenser according to claim 14, wherein the standoff distance is between
5 and 15 mm.

**16.** A dispenser according to claim 14 or 15, further comprising a first filter
element (54) at the inlet opening and a second filter element (55) upstream of a
discharge orifice (27), the second having a smaller aperture than the first.

**17.** A dispenser according to claim 16, wherein the first filter element has an
aperture between 400 and 800 µm and the second between 100 and 200 µm, and wherein
the intake conduit and both filter elements are carried on a common carrier (56)
and are together removable as a unitary cartridge.

**18.** A dispenser according to any preceding claim, wherein the reservoir (10) is
tubular and open at both ends, closed at a first end by a head closure (12) carrying
the metering chamber and at a second end by a removable base closure (13), each
sealing by an axial face seal (14).

## Aspect 2: heating of the metered charge

**19.** A dispenser for delivering a metered volume of a liquid, comprising a
reservoir (10), a metering chamber (20) of fixed swept volume arranged to receive a
charge of liquid from the reservoir, a discharge valve (26) and an actuator (30),

**characterised by** a heating element (100) arranged to heat liquid within the
metering chamber, and a thermal break (105) disposed between the metering chamber
and the reservoir and arranged to impede conduction of heat from the metering
chamber to liquid remaining in the reservoir,

such that a charge may be heated without heating the contents of the reservoir.

**20.** A dispenser according to claim 19, wherein the fixed swept volume is less
than one five hundredth of the capacity of the reservoir.

**21.** A dispenser according to claim 19 or 20, wherein the heating element is
arranged to raise the temperature of a charge by at least 20 K in less than 2
seconds at an electrical input power not exceeding 20 W.

**22.** A dispenser according to any of claims 19 to 21, further comprising an
electrical power input (103), preferably a USB receptacle.

**23.** A dispenser according to claim 22, further comprising an energy store (106)
arranged to permit heating at a power exceeding the instantaneous capability of a
supply connected to the power input.

**24.** A dispenser according to any of claims 19 to 23, further comprising a
controller (102) arranged to limit the temperature of the charge to a predetermined
maximum not exceeding 80 °C, preferably not exceeding 60 °C.

**25.** A dispenser according to any of claims 19 to 24, further comprising a grip
sensor (108), the controller being arranged to energise the heating element upon
the grip sensor indicating that the dispenser has been grasped.

**26.** A dispenser according to any of claims 19 to 25, comprising the fill
completion interlock of any of claims 1 to 5, wherein the heating element is
energised during an interval in which the interlock is in the blocking
configuration.

## Aspect 3: determination of viscosity from return stroke duration

**27.** A dispenser for delivering a metered volume of a liquid, comprising a
metering chamber (20), a metering piston (23), a return spring (24) arranged to
urge the piston through a return stroke drawing liquid into the metering chamber,
and a sensor (104) arranged to detect attainment by the piston of a predetermined
fill position,

**characterised by** a controller (102) arranged to measure a duration between
commencement of the return stroke and attainment of said fill position, and to
determine from that duration a parameter indicative of the viscosity of the liquid
drawn into the metering chamber.

**28.** A dispenser according to claim 27, wherein the sensor (104) is actuated by a
member of a fill completion interlock according to any of claims 1 to 5, whereby the
interlock serves both to prevent premature actuation and to provide said detection.

**29.** A dispenser according to claim 27 or 28, further comprising a temperature
sensor (101), the controller being arranged to determine said parameter from the
measured duration and the measured temperature in combination.

**30.** A dispenser according to any of claims 27 to 29, wherein the controller is
arranged to identify a class of liquid present in the reservoir from said parameter
and a measured temperature, without input from a user.

## Aspect 4: closed loop normalisation of viscosity

**31.** A dispenser according to any of claims 27 to 30, further comprising a
heating element (100) arranged to heat liquid to be drawn into or contained within
the metering chamber, **wherein the controller is arranged to regulate the heating
element in dependence upon said measured duration so as to drive the measured
duration towards a target duration corresponding to a target viscosity**, whereby
liquid presented to the metering chamber is of substantially constant viscosity
irrespective of the liquid supplied and of ambient temperature.

**32.** A dispenser according to claim 31, wherein the controller regulates the
energy delivered to the heating element for a succeeding charge in dependence upon
the duration measured for a preceding charge.

**33.** A dispenser according to claim 31 or 32, wherein the target duration is
selected such that the discharge valve and a discharge orifice receive liquid within
a viscosity range over which a predetermined atomisation quality is maintained.

**34.** A dispenser according to any of claims 31 to 33, wherein both the volume
delivered per delivery stroke and the interval between successive delivery strokes
are substantially constant across a kinematic viscosity range of the supplied liquid
of at least 20 to 100 centistokes.

**35.** A dispenser according to any of claims 31 to 34, wherein the controller is
arranged to store and apply a relationship between temperature and viscosity for
each of a plurality of classes of edible oil.

## Aspect 5: non flowable contents

**36.** A dispenser according to any of claims 27 to 35, wherein the controller is
arranged to determine, from an absence of movement of the metering piston within a
predetermined interval following release of the return spring, that the contents of
the reservoir are not in a flowable state, and in response to energise the heating
element in a melt mode prior to a further attempt to charge the metering chamber.

**37.** A dispenser according to claim 36, wherein in the melt mode the heating
element is arranged to direct heat to an intake path (50) in preference to the bulk
of the reservoir.

**38.** A dispenser according to claim 36 or 37, arranged for use with a fat which is
solid below approximately 24 °C, such as coconut oil, or with clarified butter.

## Aspect 6: obstruction detection

**39.** A dispenser according to any of claims 27 to 38, comprising at least one
filter element (54, 55) in an intake path, wherein the controller is arranged to
compare the measured duration with a duration predicted from a measured temperature
for an unobstructed intake path, and to generate an obstruction indication where the
measured duration exceeds the predicted duration by more than a predetermined
threshold.

**40.** A dispenser according to claim 39, wherein the obstruction indication is
generated before a degradation of spray quality perceptible to a user has occurred.

**41.** A dispenser according to claim 39 or 40, wherein the controller distinguishes
an increase in duration attributable to viscosity from an increase attributable to
obstruction by reference to the measured temperature.

## Further apparatus features

**42.** A dispenser according to any preceding claim, further comprising a counter
(60) arranged to register delivery strokes and to indicate a quantity of liquid
remaining.

**43.** A dispenser according to claim 42, wherein the counter is arranged to
indicate an energy content of the liquid dispensed, derived from the number of
delivery strokes, the fixed swept volume and a stored energy density.

**44.** A dispenser according to any preceding claim, further comprising a vent (70)
comprising a hydrophobic membrane.

**45.** A dispenser according to any preceding claim, wherein the liquid is an edible
oil.

**46.** A dispenser according to any preceding claim, wherein the reservoir, the
metering chamber, an intake cartridge, a nozzle, a base closure and a grip member are
each separable from one another without tools and without breaking an adhesive, weld
or rivet.

## Methods

**47.** A method of delivering metered volumes of a liquid of unknown viscosity from a
manually actuated dispenser having a metering chamber of fixed swept volume and a
metering piston, comprising: (a) urging the metering piston through a return stroke
under a return spring so as to draw liquid into the metering chamber; (b) blocking a
manually operable actuator so as to prevent a delivery stroke whilst the piston is
between a discharge position and a predetermined fill position corresponding to said
fixed swept volume; (c) releasing the actuator upon the piston attaining said fill
position; and (d) executing a delivery stroke to expel said fixed swept volume,
whereby the volume delivered is substantially independent of the viscosity of the
liquid.

**48.** A method of determining a parameter indicative of the viscosity of a liquid in
a dispenser, comprising urging a metering piston through a return stroke under a
return spring of known force so as to draw the liquid into a metering chamber of
known geometry, measuring the duration between commencement of the return stroke and
attainment by the piston of a predetermined fill position, and determining said
parameter from that duration.

**49.** A method according to claim 48, further comprising measuring a temperature of
the liquid and determining said parameter from the duration and the temperature in
combination.

**50.** A method of dispensing metered volumes of a liquid, comprising performing the
method of claim 48, comparing the determined duration with a target duration
corresponding to a target viscosity, and heating a charge of the liquid within the
metering chamber by an amount selected to drive a subsequently measured duration
towards the target duration, **whereby successive charges are presented to a
discharge orifice at substantially constant viscosity**.

**51.** A method according to claim 50, wherein the heating is performed during an
interval in which a fill completion interlock prevents actuation.

**52.** A method according to claim 50 or 51, wherein the charge heated is less than
one five hundredth of the liquid held in a reservoir of the dispenser, and wherein
liquid remaining in the reservoir is not substantially heated.

**53.** A method of detecting obstruction of a filter element in a dispenser,
comprising measuring a duration of a return stroke as in claim 48, measuring a
temperature of the liquid, predicting a duration for an unobstructed intake path at
said temperature, and generating an obstruction indication where the measured
duration exceeds the predicted duration by more than a threshold.

**54.** A method of dispensing a fat which is solid at ambient temperature, comprising
releasing a return spring of a metering piston, determining from an absence of
movement of the piston that the fat is not in a flowable state, energising a heating
element in a melt mode, and thereafter charging a metering chamber and executing a
delivery stroke.

## Aspect 7: manual viscosity calibration collar

> **Renumber these immediately after claim 18.** They are placed here only to
> avoid renumbering the draft. This is now the **preferred embodiment**, and claim
> 55 should be presented as the second independent apparatus claim.

**55.** A manually actuated dispenser for delivering a metered volume of a liquid,
comprising a reservoir (10), a metering chamber (20) of fixed swept volume, a
metering piston (23), a manually operable actuator (30), a return spring (24), an
inlet valve (25), a discharge valve (26) and an intake path by which liquid is
drawn from the reservoir into the metering chamber,

**characterised by** a user settable calibration member (90) movable between a
plurality of discrete positions, each position establishing a different flow
resistance in said intake path, **the swept volume of the metering chamber being
the same in each of said positions**,

whereby the interval required to charge the metering chamber may be brought within
a predetermined range for liquids of differing viscosity without altering the
volume delivered per delivery stroke.

**56.** A dispenser according to claim 55, wherein the calibration member is a
collar rotatably mounted upon a head assembly of the dispenser.

**57.** A dispenser according to claim 56, wherein the collar carries an arcuate
port of progressively varying width arranged to register with an inlet passage,
such that rotation of the collar varies the effective flow area of the inlet
passage.

**58.** A dispenser according to claim 56 or 57, wherein the collar additionally
serves as a closure securing the head assembly to the reservoir, such that no
component is added to the dispenser by the provision of the calibration member.

**59.** A dispenser according to any of claims 55 to 58, further comprising detents
defining said discrete positions, and indicia associated with each position
identifying a class of edible oil, a season, an ambient temperature range, or a
combination thereof.

**60.** A dispenser according to any of claims 55 to 59, wherein the ratio of the
largest to the smallest effective flow area established by the calibration member
is at least 1.5, preferably at least 1.7, corresponding to a viscosity range of at
least a factor of three.

**61.** A dispenser according to any of claims 55 to 60, wherein movement of the
calibration member alters neither the stroke of the metering piston, nor the force
of the return spring, nor the swept volume of the metering chamber.

**62.** A dispenser according to any of claims 55 to 61, further comprising a
thermally responsive element (80) arranged to bias the effective flow area with
ambient temperature, such that the calibration member addresses the class of
liquid and the thermally responsive element addresses ambient temperature.

**63.** A dispenser according to any of claims 55 to 62, further comprising a fill
completion interlock (40) according to any of claims 1 to 5, **arranged such that a
setting of the calibration member corresponding to a liquid less viscous than that
present causes the interlock to impose a delay perceptible to the user, and a
correct setting causes no perceptible delay**, whereby the interlock constitutes
the sole indication to the user of a correct setting of the calibration member.

**64.** A dispenser according to any of claims 55 to 63, wherein the calibration
member additionally alters a preload of the return spring (24).

**65.** A method of calibrating a manually actuated dispenser to a liquid of unknown
viscosity, comprising: actuating the dispenser; observing whether a fill completion
interlock imposes a perceptible delay before a subsequent delivery stroke may be
executed; and, where such a delay is observed, advancing a calibration member to a
position establishing a lower flow resistance in an intake path, and repeating until
no perceptible delay is observed, **the volume delivered per delivery stroke being
unaltered throughout.**

**66.** A method according to claim 65, wherein the calibration is performed without
any indication to the user other than the presence or absence of said delay.

## Abstract

A manually actuated dispenser delivers a metered volume of liquid substantially
independently of viscosity. A metering chamber (20) is charged during a return
stroke of a piston (23) urged by a spring (24). Because the piston advances only as
rapidly as liquid enters behind it, its position measures the state of charge, and
the duration of the return stroke measures the viscosity. A fill completion
interlock (40) blocks the actuator (30) until the piston reaches a fill stop (43),
so delivered volume is set by chamber geometry alone. In powered embodiments a
heating element (100) heats only the charge within the metering chamber, isolated by
a thermal break (105) from the reservoir, requiring approximately one thousandth of
the energy needed to heat the reservoir. A user settable
calibration collar (90) varies the flow resistance of the intake path, but not the
swept volume, so that the charging interval is brought within range for oils of
differing viscosity without altering the delivered volume; because a mis-set collar
causes the interlock to impose a perceptible pause and a correct setting causes
none, the interlock itself teaches the user the correct setting. In powered
embodiments a heating element (100) heats only the charge within the metering
chamber, and a controller (102) regulates it against the measured return stroke
duration. (Figures 2, 9 and 11)

---

# PART E. Filing strategy

## E1. Sequence, which Section 39 dictates

| When | Action | Why |
|---|---|---|
| **Day 0** | **File Indian provisional** covering all six aspects | Priority date. Starts the Section 39 six week clock and the twelve month Paris clock. A provisional needs no claims, so file the full description |
| Day 0 | Preserve evidence of the site's first public date | It will be asked for, and the evidence decays |
| **Week 6** | Free to file abroad | Section 39 satisfied by the six week route |
| Months 1 to 9 | Professional novelty search; build the bench rig | Evidence for the complete specification, and a reduction to practice |
| **By month 12** | **File PCT** claiming Indian priority, and the Indian complete specification | One application preserving most of the world |
| Month 16 | International Search Report and Written Opinion | The first real read. Decide what to prune |
| **Month 30 or 31** | **EPO and USPTO national phase** | The expensive step, deferred as long as possible |

## E2. What to file where, given the disclosure problem

- **India and EPO.** Lead with the clean subject matter: the interlock, the
  viscometry, the charge heating, the closed loop, melt mode and obstruction
  detection. Treat the raised intake, the two stage filtration ratings, the
  cracking pressure and the dual opening body as **dependent claims only**,
  expecting them to be cut.
- **United States.** The twelve month grace period may still protect the published
  material if filed in time. Ask the attorney whether a broader US claim set is
  worth pursuing on that basis, and establish the first public date before relying
  on it.

## E3. Unity of invention, which will be raised

PCT Rule 13 requires a single general inventive concept. Six aspects invites an
objection and a demand for additional search fees.

**The unifying special technical feature to argue is this:** *using the motion of
the metering piston during the return stroke as a measure of the state of charge
and of the viscosity of the liquid, and employing that measure to render the
delivered volume independent of viscosity.* Aspects 1, 3, 4, 5 and 6 all rest on
it directly.

**Aspect 2, charge only heating with a thermal break, is the most likely to be
severed**, because it can be practised without measuring anything. Be ready to
divide it out. That is not a loss: a divisional keeps the priority date, and
charge only heating is independently valuable and independently licensable.

## E4. Indicative costs

Ranges only. Confirm with the firm before committing.

| Step | Government fee | Professional fee |
|---|---|---|
| Indian provisional, natural person or startup, e-filed | approx ₹1,600 | ₹20,000 to ₹45,000 |
| Indian complete specification | approx ₹1,600 | ₹40,000 to ₹90,000 |
| Indian request for examination | approx ₹4,000 | included |
| PCT with international search | approx ₹1.5 to 2.5 lakh | ₹40,000 to ₹80,000 |
| EPO regional phase | €4,000 to €8,000 plus claim fees | varies |
| EPO claim fees | fee per claim from the 16th, higher from the 51st | prune before entry |
| US national phase, small or micro entity | $1,000 to $2,000 | $6,000 to $12,000 |
| Each divisional | roughly a further national phase | budget for at least one |

Claim startup status with the Indian Patent Office where eligible; the reduction is
substantial.

## E5. Search instructions

Commission the search after the provisional, not before; the provisional is cheap
enough to file first. Direct the searcher to:

- metering pumps with actuation lockout dependent on chamber charge state
- inhaler and injection pen dose interlocks, the most likely citations
- **heated dispensers** for chocolate, wax, adhesive, cosmetics and infant formula,
  specifically whether any heats a metered charge in isolation from a reservoir
- **inference of fluid viscosity from pump stroke timing**, including in industrial
  metering and in inkjet
- filter obstruction detection by flow or timing anomaly
- **adjustable flow restriction in hand pump dispensers**, multi position inlet
  selectors, and any dispenser bearing user indicia naming a liquid or a season
- adjustable dose pumps, to establish that the art varies dose rather than
  preserving it
- IPC and CPC: B05B 11/00, B05B 11/10, B67D 3/00, B67D 1/08, G01F 11/02,
  G01N 11/04, A47J 43/00, H05B 1/02

## E6. What the electronics change, beyond patents

Adding a heater, controller and USB input moves the product into a different
regulatory class, and this should be costed before committing:

- **Electrical safety**: IEC 60335-1 and the relevant part 2, for household
  appliances.
- **India**: the BIS Compulsory Registration Scheme may apply to the electronics.
  Check whether the product falls within a notified category.
- **Cells**: IEC 62133 if an energy store using a cell is fitted. A supercapacitor
  avoids much of this and is worth considering for that reason alone.
- **EU and US**: CE and UKCA marking, FCC Part 15 for the US.
- **Food contact**: unchanged, and now additionally the heating element must not
  contact the oil directly unless its wetted surface is itself compliant.

**It also conflicts with the ten year repairability commitment**, since a
controller is not a repairable module in the sense the rest of the product is. The
cleanest resolution is that the powered version is a **separate model**, with the
unpowered six module product remaining the repairable one, and the shared published
interface allowing a powered head to be fitted to the same body. The interface
specification already contemplates exactly that.

## E7. Also file separately

**Design registration** under the Designs Act 2000 on the final form. ₹1,000
government fee for a startup or small entity with Form 24, plus ₹5,000 to ₹8,000
professional, ten years extendable by five. This is the right instrument for the
six module architecture and the dual opening body, which are weak as patent subject
matter but strong as appearance. **File after the patent provisional, and note that
prior publication can destroy design novelty too.**

**Trade mark** ENNA in class 21, with classes 8 and 11 as relevant.

---

# PART F. What this document is not

I am not a patent attorney, this is not legal advice, and nothing here has been
professionally searched.

1. **No professional novelty search has been conducted.** The prior art in Part B
   was found by ordinary web searching. A proper search will find art I have not
   seen, and may find something reading directly on claim 1.
2. **The claims need professional revision.** Claim scope is the whole value of a
   patent, and the set above is a starting point, not a filing text. It is also
   deliberately over inclusive, per the note in Part D.
3. **None of the ten figures has been drawn.** They must be prepared to each
   office's formal drawing standards.
4. **The thermal figures are calculated, not measured.** 9.2 J for a 0.20 ml charge
   at 25 K rise assumes 2.0 J/g/K and 0.92 g/ml. Confirm against the actual oils
   before the complete specification, and measure on the bench rig.
5. **Nothing has been reduced to practice.** No interlock has been built, no loop
   has been closed, no viscosity has been inferred from a real return stroke. The
   specification must be enabling on paper, and the bench rig should exist before
   the complete specification is filed.
6. **A registered Indian patent agent is required** to prosecute in India.
7. **The Section 39 and disclosure questions require a lawyer's opinion on your
   actual facts**, especially the site's first public date.

## The order of the next three things

1. **Establish and evidence the date the site first became publicly reachable.**
   The password protection stops the bleeding but does not heal the wound, and the
   evidence decays.
2. **File the Indian provisional**, with the full description of all six aspects.
   It is cheap, it can be done in days, and it starts every clock you need.
3. **Build the bench rig, which is now much smaller than it was.** A spring, a
   piston, a chamber, a latch and a variable inlet orifice. Measure charging time
   against oil and temperature, and confirm that opening the aperture by about a
   third restores the charging interval across a threefold viscosity range. **If
   it does, the collar and the interlock are the whole product** and nothing needs
   a power supply. Add a timer and a thermistor to the same rig only afterwards,
   to check whether the powered aspects are worth holding.
