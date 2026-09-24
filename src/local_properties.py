"""Local properties."""

from util import en, pl


def add_local_properties_entities(onto):
    """Add local properties entities."""
    with onto:

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

        class ThinFilmMagnet(onto.Magnet, onto.MaterialBySize):
            """Piece of matter made of one or more magnetic material
            in form a thin film."""

            prefLabel = en("ThinFilmMagnet")
            is_a = [
                onto.hasProperty.min(0, onto.InducedMagneticAnisotropy),
                onto.hasProperty.min(0, onto.SampleGeometry),
                onto.hasProperty.min(0, onto.LocalThickness),
                onto.hasProperty.min(0, onto.LocalCoercivity),
                onto.hasProperty.min(0, onto.LocalReflectivity),
                onto.hasProperty.min(0, onto.LocalXrayDiffractionData),
                onto.hasProperty.min(0, onto.LocalLatticeConstantA),
                onto.hasProperty.min(0, onto.LocalLatticeConstantC),
                # New properties from issue #20
                onto.hasProperty.min(0, onto.LocalAtomPercent),
                onto.hasProperty.min(0, onto.LocalMassPercent),
                onto.hasProperty.min(0, onto.LocalAnnealingTemperature),
                onto.hasProperty.min(0, onto.LocalAnnealingTime),
                onto.hasProperty.min(0, onto.LocalPhaseFraction),
                onto.hasProperty.min(0, onto.LocalEdxData),
                onto.hasProperty.min(0, onto.LocalMokeData),
                onto.hasProperty.min(0, onto.LocalProfilometryData),
                onto.hasProperty.min(0, onto.Xrd2dImage),
            ]
