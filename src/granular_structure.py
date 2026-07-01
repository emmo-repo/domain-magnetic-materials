"""Grains and granular structure."""

from util import en, pl


def add_granular_structure_entities(onto):
    """Add entities related to grains and granular structure."""
    with onto:

        class EulerAngles(onto.Quantity):
            """Three angles introduced by Leonhard Euler to describe the
            orientation of a rigid body with respect to a fixed coordinate
            system."""

            prefLabel = en("EulerAngles")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q751290")
            is_a = [onto.hasProperty.exactly(3, onto.Angle)]

        class CrystallographicOrientation(onto.Property):
            """Relative direction of a crystallite in space with respect to
            another, disregarding distance."""

            prefLabel = en("CrystallographicOrientation")
            altLabel = en("CrystalOrientation")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q11799166")
            is_a = [onto.hasProperty.exactly(1, EulerAngles)]

        class GrainMisalignmentAngle(onto.Angle):
            """Standard deviation of the angle of the easy axis with respect to
            the alignment direction."""

            prefLabel = en("GrainMisalignmentAngle")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q117089304")

        class EasyAxisDistributionSigma(onto.Angle):
            """Standard deviation of the grain misalignment angle in an ensembles
            of misaligned magnetic particles.

            This refers not only to isotropic magnets but also to
            partly aligned or textured magnets, where the easy-axis distribution
            is described by a function P(theta).
            """

            prefLabel = en("EasyAxisDistributionSigma")

        class Grain(onto.Crystal):
            """A grain is a small or even microscopic crystal which forms, for
            example, during the cooling of many materials."""

            prefLabel = en("Grain")
            altLabel = en("Crystallite")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q899604")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Crystallite")
            is_a = [
                onto.hasProperty.exactly(1, onto.CrystalStructure),
                onto.hasProperty.exactly(1, onto.ChemicalComposition),
                onto.hasProperty.exactly(1, onto.Diameter),
                onto.hasProperty.exactly(1, onto.CrystallographicOrientation | onto.GrainMisalignmentAngle),
            ]

        class MeanGrainSize(onto.Length):
            """The mean of the grain diameter of grains. Diameter is the diameter
            of a sphere with equivalent volume."""

            prefLabel = en("MeanGrainSize")

        class SigmaGrainSize(onto.Length):
            """The standard deviation of the grain diameter of grains. Diameter is
            the diameter of a sphere with equivalent volume."""

            prefLabel = en("SigmaGrainSize")

        class GrainSizeDistribution(onto.Property):
            """Function representing relative sizes of grains in a system.
            Given by its mean and standard deviation of a lognormal distribution
            """

            prefLabel = en("GrainSizeDistribution")
            altLabel = en("ParticleSizeDistribution")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Particle-size_distribution")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q2054937")
            is_a = [
                onto.hasProperty.exactly(1, onto.MeanGrainSize),
                onto.hasProperty.exactly(1, onto.SigmaGrainSize),
            ]

        class MagneticMaterial(onto.MaterialByStructure):
            """Magnetically ordered solids which have atomic magnetic moments due
            to unpaired electrons."""

            prefLabel = en("MagneticMaterial")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q11587827")
            is_a = [
                onto.hasProperty.exactly(1, onto.ChemicalComposition),
                onto.hasProperty.exactly(1, onto.Density),
                onto.hasProperty.exactly(1, onto.IntrinsicMagneticProperties),
            ]

        class AmorphousMagneticMaterial(onto.AmorphousMaterial, onto.MagneticMaterial):
            """Any amorphous structure entails a distribution of nearest-neighbour
            environments and bond lengths for a given magnetic atom, described by
            the radial distribution function and higher-order correlation
            functions. These distributions lead to a distribution of site moments,
            exchange interactions, dipolar and crystal fields, all of which
            influence the nature of the magnetic order."""

            prefLabel = en("AmorphousMagneticMaterial")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Amorphous_magnet")

        class GranularStructure(onto.CrystallineMaterial):
            """Ensemble of grains of 1 or more grains."""

            prefLabel = en("GranularStructure")
            is_a = [
                onto.hasProperty.exactly(1, onto.CrystalStructure),
                onto.hasProperty.exactly(1, onto.GrainSizeDistribution),
                onto.hasProperty.min(0, onto.XrayDiffractionData),
                onto.hasSpatialPart.min(0, onto.Grain),
            ]

        class NonMagneticMaterial(onto.Material):
            """A material which is non-magnetic."""

            prefLabel = en("NonMagneticMaterial")
            is_a = [
                onto.hasProperty.exactly(1, onto.ChemicalComposition),
                onto.hasProperty.exactly(1, onto.Density),
                onto.hasSpatialPart.min(0, onto.GranularStructure),
            ]

        class CrystallineMagneticMaterial(onto.GranularStructure, onto.MagneticMaterial):
            """Magnetic material with crystalline structure."""

            prefLabel = en("CrystallineMagneticMaterial")
