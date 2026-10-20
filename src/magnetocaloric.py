from util import en, pl


def add_magnetocaloric_entities(onto):
    """Register magnetocaloric entities with the ontology."""
    with onto:
        # ======================================================================
        # Temperature Interval class (not in EMMO, needed for span/range classes)
        # ======================================================================
        class TemperatureInterval(onto.PhysicalQuantity):
            """A temperature interval defined by two temperature values.

            This is a MagMO-specific subclass used for quantities that represent
            temperature spans or ranges (ΔT) rather than absolute temperatures.
            """

            prefLabel = en("TemperatureInterval")
            altLabel = [
                en("TemperatureSpan"),
                pl("ΔT"),
            ]
            is_a = [onto.hasMeasurementUnit.some(onto.TemperatureUnit)]

        # ======================================================================
        # Unit classes for MCE-specific units
        # MassSpecificEnergy, MassSpecificEnergyUnit, and JoulePerKilogram are
        # not present in EMMO 1.0.3 or upstream MagMO, so we define them here.
        # ======================================================================
        class MassSpecificEnergyUnit(onto.SIDimensionalUnit):
            """Class of units of energy per unit mass.

            Defined using SI base units for mass-specific energy quantities
            such as refrigerant capacity and relative cooling power.
            
            Note: J/kg = (kg·m²/s²)/kg = m²/s², so mass dimension cancels.
            """

            prefLabel = en("MassSpecificEnergyUnit")
            altLabel = [
                en("SpecificEnergyUnit"),
                en("EnergyPerMassUnit"),
            ]
            is_a = [onto.hasDimensionString.value("T-2 L+2 M0 I0 Θ0 N0 J0")]

        class JoulePerKilogram(onto.MassSpecificEnergyUnit):
            """Unit of energy per unit mass: J/kg."""

            prefLabel = en("JoulePerKilogram")
            altLabel = [
                pl("J/kg"),
                pl("J*kg^-1"),
            ]
            unitSymbol = en("J/kg")
            ucumCode = en("J.kg-1")

        class MassSpecificEnergy(onto.PhysicalQuantity):
            """Mass-specific energy quantity (energy per unit mass)."""

            prefLabel = en("MassSpecificEnergy")
            altLabel = [
                en("SpecificEnergy"),
                en("EnergyPerUnitMass"),
            ]
            is_a = [onto.hasMeasurementUnit.some(onto.MassSpecificEnergyUnit)]

        # ======================================================================
        # MCE Quantity Classes
        # ======================================================================

        # --- Entropy Change Classes ---
        class MagneticEntropyChange(onto.SpecificEntropy):
            """Change in the magnetic contribution to the mass-specific entropy of a
            magnetocaloric material caused by a change in applied magnetic field,
            usually evaluated under isothermal conditions.
            
            Note: This represents mass-specific magnetic entropy change in J/(kg·K).
            """

            prefLabel = en("MagneticEntropyChange")
            altLabel = [
                pl("ΔSₘ"),
                pl("ΔSiso"),
                pl("DeltaSm"),
                en("IsothermalMagneticEntropyChange"),
            ]
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocaloric_effect")
            is_a = [onto.hasMeasurementUnit.some(onto.EntropyPerMassUnit)]

        class MaximumMagneticEntropyChange(MagneticEntropyChange):
            """Maximum value of the magnetic entropy change obtained for a given
            magnetic field change, usually observed near the magnetic phase
            transition temperature."""

            prefLabel = en("MaximumMagneticEntropyChange")
            altLabel = [
                pl("ΔSₘ,max"),
                pl("DeltaSmMax"),
                en("MaximumIsothermalMagneticEntropyChange"),
            ]
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocaloric_effect")

        class ReversibleMagneticEntropyChange(MagneticEntropyChange):
            """Recoverable component of the magnetic entropy change that can be
            repeatedly obtained during the application and removal of a magnetic
            field under a specified cyclic measurement protocol."""

            prefLabel = en("ReversibleMagneticEntropyChange")
            altLabel = [
                pl("ΔSₘ,rev"),
                pl("DeltaSmRev"),
                en("ReversibleIsothermalMagneticEntropyChange"),
            ]
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocaloric_effect")

