"""Materials, microstructure, geometry, layers, and physical objects."""

from owlready2 import Not

from util import en, enGB, pl


def _add_sample_geometry_entities(onto):
    """Add the G1 geometry foundation required by G2."""
    with onto:

        class RectangularCuboid(onto.EuclideanSpace):
            """A rectangular cuboid is a special case of a cuboid with rectangular
            faces in which all of its dihedral angles are right angles."""

            prefLabel = en("RectangularCuboid")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q262959")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Rectangular_cuboid")

        class GeometricalSize(onto.Property):
            """Spatial extension along the principal axes."""

            prefLabel = en("GeometricalSize")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Size")
            is_a = [onto.hasProperty.exactly(3, onto.Length)]

        class GeometricShape(onto.Property, onto.Geometrical):
            """Geometric shape.

            Two extrinsic properties, the remanence Mr
            and coercivity Hc, which depend on the sample shape
            """

            prefLabel = en("GeometricShape")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q207961")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Shape")
            is_a = [onto.hasSpatialDirectPart.exactly(1, onto.Cylinder | RectangularCuboid)]

        class SampleGeometry(onto.Property):
            """The size and shape of the magnet"""

            prefLabel = en("SampleGeometry")
            is_a = [
                onto.hasProperty.exactly(1, onto.GeometricalSize),
                onto.hasProperty.exactly(1, onto.GeometricShape),
            ]

        class DemagnetizingFactor(onto.ElectromagneticQuantity):
            """For a uniformly magnetized ellipsoid with magnetization along a
            major axis the demagnetizing field is Hd = -N M.

            The principal components of the diagonal demagnetizing tensor form
            the demagnetizing factors. Only two of the three are independent
            because the demagnetizing tensor has unit trace Nx + Ny + Nz = 1.
            """

            comment = pl(
                "H = H' - DM, where D is the demagnetizing factor, M is the magnetization, and H is the internal field."
            )
            prefLabel = en("DemagnetizingFactor")
            altLabel = [
                enGB("DemagnetisingFactor"),
                pl("N"),
                pl("D"),
            ]
            is_a = [onto.hasMeasurementUnit.some(onto.DimensionlessUnit)]
            IECEntry = pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=121-12-63")


def add_materials_and_objects_entities(onto):
    """Add G1 materials, structure, layers, and objects."""
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

        class MainMagneticPhase(onto.MagneticMaterial, onto.PhaseOfMatter):
            """Main phase of the magnet"""

            prefLabel = en("MainMagneticPhase")
            is_a = [
                onto.hasProperty.some(onto.VolumeFraction),
                onto.hasSpatialPart.exactly(1, onto.AmorphousMagneticMaterial | onto.CrystallineMagneticMaterial),
            ]

        class SecondaryPhase(onto.Material, onto.PhaseOfMatter):
            """An additional phase within a magnet, for example soft inclusions
            or triple junctions."""

            prefLabel = en("SecondaryPhase")
            is_a = [
                onto.hasProperty.some(onto.VolumeFraction),
                onto.hasSpatialPart.exactly(
                    1,
                    onto.AmorphousMagneticMaterial | onto.CrystallineMagneticMaterial | onto.NonMagneticMaterial,
                ),
            ]

        class GrainBoundaryPhase(onto.SecondaryPhase):
            """Material separating grains in a microstructure."""

            comment = en(
                "In permanent magnets, the grain boundary phase inhibits \
                the propagation of the magnetic reversal from grain to grain."
            )
            prefLabel = en("GrainBoundaryPhase")
            is_a = [
                onto.hasProperty.some(onto.Thickness),
            ]

        class GranularMicrostructure(onto.Material):
            """The granular structure of a magnetic materials."""

            prefLabel = en("GranularMicrostructure")
            is_a = [
                onto.hasSpatialPart.exactly(1, onto.MainMagneticPhase),
                onto.hasSpatialPart.min(0, onto.SecondaryPhase),
                onto.hasSpatialPart.min(0, onto.GrainBoundaryPhase),
            ]

        class Magnet(onto.FunctionalMaterial):
            """Piece of matter made of one or more magnetic materials."""

            prefLabel = en("Magnet")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q11421")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnet")
            IECEntry = pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=151-14-06")
            is_a = [
                onto.hasProperty.min(0, onto.MaterialsProcessing),
                onto.hasProperty.min(0, onto.WorkpieceForming),
                onto.hasSpatialPart.min(0, onto.GranularMicrostructure),
                onto.hasProperty.exactly(1, onto.ExtrinsicMagneticProperties),
                onto.hasProperty.min(0, onto.XrayDiffractionData),
            ]

        class BulkMagnet(onto.Magnet, onto.MaterialBySize):
            """Piece of matter made of one or more magnetic material."""

            prefLabel = en("BulkMagnet")
            is_a = [
                onto.hasProperty.exactly(1, onto.SampleGeometry),
                onto.hasProperty.exactly(1, onto.ShapeAnisotropy),
                onto.hasProperty.exactly(1, onto.DemagnetizingFactor),
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

        class SpacerLayer(onto.Material):
            """Nonmagnetic thin film materials."""

            prefLabel = en("SpacerLayer")
            is_a = [
                Not(onto.MagneticMaterial),
                onto.hasProperty.exactly(1, onto.ChemicalComposition),
                onto.hasProperty.some(onto.Thickness),
            ]

        class StackingSequence(onto.NominalProperty):
            """Sequence of layers in a multilayer stack."""

            prefLabel = en("StackingSequence")
            is_a = [onto.hasStringValue.some(onto.String)]

        class MultilayerMagnet(onto.SpatialTiling, onto.Magnet):
            """Piece of matter made of stacked layers of one or more magnetic
            materials."""

            prefLabel = en("MultilayerMagnet")
            is_a = [
                onto.hasSpatialTile.some(onto.ThinFilmMagnet),
                onto.hasSpatialTile.min(0, onto.SpacerLayer),
                onto.hasProperty.exactly(1, onto.SampleGeometry),
                onto.hasProperty.exactly(1, onto.StackingSequence),
                onto.hasProperty.min(0, onto.Magnetoresistance),
            ]
