"""Characterization data, local properties, composition, and processing."""

from util import en, pl


def add_characterization_and_processing_entities(onto):
    """Add entities for the grouped module."""
    with onto:
        class XrdTwoThetaAngles(onto.Vector):
            """The 2theta angles at which the counts are measured during X-ray
            diffraction."""

            prefLabel = en("XrdTwoThetaAngles")
            altLabel = en("XRDTwoThetaAngles")
            is_a = [
                onto.hasProperty.some(onto.Angle),
            ]

        class XrdCounts(onto.Vector):
            """Counts as a function of 2theta angle obtained from X-ray
            diffraction."""

            prefLabel = en("XrdCounts")
            altLabel = en("XRDCounts")
            is_a = [
                onto.hasMeasurementUnit.some(onto.CountingUnit),
            ]

        class XrayDiffractionData(onto.Property, onto.Matrix):
            """Counts as a function of 2theta angle obtained from X-ray
            diffraction."""

            prefLabel = en("XrayDiffractionData")
            is_a = [
                onto.hasProperty.exactly(1, XrdTwoThetaAngles),
                onto.hasProperty.exactly(1, XrdCounts),
            ]

        class Xrd2dImage(onto.Property, onto.Matrix):
            """2D array containing all pixel intensities from a 2D XRD camera.
            This is the raw XRD data from which 1D spectra are obtained."""

            prefLabel = en("Xrd2dImage")
            altLabel = [
                en("Xrd2DImage"),
                en("XRD2dImage"),
                en("XRD2DImage"),
            ]
            is_a = [
                onto.hasMeasurementUnit.some(onto.CountingUnit),
            ]

        class EdxEnergy(onto.Vector):
            """The energy values at which the counts are measured during
            Energy-Dispersive X-ray spectroscopy."""

            prefLabel = en("EdxEnergy")
            altLabel = en("EDXEnergy")
            is_a = [
                onto.hasMeasurementUnit.some(onto.EnergyUnit),
            ]

        class EdxCounts(onto.Vector):
            """Counts as a function of energy obtained from Energy-Dispersive
            X-ray spectroscopy."""

            prefLabel = en("EdxCounts")
            altLabel = en("EDXCounts")
            is_a = [
                onto.hasMeasurementUnit.some(onto.CountingUnit),
            ]

        class EdxData(onto.Property, onto.Matrix):
            """Counts as a function of energy obtained from Energy-Dispersive
            X-ray spectroscopy."""

            prefLabel = en("EdxData")
            altLabel = [en("EDXData"), en("EnergyDispersiveXraySpectroscopyData")]
            is_a = [
                onto.hasProperty.exactly(1, EdxEnergy),
                onto.hasProperty.exactly(1, EdxCounts),
            ]

        class MokeAppliedField(onto.Vector):
            """The applied magnetic field values during MOKE measurement."""

            prefLabel = en("MokeAppliedField")
            altLabel = en("MOKEAppliedField")
            is_a = [
                onto.hasMeasurementUnit.some(onto.MagneticFieldStrengthUnit),
            ]

        class MokeKerrSignal(onto.Vector):
            """The Kerr signal (rotation or ellipticity) as a function of
            applied field obtained from MOKE measurement."""

            prefLabel = en("MokeKerrSignal")
            altLabel = [
                en("MOKEKerrSignal"),
                en("KerrSignal"),
            ]
            is_a = [
                onto.hasMeasurementUnit.some(onto.DimensionlessUnit),
            ]

        class MokeData(onto.Property, onto.Matrix):
            """Kerr signal as a function of applied magnetic field obtained
            from Magneto-Optic Kerr Effect measurement."""

            prefLabel = en("MokeData")
            altLabel = [
                en("MOKEData"),
                en("MagnetoOpticKerrEffectData"),
            ]
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magneto-optic_Kerr_effect")
            IECEntry = pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=121-12-97")
            is_a = [
                onto.hasProperty.exactly(1, MokeAppliedField),
                onto.hasProperty.exactly(1, MokeKerrSignal),
            ]

        class ProfilDistance(onto.Vector):
            """The distance values along the scan direction during
            profilometry measurement."""

            prefLabel = en("ProfilDistance")
            altLabel = en("PROFILDistance")
            is_a = [
                onto.hasMeasurementUnit.some(onto.LengthUnit),
            ]

        class ProfilTotalProfile(onto.Vector):
            """The height profile as a function of distance obtained from
            profilometry measurement."""

            prefLabel = en("ProfilTotalProfile")
            altLabel = en("PROFILTotalProfile")
            is_a = [
                onto.hasMeasurementUnit.some(onto.LengthUnit),
            ]

        class ProfilometryData(onto.Property, onto.Matrix):
            """Height profile as a function of distance obtained from
            profilometry measurement."""

            prefLabel = en("ProfilometryData")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Profilometer")
            is_a = [
                onto.hasProperty.exactly(1, ProfilDistance),
                onto.hasProperty.exactly(1, ProfilTotalProfile),
            ]
        class Reflectivity(onto.Property):
            """Capacity of an object to reflect light."""

            prefLabel = en("Reflectivity")
            altLabel = [
                en("Reflectance"),
                pl("R"),
            ]
            wikidataReference = pl("https://www.wikidata.org/wiki/Q663650")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Reflectance")
            is_a = [
                onto.hasMeasurementUnit.some(onto.DimensionlessUnit),
            ]

        class LocalReflectivity(onto.Reflectivity):
            """Local reflectivity measured with the magneto-optic Kerr effect."""

            prefLabel = en("LocalReflectivity")
            is_a = [
                onto.hasProperty.exactly(1, onto.PositionVector),
            ]

        class LocalCoercivity(onto.CoercivityHcExternal):
            """Local coercive field measured with the magneto-optic Kerr effect."""

            prefLabel = en("LocalCoercivity")
            is_a = [
                onto.hasProperty.exactly(1, onto.PositionVector),
            ]

        class LocalXrayDiffractionData(onto.XrayDiffractionData):
            """Local X-ray diffraction data."""

            prefLabel = en("LocalXrayDiffractionData")
            is_a = [
                onto.hasProperty.exactly(1, onto.PositionVector),
            ]

        class LocalLatticeConstantA(onto.LatticeConstantA):
            """The length of lattice vectors `a`, where lattice vectors
            `a`, `b` and `c` defines the unit cell, measured locally."""

            prefLabel = en("LocalLatticeConstantA")
            is_a = [
                onto.hasProperty.exactly(1, onto.PositionVector),
            ]

        class LocalLatticeConstantC(onto.LatticeConstantC):
            """The length of lattice vectors `c`, where lattice vectors
            `a`, `b` and `c` defines the unit cell, measured locally."""

            prefLabel = en("LocalLatticeConstantC")
            is_a = [
                onto.hasProperty.exactly(1, onto.PositionVector),
            ]

        class LocalThickness(onto.Thickness):
            """The thickness of the film measured locally."""

            prefLabel = en("LocalThickness")
            is_a = [
                onto.hasProperty.exactly(1, onto.PositionVector),
            ]

        class LocalAtomPercent(onto.RatioQuantity):
            """Local atomic percentage obtained from EDX quantification."""

            prefLabel = en("LocalAtomPercent")
            altLabel = [en("LocalAtomicPercent"), en("at.%")]
            is_a = [
                onto.hasMeasurementUnit.some(onto.Percent),
                onto.hasProperty.exactly(1, onto.PositionVector),
            ]

        class LocalMassPercent(onto.RatioQuantity):
            """Local mass percentage obtained from EDX quantification."""

            prefLabel = en("LocalMassPercent")
            altLabel = [en("LocalWeightPercent"), en("wt.%")]
            is_a = [
                onto.hasMeasurementUnit.some(onto.Percent),
                onto.hasProperty.exactly(1, onto.PositionVector),
            ]

        class LocalAnnealingTemperature(onto.ThermodynamicTemperature):
            """Local annealing temperature from heat treatment such as
            Rapid Thermal Annealing (RTA)."""

            prefLabel = en("LocalAnnealingTemperature")
            is_a = [
                onto.hasProperty.exactly(1, onto.PositionVector),
            ]

        class LocalAnnealingTime(onto.Duration):
            """Local annealing time (duration) from heat treatment such as
            Rapid Thermal Annealing (RTA)."""

            prefLabel = en("LocalAnnealingTime")
            altLabel = en("LocalAnnealingDuration")
            is_a = [
                onto.hasProperty.exactly(1, onto.PositionVector),
            ]

        class LocalPhaseFraction(onto.RatioQuantity):
            """Local phase fraction obtained from XRD analysis, typically
            expressed in weight percent."""

            prefLabel = en("LocalPhaseFraction")
            altLabel = en("LocalPhaseContent")
            is_a = [
                onto.hasMeasurementUnit.some(onto.Percent),
                onto.hasProperty.exactly(1, onto.PositionVector),
            ]

        class LocalEdxData(onto.EdxData):
            """Local EDX data measured at a specific position."""

            prefLabel = en("LocalEdxData")
            altLabel = en("LocalEDXData")
            is_a = [
                onto.hasProperty.exactly(1, onto.PositionVector),
            ]

        class LocalMokeData(onto.MokeData):
            """Local MOKE data measured at a specific position."""

            prefLabel = en("LocalMokeData")
            altLabel = en("LocalMOKEData")
            is_a = [
                onto.hasProperty.exactly(1, onto.PositionVector),
            ]

        class LocalProfilometryData(onto.ProfilometryData):
            """Local profilometry data measured at a specific position."""

            prefLabel = en("LocalProfilometryData")
            is_a = [
                onto.hasProperty.exactly(1, onto.PositionVector),
            ]

