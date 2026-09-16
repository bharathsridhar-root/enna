# Enna: Patentability Assessment and Draft Patent Specification

**Prepared 16 September 2026. Draft for instructing a patent attorney. Not legal advice.**

I am not a patent attorney and this is not a filing. What follows is a
technically detailed draft and a reasoned patentability assessment, written so
that a registered agent can take it, run a proper search, and file. Claim
language in particular must be reviewed by a professional before filing, because
claim scope is where value is won and lost.

---

# PART A. Two things that need a decision this week

## A1. Section 39: you may not file abroad first

If any inventor is resident in India, **Section 39 of the Patents Act 1970**
prohibits filing a patent application outside India unless one of these is true:

1. An application for the same invention was filed **in India at least six weeks
   earlier**, and no secrecy direction under Section 35(1) is in force; or
2. Written permission has been obtained from the Controller, by filing
   **Form 25**. Under Rule 71, the Controller ordinarily disposes of the request
   within 21 days.

**The penalty is not administrative.** Section 118 provides imprisonment up to
two years, or a fine, or both. Beyond that, the corresponding Indian application
can be deemed abandoned and a granted Indian patent can be revoked.

**Consequence for us:** the first filing must be the Indian one. This is not a
preference, it is a legal constraint, and it happens to also be the cheapest and
most sensible sequence anyway.

## A2. Your own website may already have destroyed novelty in Europe and India

This is the urgent one.

| Jurisdiction | Grace period for the inventor's own disclosure |
|---|---|
| **United States** | **12 months.** A disclosure by the inventor does not count as prior art if the application is filed within one year |
| **European Patent Office** | **Effectively none.** Absolute novelty. Six months only for disclosure obtained through abuse, or display at an official international exhibition |
| **India** | **Effectively none for this case.** The one year grace applies to a reading before a learned society or publication in its transactions, not a commercial website |

I audited what the Enna site currently discloses. If the Amplify deployment is
publicly reachable, then the following are already published:

- the **9 mm raised intake standoff** and the sediment settling principle
- the **600 µm intake and 150 µm pre-nozzle two stage filtration**
- the **pre-compression valve with a 2.4 bar cracking pressure**
- the **body open at both ends** and the axial face seal closures
- the **0.20 ml metered dose** and the stroke counter
- the **bayonet nozzle** and the six module architecture

For the EPO and India, those features are therefore at serious risk of being
unpatentable, because they were disclosed before filing. For the US they are
still recoverable if you file within twelve months of first publication.

**The good news, and it is substantial.** I searched the site and the repository
for the invention you actually want to claim, which is viscosity compensated
constant volume metering. **It appears nowhere.** No mention of a fill completion
interlock, a differential inlet, thermal compensation or constant volume. That
subject matter is completely clean in every jurisdiction.

### What to do, in order

1. **Establish the facts.** Find the exact date the Amplify site first became
   publicly reachable, and whether search engines indexed it. If it was never
   public, or only shared privately, the position is far better. Record this in
   writing now, because you will be asked.
2. **Put the site behind a password today** if it is live, until the provisional
   is on file. Amplify supports access control on a branch. This does not undo a
   past disclosure but it stops further accrual and stops third parties
   republishing.
3. **File the Indian provisional as fast as possible**, covering the metering
   invention in full and the intake and filtration and body architecture as
   fallback subject matter. A provisional can be filed within days.
4. **Ask the attorney specifically** whether the published material can still be
   claimed in India on the basis that publication was by the applicant and
   whether any Section 31 exception applies. Do not assume either way.

---

# PART B. Patentability assessment

## B1. The three candidate inventions, ranked

| # | Candidate | Novelty | Inventive step | Disclosed already | Verdict |
|---|---|---|---|---|---|
| **I** | **Viscosity independent constant volume metering by fill completion interlock** | Strong | Strong | **No** | **File this. It is the invention.** |
| II | Anti sediment raised intake with two stage serviceable filtration | Moderate | Moderate | **Yes** | File as fallback, expect EPO and India difficulty |
| III | Body open at both ends with axial face seals, six module architecture | Weak as a patent | Weak | **Yes** | **Design registration, not a patent** |

