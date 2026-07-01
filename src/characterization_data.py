"""Entities related to characterization data.

- XRD: X-Ray Diffraction.
- EDX: Energy-Dispersive X-ray Spectroscopy.
- MOKE: Magneto-Optic Kerr Effect.
- Profil: Profilometry measurement.
"""

from util import en, pl


def add_characterization_data_entities(onto):
    """Add all entities related to characterization data."""
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