# introduce the following new (check descr. and altLabel)
        class ReversibleAdiabaticTemperatureChange(MagneticEntropyChange):
            """Recoverable component of the adiabatic temerature change that can be
            repeatedly obtained during the application and removal of a magnetic
            field under a specified cyclic measurement protocol."""

            prefLabel = en("ReversibleAdiabaticTemperatureChange")
            altLabel = [
                pl("ΔSₘ,rev"),
                pl("DeltaSmRev"),
                en("ReversibleAdiabaticTemperatureChange"),
            ]
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocaloric_effect")



        # --- Temperature Change Classes ---
        class AdiabaticTemperatureChange(TemperatureInterval):
            """Temperature change of a magnetocaloric material caused by the
            application or removal of a magnetic field under adiabatic conditions."""

            prefLabel = en("AdiabaticTemperatureChange")
            altLabel = [
                pl("ΔTₐd"),
                pl("DeltaTad"),
                en("AdiabaticTemperatureVariation"),
            ]
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocaloric_effect")

        # --- Refrigerant Capacity Classes ---
        class RefrigerantCapacity(onto.MassSpecificEnergy):
            """Amount of heat that can be transferred by a magnetocaloric material
            between cold and hot reservoirs over a selected operating temperature
            interval."""

            prefLabel = en("RefrigerantCapacity")
            altLabel = [
                pl("RC"),
                en("RefrigerationCapacity"),
                en("CoolingCapacity"),
            ]

        class EffectiveRefrigerantCapacity(RefrigerantCapacity):
            """Net amount of heat that can be transferred by a magnetocaloric
            material over a specified temperature interval after accounting
            for hysteresis losses."""

            prefLabel = en("EffectiveRefrigerantCapacity")
            altLabel = [
                pl("RCeff"),
                pl("EffectiveRC"),
                en("NetRefrigerantCapacity"),
                en("NetRC"),
            ]
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocaloric_effect")

        class RelativeCoolingPower(onto.MassSpecificEnergy):
            """Magnetocaloric performance quantity used to estimate the cooling
            potential of a material, commonly related to the maximum magnetic
            entropy change and the temperature width of the entropy-change peak."""

            prefLabel = en("RelativeCoolingPower")
            altLabel = [
                pl("RCP"),
                en("RelativeRefrigerantPower"),
            ]

        # --- Temperature Span/Range Classes ---
        class TemperatureSpanOfMagnetocaloricEffect(TemperatureInterval):
            """Temperature interval over which a magnetocaloric material exhibits
            a useful magnetic entropy change or adiabatic temperature change for
            a specified magnetic field change."""

            prefLabel = en("TemperatureSpanOfMagnetocaloricEffect")
            altLabel = [
                pl("ΔTspan"),
                pl("DeltaTspan"),
                en("MCE_Temperature_Span"),
                en("MagnetocaloricOperatingTemperatureSpan"),
            ]
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocaloric_effect")

        class PeakTemperatureOfMagnetocaloricEffect(onto.ThermodynamicTemperature):
            """Temperature at which the magnetic entropy change or adiabatic
            temperature change reaches its maximum value for a specified
            magnetic field change."""

            prefLabel = en("PeakTemperatureOfMagnetocaloricEffect")
            altLabel = [
                pl("Tpeak"),
                pl("PeakMCETemperature"),
                en("MagneticEntropyChangePeakTemperature"),
            ]
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocaloric_effect")

        class FullWidthAtHalfMaximumOfMagneticEntropyChange(TemperatureInterval):
            """Temperature interval between the two temperatures at which the
            absolute magnetic entropy change equals one half of its maximum
            value for a specified magnetic field change."""

            prefLabel = en("FullWidthAtHalfMaximumOfMagneticEntropyChange")
            altLabel = [
                pl("FWHM"),
                pl("ΔT_FWHM"),
                en("MagneticEntropyChangePeakWidth"),
            ]
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Full_width_at_half_maximum")

        class OperatingTemperatureRangeOfMagnetocaloricMaterial(TemperatureInterval):
            """Temperature interval within which a magnetocaloric material can
            operate effectively in a specified magnetic refrigeration cycle
            while satisfying defined performance and reversibility criteria."""

            prefLabel = en("OperatingTemperatureRangeOfMagnetocaloricMaterial")
            altLabel = [
                en("OperatingTemperatureRange"),
                en("WorkingTemperatureRange"),
                en("MCEOperatingRange"),
            ]
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocaloric_effect")

        # --- Efficiency Class ---
        class MagnetocaloricEfficiency(onto.ISQDimensionlessQuantity):
            """Dimensionless performance quantity expressing the useful cooling
            effect produced by a magnetocaloric process relative to the energy
            or work supplied during a specified magnetic refrigeration cycle."""

            prefLabel = en("MagnetocaloricEfficiency")
            altLabel = [
                en("CoolingEfficiency"),
                en("MagneticCoolingEfficiency"),
                en("MCE_Efficiency"),
            ]
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocaloric_effect")