## B2. Invention I: the technical problem, stated properly

A hand actuated positive displacement pump should deliver a volume per stroke
equal to the swept volume of its metering chamber. It does, **provided the
chamber completely refills between strokes.**

Refill is driven by the return spring creating a sub atmospheric pressure in the
chamber, drawing liquid through the dip tube and inlet valve. That flow is
governed approximately by the Hagen-Poiseuille relation:

```
Q  ≈  π · ΔP · r⁴  /  (8 · μ · L)
```

so refill time is **directly proportional to dynamic viscosity μ**.

Edible oils vary far more than is generally appreciated. Kinematic viscosity
roughly doubles for each 20 °C fall in temperature, and different oils differ
again at the same temperature. A device tuned for sunflower oil at 30 °C in
Chennai may see three times the viscosity with a cold pressed oil at 12 °C in
Delhi in January.

**The failure is invisible.** The user squeezes at their habitual cadence, of
roughly one stroke per second. With a thin oil the chamber fully refills and
delivers the nominal 0.20 ml. With a cold or thick oil the chamber is only
partly refilled when the next delivery stroke begins, and the device may deliver
0.12 ml. The action feels identical. The user has no way to know.

For an ordinary sprayer that is a minor annoyance. **For a product whose entire
proposition is portion control and a stated calorie per stroke, it is fatal**,
because the number printed on the device is simply wrong for half the year.

## B3. Why the known art does not solve it

I identified the closest art in four groups. Each must be distinguished in the
background section, and a professional search will find more.

**Group 1: pre-compression and discharge pressure regulation.**
US5467900, US5730335, and the AFA Flairosol family US8905271B2, US9714133 and
EP2566629B1. These regulate **the pressure at which the chamber empties.**

> **The distinction that matters, and it should be stated explicitly in the
> specification:** a pre-compression valve controls how the chamber discharges.
> It does nothing whatsoever about whether the chamber was full when discharge
> began. A device can have a perfect pre-compression valve and still deliver a
> wrong dose, because the error was created during the *return* stroke, before
> the valve is involved at all.

**Group 2: nozzle improvements for viscous fluids.**
US6659369B1, "high viscosity liquid sprayer nozzle assembly", which expressly
addresses trigger sprayers and cooking oil, and WO2016077114A1, "spray nozzle for
high viscosity (e.g. oil) spray applications". These improve **atomisation
quality**, not dose volume. A better spray of the wrong quantity is still the
wrong quantity.

**Group 3: powered and programmable metering pumps.**
US5022556A programmable volume dispensing with a positive displacement metering
pump for high viscosity fluids; DE102012100306A1, expressly a method for adapting
a metering pump to the viscosity of the medium, which notes that viscous media
need longer intake and delivery times; US4518105 for dispensing viscous
concentrates of variable viscosity in metered quantities. **These require power,
control electronics or operator configuration.** None is applicable to an
unpowered hand held domestic device, and that limitation is the inventive gap.

**Group 4: metered dose pumps for semi solids.**
US6889875 taper well meter dose pump. Different problem, different regime.

**Conclusion.** The art either regulates discharge pressure, or improves
atomisation, or achieves viscosity tolerance using power and control systems.
**I did not find art that makes dose volume viscosity independent in an unpowered
hand actuated dispenser by mechanically guaranteeing complete refill before
permitting delivery.** That is the inventive concept.

## B4. The inventive concept, in one sentence

> Instead of trying to make a viscous liquid refill a chamber faster, **prevent
> the device from firing until the chamber is actually full**, so that the error
> is moved off the axis the user cannot perceive, which is volume, and onto the
> axis they can, which is a fraction of a second of delay.

Three cooperating features, all passive and unpowered:

**(A) Fill completion interlock. This is the core.** A mechanical interlock is
coupled to the metering piston and to the actuator. It holds the actuator blocked
and releases only when the piston reaches a predetermined full fill position. The
user simply cannot execute a delivery stroke on a partly filled chamber.

**(B) Differential pressure responsive inlet valve.** The inlet poppet's lift
increases with the pressure differential across it. A more viscous fluid produces
a greater differential at a given flow, so it automatically opens a larger inlet
aperture and refills faster. Passive self compensation, no sensing.

