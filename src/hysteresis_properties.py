"""Hysteresis properties."""

from util import en, enGB, enUS, pl


def add_hysteresis_properties_entities(onto):
    with onto:

        class CoercivityHc(onto.Coercivity):
            """The internal magnetic field -Hc at which the macroscopic
            magnetization vanishes is the coercivity or coercive force.

            Although it is not an intrinsic property in our sense of the term,
            the M-H loop coercivity Hc is sometimes referred to as
            'intrinsic' coercivity.
            """

            prefLabel = en("CoercivityHc")
            altLabel = [
                en("CoercivityInternal"),
                en("CoercivityHcInternal"),
                en("CoerciveField"),
                pl("Hc"),
            ]
            IECEntry = [
                pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=221-02-35"),
                pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=121-12-69"),
                pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=221-02-36"),
            ]
            wikidataReference = pl("https://www.wikidata.org/wiki/Q432635")

        class CoercivityBHc(onto.Coercivity):
            """Defined as internal field on the B(H) loop where B = 0.
            It is also called flux coercivity BHc.

            BHc depends on sample shape and has to be corrected for the
            demagnetizing field.
            """

            prefLabel = en("CoercivityBHc")
            altLabel = pl("BHc")

        class CoercivityHcExternal(onto.Coercivity):
            """The external magnetic field -H'c at which the macroscopic
            magnetization vanishes.
            The coercivity on M(H') loop, where H' is the external field."""

            prefLabel = en("CoercivityHcExternal")
            altLabel = pl("H'c")

        class CoercivityBHcExternal(onto.Coercivity):
            """Defined as external field on the B(H') loop where
            B = 0. H' is the external field."""

            prefLabel = en("CoercivityBHcExternal")
            altLabel = pl("BH'c")

        class SwitchingFieldCoercivity(onto.MagneticFieldStrength):
            """Defined by the maximum slope of the descending branch of
            the M-H hysteresis loop, with H the internal field."""

            comment = pl(
                "This field is often used when analysing the temperature\
                dependent coercivity for deriving microstructural parameters."
            )
            prefLabel = en("SwitchingFieldCoercivity")
            altLabel = pl("Hsw")

        class SwitchingFieldCoercivityExternal(onto.MagneticFieldStrength):
            """Defined by the maximum slope of the descending branch of
            the M-H' hysteresis loop, with H' the external field."""

            prefLabel = en("SwitchingFieldCoercivityExternal")
            altLabel = pl("H'sw")

        class KneeField(onto.MagneticFieldStrength):
            """The maximum working field - also named knee field H_K, is
            defined as the reverse internal field for which the magnetization
            is reduced by 10%; thus it corresponds to the point on the
            magnetization loop for which M = 0.9 Mr (J = 0.9 Jr)."""

            prefLabel = en("KneeField")
            altLabel = [
                en("KneeFieldInternal"),
                en("MaximumWorkingField"),
                pl("Hk"),
            ]

        class KneeFieldExternal(onto.MagneticFieldStrength):
            """The maximum working field - also named knee field H_K,
            is defined as the reverse external field for which the
            magnetization is reduced by 10%; thus it corresponds to the
            point on the magnetization loop for which M = 0.9 Mr (J = 0.9 Jr).
            """

            prefLabel = en("KneeFieldExternal")
            altLabel = pl("H'k")

        class Remanence(onto.ElectromagneticQuantity):
            """The remanence Mr which remains when the applied field is
            restored to zero in the hysteresis loop"""

            prefLabel = en("Remanence")
            altLabel = [
                enUS("RemanentMagnetization"),
                enGB("RemanentMagnetisation"),
                pl("Mr"),
            ]
            is_a = [onto.hasMeasurementUnit.some(onto.MagneticFieldStrengthUnit)]
            wikidataReference = pl("https://www.wikidata.org/wiki/Q4150950")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Remanence")
            IECEntry = pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=221-02-40")

        class RemanentMagneticPolarization(onto.ElectromagneticQuantity):
            """The remanent magnetic polarization Jr which remains when the applied
            field is restored to zero in the hysteresis loop"""

            prefLabel = en("RemanentMagneticPolarization")
            altLabel = [
                enGB("RemanentMagneticPolarisation"),
                pl("Jr"),
            ]
            is_a = [onto.hasMeasurementUnit.some(onto.MagneticFluxDensityUnit)]
            IECEntry = pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=221-02-39")

        class ExternalSusceptibility(onto.MagneticSusceptibility):
            """Ratio of the change of magnetization and the external
            field: M = chi' H'."""

            prefLabel = en("ExternalSusceptibility")
            altLabel = pl("chi'")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q691463")

        class InternalSusceptibility(onto.MagneticSusceptibility):
            """Ratio of the change of magnetization and the internal
            field: M = chi H."""

            prefLabel = en("InternalSusceptibility")
            altLabel = pl("chi")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q691463")

        class MassSusceptibility(onto.ElectromagneticQuantity):
            """Ratio of the change of the magnetic moment per unit mass and
            the internal field: sigma = chi_m H."""

            comment = en("MagneticSusceptibilityPerMassDensity")
            prefLabel = en("MassSusceptibility")
            altLabel = pl("chi_m")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q104655916")
            is_a = [onto.hasMeasurementUnit.some(onto.VolumePerMassUnit)]

        class AbsolutePermeability(onto.ElectromagneticQuantity):
            """Ratio of the change of magnetic flux density and the internal
            field: B = mu H."""

            prefLabel = en("AbsolutePermeability")
            altLabel = pl("mu")
            is_a = [onto.hasMeasurementUnit.some(onto.PermeabilityUnit)]
            IECEntry = pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=121-12-28")

        class MaximumEnergyProduct(onto.ElectromagneticQuantity):
            """The value of the maximum energy product (BH)max is deduced from a
            plot of BH(B) for all points of the second quadrant of the B-H
            hysteresis loop. BH varies with B going through a maximum value (BH)max
            for a particular value of B.

            (BH)max equals the area of the largest second-quadrant rectangle which
            fits under the B-H loop.

            The maximum energy product is considered to be the best single index
            of quality of a permanent magnet material.
            It is twice the energy stored in the stray field of the magnet of
            optimal shape.
            """

            prefLabel = en("MaximumEnergyProduct")
            altLabel = pl("(BH)max")
            is_a = [onto.hasMeasurementUnit.some(onto.EnergyDensityUnit)]
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Maximum_energy_product")

        class SaturationMagneticPolarization(onto.ElectromagneticQuantity):
            """The Saturation magnetic polarization Jsat is the maximum
            obtainable magnetic polarization for a given substance
            at a given temperature. Jsat should be used instead of Js to avoid
            confusion with the symbol for the spontaneous polarization"""

            prefLabel = en("SaturationMagneticPolarization")
            altLabel = [
                enGB("SaturationMagneticPolarisation"),
                en("Jsat"),
            ]
            is_a = [onto.hasMeasurementUnit.some(onto.MagneticFluxDensityUnit)]
            IECEntry = pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=221-01-05")

        class SaturationMagnetization(onto.ElectromagneticQuantity):
            """The Saturation magnetization Msat is the maximum
            obtainable magnetic magnetization for a given substance
            at a given temperature. Msat should be used instead Ms to avoid
            confusion with the symbol for the SpontaneousMagnetization"""

            prefLabel = en("SaturationMagnetization")
            altLabel = [
                enGB("SaturationMagnetisation"),
                en("Msat"),
            ]
            is_a = [onto.hasMeasurementUnit.some(onto.MagneticFieldStrengthUnit)]
            IECEntry = pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=221-01-04")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Saturation_(magnetic)")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q2630994")

        class LoopSquarenessFactorInternal(onto.ElectromagneticQuantity, onto.RatioQuantity):
            """The internal loop squareness factor SF is defined as the ratio of
            the internal KneeField Hk over the internal Coercivity Hc
            (SF = KneeFieldInternal / CoercivityHcInternal)."""

            prefLabel = en("LoopSquarenessFactorInternal")
            altLabel = [
                en("SquarenessFactorInternal"),
                en("SF_internal"),
            ]
            is_a = [onto.hasMeasurementUnit.some(onto.DimensionlessUnit)]

        class LoopSquarenessFactorExternal(onto.ElectromagneticQuantity, onto.RatioQuantity):
            """The external loop squareness factor is defined as the ratio of
            the external KneeField H'k over the external Coercivity H'c
            (SF' = KneeFieldExternal / CoercivityHcExternal)."""

            prefLabel = en("LoopSquarenessFactorExternal")
            altLabel = [
                en("SquarenessFactorExternal"),
                en("SF_external"),
            ]
            is_a = [onto.hasMeasurementUnit.some(onto.DimensionlessUnit)]

        class LoopSquareness(onto.ElectromagneticQuantity, onto.RatioQuantity):
            """The external loop squareness is defined as the ratio of
            the remanent polarisation over the saturation polarisation
            (SS = RemanentMagneticPolarization / SaturationMagneticPolarization)."""

            prefLabel = en("LoopSquareness")
            altLabel = [
                en("Squareness"),
                en("SS"),
            ]
            is_a = [onto.hasMeasurementUnit.some(onto.DimensionlessUnit)]

        class MagneticHysteresisProperties(onto.Property):
            """The essential practical characteristic of any ferromagnetic material
            is the irreversible nonlinear response of magnetization M to an imposed
            magnetic field H. This response is given by the hysteresis loop. The
            characteristics of hysteresis loop are known as hysteresis properties.

            Instead of M(H), other quantities can be used to plot a hysteresis loop.

            M(H): Magnetization as function of the internal field.
            M(H'): Magnetization as function of the external field.

            J(H): Magnetic polarization as function of the internal field.
            J(H'): Magnetic polarization as function of the external field.

            B(H): Magnetic flux density as function of the internal field.
            B(H'): Magnetic flux density as function of the external field.
            """

            prefLabel = en("MagneticHysteresisProperties")
            is_a = [
                onto.hasProperty.exactly(1, onto.CoercivityHc),
                onto.hasProperty.min(0, onto.CoercivityBHc),
                onto.hasProperty.min(0, onto.CoercivityHcExternal),
                onto.hasProperty.min(0, onto.CoercivityBHcExternal),
                onto.hasProperty.min(0, onto.SwitchingFieldCoercivity),
                onto.hasProperty.min(0, onto.SwitchingFieldCoercivityExternal),
                onto.hasProperty.min(0, onto.KneeField),
                onto.hasProperty.min(0, onto.KneeFieldExternal),
                onto.hasProperty.exactly(1, onto.Remanence),
                onto.hasProperty.min(0, onto.RemanentMagneticPolarization),
                onto.hasProperty.min(0, onto.SaturationMagneticPolarization),
                onto.hasProperty.min(0, onto.LoopSquarenessFactorInternal),
                onto.hasProperty.min(0, onto.LoopSquarenessFactorExternal),
                onto.hasProperty.min(0, onto.LoopSquareness),
                onto.hasProperty.min(0, onto.MaximumEnergyProduct),
            ]

        class ExtrinsicMagneticProperties(onto.Property):
            """Extrinsic magnetic Properties depend on the microstructure."""

            prefLabel = en("ExtrinsicMagneticProperties")
            is_a = [
                onto.hasProperty.exactly(1, onto.MagneticHysteresisProperties),
                onto.hasProperty.min(0, onto.DemagnetizingFactor),
                onto.hasProperty.min(0, onto.AbsolutePermeability),
                onto.hasProperty.min(0, onto.RelativePermeability),
            ]