**(C) Thermally responsive inlet element.** Viscosity is dominated by
temperature. A bimetallic or shape memory element increases inlet flow area as
temperature falls, pre empting the seasonal case.

**(D) Fill completion signal.** Release of the interlock produces a tactile and
audible detent, so the user receives positive confirmation that the dose about to
be delivered is a full one.

## B5. Honest weaknesses to raise with the attorney

1. **Interlocks are old.** Mechanical interlocks preventing actuation until a
   condition is met exist in many fields, including inhalers and injection pens.
   The inventive step argument must rest on the *combination and purpose*, which
   is using a fill completion interlock specifically to render dispensed volume
   independent of fluid viscosity in an unpowered dispenser. Expect an examiner
   to cite an inhaler dose interlock. The answer is that those interlocks meter a
   pre loaded solid or a fixed gas charge and address dose counting or lockout
   after exhaustion, not the refill dynamics of a viscous liquid.
2. **Obviousness attack.** An examiner may argue it is obvious to wait for the
   chamber to fill. The response is that the art consistently solves viscosity by
   adding power and control, per DE102012100306A1, which is evidence that the
   simple mechanical route was not obvious to those skilled in the art.
3. **Claim 1 must not be limited to edible oil.** Claim the fluid class broadly
   and make edible oil a dependent claim, otherwise you give away every adjacent
   application.
4. **Enablement.** The specification must describe at least one interlock
   geometry in enough detail to be built. The draft below does.

---

# PART C. Draft patent specification

## Title

**A manually actuated dispenser for delivering metered volumes of liquid
substantially independently of liquid viscosity**

A plainer alternative for the Indian filing: *Dispenser with viscosity
independent volumetric metering.*

## Technical field

The invention relates to manually actuated dispensers for liquids, and in
particular to hand operated pump dispensers which deliver a metered volume of a
liquid of variable and unknown viscosity, such as an edible oil, per actuation.

## Background

Manually actuated pump dispensers of the trigger or piston type are widely used
to dispense liquids. In a positive displacement dispenser of this class, liquid
is drawn from a reservoir into a metering chamber during a return stroke of a
piston, and expelled through a discharge orifice during a delivery stroke. The
nominal volume delivered per actuation is the swept volume of the metering
chamber.

That nominal volume is achieved only if the metering chamber is completely
refilled between successive delivery strokes. Refilling occurs because the
returning piston creates a pressure below atmospheric within the chamber, drawing
liquid through an intake conduit and an inlet valve. The rate of that flow is
approximately inversely proportional to the dynamic viscosity of the liquid,
according to the Hagen-Poiseuille relation, so that the time required to refill
the chamber increases in approximately direct proportion to viscosity.

Edible oils exhibit a wide range of viscosity. Kinematic viscosity approximately
doubles for each 20 °C reduction in temperature, and different oils differ
substantially at a common temperature. A dispenser used with a low viscosity oil
at 30 °C may encounter three times that viscosity when used with a cold pressed
oil at 12 °C.

A user actuates such a dispenser at a habitual cadence, typically of the order of
one actuation per second, and does not vary that cadence according to the liquid.
Where the refill time exceeds the interval between actuations, the metering
chamber is only partially charged when the next delivery stroke commences, and
the volume delivered is correspondingly reduced. Critically, **the actuation feels
identical to the user**, and there is no indication that a reduced volume has been
delivered. The dispensed volume may fall by forty percent or more without the
user's knowledge.

Where the dispenser is used for portion control, or where a stated volume or
energy content per actuation is relied upon, this variation defeats the purpose
of the device.

Several approaches are known. Pre-compression discharge valves, such as those
disclosed in US 5,467,900, US 5,730,335, US 8,905,271 and EP 2,566,629, establish
a minimum pressure below which the chamber does not discharge, thereby improving
atomisation consistency. **Such valves regulate the conditions under which the
metering chamber empties, and have no effect upon whether the metering chamber
was fully charged before emptying commenced.** The volumetric error arises during
the return stroke, before the discharge valve participates at all.

Nozzle assemblies adapted to viscous liquids are disclosed in US 6,659,369 and
WO 2016/077114. These improve the quality of atomisation of a viscous liquid but
do not address the volume delivered.

Viscosity tolerant metering is known in powered apparatus. US 5,022,556 discloses
a programmable volume dispensing apparatus using a positive displacement metering
pump for high viscosity fluids. DE 10 2012 100 306 discloses a method for adapting
a metering pump to the viscosity of the medium to be metered, and expressly
recognises that highly viscous media require longer intake and delivery times.
US 4,518,105 discloses dispensing viscous concentrates of variable viscosity in
metered quantities. **Each of these requires a power source, control apparatus, or
operator configuration, and none is applicable to an unpowered hand held
dispenser intended for domestic use.**

There remains a need for a manually actuated, unpowered dispenser which delivers a
consistent metered volume of liquid irrespective of the viscosity of that liquid.

## Summary of the invention

According to a first aspect there is provided a manually actuated dispenser
comprising a reservoir, a metering chamber of fixed swept volume, a metering
piston, a manually operable actuator arranged to drive the piston through a
delivery stroke, a return spring arranged to drive the piston through a return
stroke so as to draw liquid into the metering chamber, an inlet valve and a
discharge valve, **characterised by a fill completion interlock operatively
coupled between the metering piston and the actuator, the interlock being
arranged to prevent the actuator from executing a delivery stroke until the
metering piston has attained a predetermined fill position corresponding to the
fixed swept volume.**

The invention proceeds from the recognition that **the position of the metering
piston during the return stroke is itself a direct measure of the state of charge
of the metering chamber.** The returning piston can advance only as rapidly as
liquid enters the chamber behind it. The piston therefore reaches its return stop
if and only if the chamber has been completely charged, whatever the viscosity of
the liquid. Interlocking the actuator to that position converts a volumetric
error, which the user cannot perceive, into a short delay, which the user can.

The consequence is that the delivered volume is determined solely by the geometry
of the metering chamber and is substantially independent of liquid viscosity,
without any power source, sensor or control system.

Preferably the dispenser further comprises an inlet valve having a flow area
which increases with the pressure differential across the valve, so that a more
viscous liquid, which generates a greater differential at a given flow rate,
automatically opens a larger inlet aperture and refills the chamber more rapidly.
This shortens the delay which the interlock would otherwise impose.

Preferably the dispenser further comprises a thermally responsive element
arranged to increase the inlet flow area as temperature decreases, since the
viscosity of edible oils is dominated by temperature.

Preferably release of the interlock produces a tactile or audible signal, so that
the user receives positive confirmation that a complete dose is available.

According to a second aspect there is provided a method of dispensing metered
volumes of a liquid of unknown viscosity, comprising drawing liquid into a
metering chamber under the action of a return spring, **blocking a delivery stroke
until the metering piston has attained a predetermined fill position**, and
thereafter permitting the delivery stroke.

## Brief description of the drawings

- **Figure 1** is a sectional elevation of a dispenser according to the invention.
- **Figure 2** is an enlarged section of the metering chamber and fill completion interlock, with the interlock in the blocking configuration and the chamber partially charged.
- **Figure 3** is the view of Figure 2 with the chamber fully charged and the interlock in the releasing configuration.
- **Figure 4** is an enlarged section of the differential pressure responsive inlet valve, showing the progressive seat profile.
- **Figure 5** is a section of the removable intake cartridge, showing the raised inlet opening, the first filter element and the second filter element.
- **Figure 6** is an exploded view showing the separable modules.
- **Figure 7** is a graph of delivered volume against liquid viscosity, for a dispenser according to the invention and for a conventional dispenser.

## Detailed description

### Overall arrangement, Figure 1

A dispenser comprises a tubular reservoir (10) having a floor (11), closed at a
first end by a head closure (12) and at a second end by a base closure (13), each
sealed by an axial face seal (14) compressed by a multi start thread. Because both
closures are removable, the reservoir (10) may be opened at both ends for
cleaning.

Within the head closure (12) is a metering chamber (20) of fixed swept volume,
having an inlet (21) and an outlet (22), and containing a metering piston (23)
slidable between a discharge position and a fill position. A return spring (24)
urges the piston (23) towards the fill position. An inlet valve (25) admits liquid
to the chamber (20) during the return stroke and closes during the delivery
stroke. A discharge valve (26), preferably a pre-compression valve having a
predetermined cracking pressure of between 1.5 and 4 bar, and in one embodiment
2.4 bar, communicates with a discharge orifice (27).

A manually operable actuator (30) in the form of a trigger is pivoted at (31) and
carries a drive member (32) arranged to bear upon a piston rod (33) extending
from the piston (23).

Liquid is drawn from the reservoir (10) through an intake conduit (50).

In one embodiment the swept volume of the metering chamber (20) is between 0.1
and 0.5 ml, and in a particular embodiment 0.20 ml, corresponding to
approximately 0.18 g and approximately 1.7 kilocalories of a typical edible oil.

### The fill completion interlock, Figures 2 and 3

A latch member (41) is pivotally mounted within the head closure (12) and is
resiliently biased into a blocking configuration, shown in Figure 2, in which a
nose of the latch member (41) lies within the path of travel of the drive member
(32) and engages a detent surface (42) thereon. In that configuration the trigger
(30) cannot advance the piston (23), and no delivery stroke can occur.

The piston rod (33) carries a release cam (44). As the return spring (24) drives
the piston (23) towards the fill position, liquid is drawn into the chamber (20)
through the inlet valve (25). **The piston can advance only as rapidly as liquid
enters behind it.** The rate of advance is therefore governed by the viscosity of
the liquid, but the final position of the piston is not.

When, and only when, the piston (23) abuts a return stop (43) defining the fill
position, the release cam (44) displaces the latch member (41) out of the path of
the drive member (32), as shown in Figure 3. The trigger (30) is then free to
execute a delivery stroke, and the volume expelled is the full swept volume of
the chamber (20).

In a preferred arrangement the latch member (41) and the detent surface (42) are
profiled such that a small lost motion of the trigger (30) is permitted in the
blocking configuration. The user therefore perceives a short positive resistance
rather than a rigid obstruction, and release of the latch produces a tactile and
audible detent which signals that a complete dose is available.

With a low viscosity liquid the chamber charges within a small fraction of a
second and the interlock is released before the user can return the trigger, so
the interlock is imperceptible. With a high viscosity or cold liquid the interlock
imposes a delay of the order of a second. **In neither case does the delivered
volume change.**

### Differential pressure responsive inlet valve, Figure 4

The inlet valve (25) comprises a poppet resiliently biased against a seat, the
seat having a progressive profile such that the annular flow area between poppet
and seat increases more than linearly with poppet lift.

The lift of the poppet is a function of the pressure differential across the
valve. For a given volumetric flow rate, a liquid of higher viscosity generates a
greater pressure differential, and therefore lifts the poppet further and opens a
larger flow area. The valve thus compensates passively, in the correct direction,
without sensing, power or adjustment.

The seat profile is selected such that, over a design viscosity window of
approximately 20 to 100 centistokes at 25 °C, the variation in refill time is
substantially reduced relative to a valve of fixed flow area.

### Thermally responsive element

A thermally responsive element (80), for example a bimetallic washer or a shape
memory alloy element, is disposed in the inlet path and arranged to reduce the
resilient bias upon the poppet, or to increase its rest lift, as temperature
falls. Because the viscosity of edible oils is dominated by temperature, this
anticipates the increase in viscosity rather than merely responding to it.

### Intake and filtration, Figure 5

The intake conduit (50) terminates in an inlet opening (51) held at a standoff
(52) of between 5 and 15 mm, and in one embodiment 9 mm, above the floor (11) of
the reservoir (10), defining beneath it a settling volume (53) into which
particulate matter descends and from which it is not drawn.

A first filter element (54) having an aperture of between 400 and 800 µm, and in
one embodiment 600 µm, is disposed at the inlet opening (51). A second filter
element (55) having a smaller aperture, of between 100 and 200 µm and in one
embodiment 150 µm, is disposed upstream of the discharge orifice (27).

In a preferred arrangement the intake conduit (50), the first filter element (54)
and the second filter element (55) are carried upon a common carrier (56) and are
removable from the reservoir (10) as a single cartridge, so that all three stages
of filtration are cleaned or replaced together.

### Further features

A stroke counter (60) is coupled to the actuator (30) and advances by one
increment per delivery stroke. Because each delivery stroke delivers a known
volume, the counter indicates both the volume remaining and, for an edible oil of
known energy density, the energy content dispensed. In one arrangement the
counter (60) is a separable module attached to the head closure (12).

A vent (70) comprising a hydrophobic membrane admits air to the reservoir (10) as
liquid is withdrawn while excluding moisture and airborne particulate.

An internal fill line is formed on the inner wall of the reservoir (10), visible
through the opened head closure (12), indicating the maximum charge.

### Performance, Figure 7

Figure 7 plots delivered volume against liquid viscosity at a fixed actuation
cadence. For a conventional dispenser the delivered volume falls progressively as
viscosity rises above the value for which the dispenser was designed. For a
dispenser according to the invention the delivered volume remains substantially
constant across the whole design window, the effect of viscosity appearing
instead as an increase in the minimum interval between actuations.

## Claims

> **Format note for the attorney.** Claim 1 is given in the EPO two part form
> with a characterising portion. For the United States the two part form is not
> required and can operate as an implied admission regarding the preamble, so the
> US claim set should be recast in single part form. The usual practice is to
> file the priority and PCT application in a form acceptable to the EPO and
> amend on entry to the US national phase. Avoid means plus function language
> under 35 USC 112(f) unless deliberately intended.

**1.** A manually actuated dispenser for delivering a metered volume of a liquid,
comprising a reservoir (10); a metering chamber (20) having a fixed swept volume,
an inlet (21) in communication with the reservoir and an outlet (22); a metering
piston (23) movable within the metering chamber between a discharge position and
a fill position; a manually operable actuator (30) arranged to drive the metering
piston through a delivery stroke from the fill position towards the discharge
position; a return spring (24) arranged to urge the metering piston through a
return stroke from the discharge position towards the fill position so as to draw
liquid from the reservoir into the metering chamber; an inlet valve (25)
permitting flow into the metering chamber during the return stroke and preventing
reverse flow during the delivery stroke; and a discharge valve (26) downstream of
the outlet,

**characterised in that** the dispenser further comprises a fill completion
interlock (40) operatively coupled to the metering piston (23) and to the actuator
(30), the interlock being arranged to adopt a blocking configuration in which it
prevents the actuator from driving the metering piston through a delivery stroke,
and to adopt a releasing configuration only upon the metering piston attaining a
predetermined fill position corresponding to said fixed swept volume,

whereby the volume of liquid delivered per delivery stroke is determined by the
fixed swept volume of the metering chamber and is substantially independent of the
viscosity of the liquid.

**2.** A dispenser according to claim 1, wherein the fill completion interlock
comprises a latch member (41) resiliently biased into the blocking configuration
and arranged, in that configuration, to engage a detent surface (42) associated
with the actuator (30).

**3.** A dispenser according to claim 2, wherein the metering piston (23) carries
a release cam (44) arranged to displace the latch member (41) to the releasing
configuration upon the metering piston abutting a return stop (43) defining said
predetermined fill position.

**4.** A dispenser according to any preceding claim, wherein the fill completion
interlock permits a lost motion of the actuator (30) whilst in the blocking
configuration, such that the actuator may be partially displaced but cannot
execute a delivery stroke.

**5.** A dispenser according to any preceding claim, wherein transition of the
fill completion interlock to the releasing configuration generates a tactile
signal, an audible signal, or both, perceptible to a user.

**6.** A dispenser according to any preceding claim, wherein the inlet valve (25)
has a flow area which increases with the pressure differential across the inlet
valve.

**7.** A dispenser according to claim 6, wherein the inlet valve (25) comprises a
poppet resiliently biased against a seat, the seat having a profile such that the
flow area between the poppet and the seat increases more than linearly with
poppet lift.

**8.** A dispenser according to any preceding claim, further comprising a
thermally responsive element (80) arranged to increase the flow area of the inlet
valve (25) as temperature decreases.

**9.** A dispenser according to claim 8, wherein the thermally responsive element
(80) comprises a bimetallic element or a shape memory alloy element.

**10.** A dispenser according to any preceding claim, wherein the discharge valve
(26) is a pre-compression valve having a predetermined cracking pressure, such
that the metering chamber does not discharge until the pressure therein exceeds
said cracking pressure.

**11.** A dispenser according to claim 10, wherein the cracking pressure is
between 1.5 and 4 bar, preferably between 2.0 and 3.0 bar.

**12.** A dispenser according to any preceding claim, wherein the fixed swept
volume is between 0.1 and 0.5 ml, preferably between 0.15 and 0.25 ml.

**13.** A dispenser according to any preceding claim, arranged such that the
volume delivered per delivery stroke varies by no more than 15 percent across a
liquid kinematic viscosity range of 20 to 100 centistokes at 25 °C.

**14.** A dispenser according to any preceding claim, further comprising an intake
conduit (50) having an inlet opening (51) disposed at a standoff distance (52)
above a floor (11) of the reservoir (10) so as to define a settling volume (53)
therebelow.

**15.** A dispenser according to claim 14, wherein the standoff distance (52) is
between 5 and 15 mm.

**16.** A dispenser according to claim 14 or 15, further comprising a first filter
element (54) disposed at the inlet opening (51) and a second filter element (55)
disposed upstream of a discharge orifice (27), the second filter element having a
smaller aperture than the first.

**17.** A dispenser according to claim 16, wherein the first filter element (54)
has an aperture between 400 and 800 µm and the second filter element (55) has an
aperture between 100 and 200 µm.

**18.** A dispenser according to claim 16 or 17, wherein the intake conduit (50),
the first filter element (54) and the second filter element (55) are carried upon
a common carrier (56) and are together removable from the reservoir as a unitary
cartridge.

**19.** A dispenser according to any preceding claim, wherein the reservoir (10)
is tubular and open at both ends, and is closed at a first end by a head closure
(12) carrying the metering chamber and at a second end by a removable base closure
(13), each closure sealing against the reservoir by an axial face seal (14).

**20.** A dispenser according to any preceding claim, further comprising a counter
(60) coupled to the actuator (30) and arranged to register the number of delivery
strokes executed, and thereby to indicate a quantity of liquid remaining.

**21.** A dispenser according to any preceding claim, further comprising a vent
(70) admitting air to the reservoir and comprising a hydrophobic membrane.

**22.** A dispenser according to any preceding claim, wherein the liquid is an
edible oil.

**23.** A method of delivering metered volumes of a liquid of unknown viscosity
from a manually actuated dispenser having a metering chamber of fixed swept
volume and a metering piston, the method comprising:

  (a) urging the metering piston through a return stroke under the action of a
      return spring, thereby drawing liquid into the metering chamber;
  (b) blocking a manually operable actuator so as to prevent a delivery stroke
      whilst the metering piston is between a discharge position and a
      predetermined fill position corresponding to said fixed swept volume;
  (c) releasing the actuator upon the metering piston attaining said predetermined
      fill position; and
  (d) thereafter executing a delivery stroke to expel said fixed swept volume,

  whereby the volume delivered is substantially independent of the viscosity of
  the liquid.

**24.** A method according to claim 23, further comprising increasing a flow area
of an inlet to the metering chamber in response to an increase in the pressure
differential across said inlet, in response to a decrease in temperature, or both.

## Abstract

A manually actuated dispenser delivers a metered volume of liquid substantially
independently of the liquid's viscosity. A metering chamber (20) of fixed swept
volume is charged during a return stroke of a piston (23) urged by a return
spring (24). Because the piston can advance only as rapidly as liquid enters
behind it, its position is a direct measure of the state of charge of the
chamber. A fill completion interlock (40) blocks the manually operable actuator
(30) until the piston (23) attains a fill position defined by a return stop (43),
whereupon a release cam (44) displaces a latch member (41) and permits a delivery
stroke. The volume delivered is therefore set by chamber geometry alone, the
effect of viscosity appearing as a short delay between actuations rather than as
an unperceived reduction in delivered volume. An inlet valve (25) whose flow area
increases with pressure differential, and a thermally responsive element (80),
shorten that delay. (Figure 2)

---

# PART D. Filing strategy

## D1. The sequence, which Section 39 largely dictates

| When | Action | Why |
|---|---|---|
| **Day 0** | **File Indian provisional specification** | Establishes the priority date. Starts both the Section 39 six week clock and the twelve month Paris Convention clock. Cheap and fast |
| **Day 0** | Password protect the website if it is live | Stops further public disclosure accruing |
| **Week 6** | Free to file abroad without Form 25 | Section 39 satisfied by the six week route |
| **By month 12** | **File PCT application** claiming Indian priority | One application preserving rights in most of the world. Also file the Indian complete specification by month 12 |
| Month 16 | International Search Report and Written Opinion | First real read on patentability. Decide whether to continue before spending on national phases |
| **Month 30 or 31** | **National or regional phase: EPO, USPTO, and any others** | The expensive step, deferred as long as possible |

Filing the Indian provisional first is not merely compliant, it is the correct
commercial sequence. It is the cheapest way to secure a date, and it defers every
large cost by up to thirty months while the product is validated.

## D2. Indicative costs

Ranges only, and they vary widely by firm. Confirm before committing.

| Step | Government fee | Professional fee |
|---|---|---|
| Indian provisional, natural person or startup, e-filed | approx ₹1,600 | ₹20,000 to ₹45,000 |
| Indian complete specification | approx ₹1,600 | ₹30,000 to ₹70,000 |
| Indian request for examination | approx ₹4,000 | included above |
| PCT international application including search | approx ₹1.5 to 2.5 lakh | ₹40,000 to ₹80,000 |
| EPO regional phase | €4,000 to €8,000 including translation and validation | varies |
| US national phase, small or micro entity | $1,000 to $2,000 | $6,000 to $12,000 |

Claim startup status with the Indian Patent Office where eligible, since the fee
reduction is substantial.

## D3. Run the searches before spending

Commission a professional novelty search before the complete specification, not
before the provisional. The provisional is cheap enough to file first and search
afterwards. Ask the searcher specifically to cover:

- metering pumps with actuation lockout or interlock dependent on chamber charge state
- inhaler and injection pen dose interlocks, which are the most likely citations
- viscosity compensation in unpowered dispensers
- IPC classes B05B 11/00, B67D 3/00, G01F 11/02, A47J 43/00

## D4. Also file, separately

**Design registration** under the Designs Act 2000 on the final form of the
product. It protects appearance, costs ₹1,000 in government fees for a startup
or small entity with Form 24, plus ₹5,000 to ₹8,000 professional, and gives ten
years extendable by five. This is the right instrument for the six module
architecture and the dual opening body, which are weak as patent subject matter
but strong as appearance. **File only after the patent provisional, and note that
a published design can also destroy design novelty.**

**Trade mark** for ENNA in class 21, with classes 8 and 11 as relevant.

---

# PART E. What this document is not

I am not a patent attorney, this is not legal advice, and nothing here has been
searched professionally. Specifically:

1. **No professional novelty search has been conducted.** The prior art in Part B
   was identified through ordinary web searching. A proper search will find art I
   have not seen, and it may well find something that reads directly on claim 1.
2. **The claims need professional revision.** Claim scope is the entire value of
   a patent and the wording above is a starting point for an attorney, not a
   filing text.
3. **Figures must be prepared** to the formal drawing standards of each office.
   Part C describes seven figures but none has been drawn.
4. **The Section 39 and disclosure questions in Part A require a lawyer's
   opinion on your actual facts**, particularly the date your site first became
   publicly reachable.
5. **A registered Indian patent agent is required** to prosecute an Indian
   application on your behalf.

## The single most important next step

**Establish the date your Amplify site first became publicly reachable, and
password protect it today if it is live.** Everything else in this document can
wait a week. That cannot, because in Europe and India the clock it started cannot
be stopped or reversed, only outrun.
