"""Entities related to intrinsic magnetic properties.

- Magnetization
- Anisotropy
- Exchange
"""

from util import add_altLabel, en, enGB, enUS, pl


def add_intrinsic_magnetic_properties_entities(onto):
    """Add entities related to magnetic properties."""
    with onto:
        add_altLabel(onto.Magnetization, enUS("VolumeMagnetization"))
        add_altLabel(onto.Magnetization, enGB("VolumeMagnetisation"))
        add_altLabel(onto.Magnetization, enGB("Magnetisation"))

        class MassMagnetizationUnit(onto.SIDimensionalUnit):
            """Class of units of the magnetization per unit mass.
            Defined using SI base units."""

            prefLabel = en("MassMagnetizationUnit")
            altLabel = [
                enGB("MassMagnetisationUnit"),
                enUS("SpecificMagnetizationUnit"),
                enGB("SpecificMagnetisationUnit"),
            ]
            is_a = [onto.hasDimensionString.value("T0 L+2 M-1 I+1 Θ0 N0 J0")]

        class AmpereSquareMeterPerKilogram(onto.MassMagnetizationUnit):
            """Unit of the magnetic moment per unit mass: Am²/kg."""

            prefLabel = en("AmpereSquareMeterPerKilogram")
            altLabel = [
                enGB("AmpereSquareMetrePerKilogram"),
            ]
            unitSymbol = en("A⋅m²/kg")
            ucumCode = en("A.m2.kg-1")

        class MagneticMomentPerUnitMass(onto.ElectromagneticQuantity):
            """Magnetic moment per unit mass, sigma."""

            comment = en("The magnetization is obtained by multiplying sigma with the density")
            prefLabel = en("MagneticMomentPerUnitMass")
            altLabel = [
                en("SpecificMagneticMoment"),
                enUS("MassMagnetization"),
                enGB("MassMagnetisation"),
                pl("sigma"),
            ]

            is_a = [onto.hasMeasurementUnit.some(onto.MassMagnetizationUnit)]

        class SpontaneousMagnetization(onto.ElectromagneticQuantity):
            """The spontaneous magnetization, Ms, of a ferromagnet is the result
            of alignment of the magnetic moments of individual atoms. Ms exists
            within a domain of a ferromagnet."""

            prefLabel = en("SpontaneousMagnetization")
            altLabel = [
                enGB("SpontaneousMagnetisation"),
                pl("Ms"),
            ]
            is_a = [onto.hasMeasurementUnit.some(onto.MagneticFieldStrengthUnit)]
            IECEntry = pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=221-02-41")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Spontaneous_magnetization")

        class SpontaneousMagneticPolarization(onto.ElectromagneticQuantity):
            """The spontaneous magnetic polarization, Js, of a ferromagnet is the
            result of alignment of the magnetic moments of  individual atoms.
            Js exists within a domain of a ferromagnet."""

            prefLabel = en("SpontaneousMagneticPolarization")
            altLabel = [
                enGB("SpontaneousMagneticPolarisation"),
                pl("Js"),
            ]
            is_a = [onto.hasMeasurementUnit.some(onto.MagneticFluxDensityUnit)]

        class MagneticAnisotropy(onto.Property):
            """Magnetic anisotropy means that the magnetic properties depend on
            the direction in which they are measured."""

            prefLabel = en("MagneticAnisotropy")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetic_anisotropy")
            IECEntry = pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=221-01-08")

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

        class ShapeAnisotropyConstant(onto.EnergyDensity):
            """The energy density of a small particle given by

            K1sh = (mu_0/4)(1-3D)Ms²

            where mu_0 is the vacuum magnetic permeability and D is the
            DemagnetizingFactor and Ms is the spontaneous magnetization.
            """

            prefLabel = en("ShapeAnisotropyConstant")
            altLabel = pl("K1sh")

        class ShapeAnisotropy(onto.MagneticAnisotropy):
            """The difference in magnetostatic energy when an elongated particle
            is magnetized along its short and long axis.
            """

            comment = en(
                "Shape anisotropy is restricted to small particles, where "
                "the inter-atomic exchange ensures a uniform  magnetization."
            )
            prefLabel = en("ShapeAnisotropy")
            is_a = [
                onto.hasProperty.exactly(1, DemagnetizingFactor),
                onto.hasProperty.exactly(1, ShapeAnisotropyConstant),
            ]

        class MagnetocrystallineAnisotropyEnergy(onto.EnergyDensity):
            """The magnetocrystalline anisotropy energy density."""

            prefLabel = en("MagnetocrystallineAnisotropyEnergy")
            altLabel = pl("MAE")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocrystalline_anisotropy")

        class AnisotropyField(onto.MagneticFieldStrength):
            """The anisotropy field Ha is defined as the field needed to
            saturate the magnetization of a uniaxial crystal in a hard direction.
            Ha = 2 Ku/Js
            """

            comment = en(
                "Beware of taking the idea of anisotropy field too literally. "
                "Except at small angles, the energy variation in a field is not the same as the leading "
                "term in the anisotropy. A magnetic field defines an easy direction, not an easy axis."
            )
            prefLabel = en("AnisotropyField")
            altLabel = pl("Ha")

        class UniaxialAnisotropyConstant(onto.EnergyDensity):
            """The change of energy with angle of the magnetization from
            the preferred direction is expressed with the
            uniaxial anisotropy constant Ea = Ku sin²(theta)."""

            prefLabel = en("UniaxialAnisotropyConstant")
            altLabel = pl("Ku")

        class UniaxialMagneticAnisotropy(onto.MagneticAnisotropy):
            """The anisotropy can be described as uniaxial when the anisotropy
            energy E depends on only a single angle, the angle between the
            magnetization vector and the easy direction of magnetization.
            """

            prefLabel = en("UniaxialMagneticAnisotropy")
            is_a = [
                onto.hasProperty.exactly(1, AnisotropyField),
                onto.hasProperty.exactly(1, UniaxialAnisotropyConstant),
            ]

        class InducedMagneticAnisotropy(onto.UniaxialMagneticAnisotropy):
            """Uniaxial anisotropy induced by annealing in a magnetic field or
            by applying a stress."""

            prefLabel = en("InducedMagneticAnisotropy")

        class MagnetocrystallineAnisotropyConstantK1(onto.EnergyDensity):
            """The magnetocrystalline constant K1 for tetragonal or
            hexagonal crystals."""

            comment = pl(
                "Ea = K1 sin^2(phi) + K2 sin^4(phi) where Ea is the is the anisotropy energy density "
                "and phi is the angle of the magnetization with respect to the c-axis of the crystal."
            )
            prefLabel = en("MagnetocrystallineAnisotropyConstantK1")
            altLabel = pl("K1")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocrystalline_anisotropy")

        class MagnetocrystallineAnisotropyConstantK2(onto.EnergyDensity):
            """The magnetocrystalline constant K2 for tetragonal or
            hexagonal crystals."""

            comment = pl(
                "Ea = K1 sin^2(phi) + K2 sin^4(phi) where Ea is the is the anisotropy energy density "
                "and phi is the angle of the magnetization with respect to the c-axis of the crystal."
            )
            prefLabel = en("MagnetocrystallineAnisotropyConstantK2")
            altLabel = pl("K2")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocrystalline_anisotropy")

        class MagnetocrystallineAnisotropyConstantK1c(onto.EnergyDensity):
            """The magnetocrystalline constant K1c for cubic crystals."""

            comment = pl(
                "Ea = K1c(a1²a2²+a2²a3²+a1²a3²)+K2c(a1²a2²a3²) where Ea is the anisotropy energy "
                "density and a1,a2,a3 are the direction cosines of the magnetization"
            )
            prefLabel = en("MagnetocrystallineAnisotropyConstantK1c")
            altLabel = pl("K1c")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocrystalline_anisotropy")

        class MagnetocrystallineAnisotropyConstantK2c(onto.EnergyDensity):
            """The magnetocrystalline constant K2c for cubic crystals."""

            comment = pl(
                "Ea = K1c(a1²a2²+a2²a3²+a1²a3²)+K2c(a1²a2²a3²) where Ea is the anisotropy "
                "energy density and a1,a2,a3 are the direction cosines of the magnetization"
            )
            prefLabel = en("MagnetocrystallineAnisotropyConstantK2c")
            altLabel = pl("K2c")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocrystalline_anisotropy")

        class UniaxialMagnetocrystallineAnisotropy(onto.UniaxialMagneticAnisotropy):
            """The uniaxial anisotropy depends on only a single angle, the angle
            magnetization vector and the c axis.
            """

            prefLabel = en("UniaxialMagnetocrystallineAnisotropy")
            is_a = [
                onto.hasProperty.exactly(1, MagnetocrystallineAnisotropyConstantK1),
                onto.hasProperty.min(0, MagnetocrystallineAnisotropyConstantK2),
            ]

        class CubicMagnetocrystallineAnisotropy(onto.MagneticAnisotropy):
            """Cubic crystals anisotropy."""

            prefLabel = en("CubicMagnetocrystallineAnisotropy")
            is_a = [
                onto.hasProperty.exactly(1, onto.MagnetocrystallineAnisotropyConstantK1c),
                onto.hasProperty.min(0, onto.MagnetocrystallineAnisotropyConstantK2c),
            ]

        class MagnetocrystallineAnisotropy(onto.Property):
            """Magnetocrystalline anisotropy is an intrinsic property. The
            magnetisation process is different when the field is applied along
            different crystallographic directions, and the anisotropy reflects
            the crystal symmetry. Its origin is in the crystal-field interaction
            and spin-orbit coupling, or else the interatomic dipole–dipole
            interaction."""

            prefLabel = en("MagnetocrystallineAnisotropy")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q6731660")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetocrystalline_anisotropy")
            is_a = [
                onto.hasProperty.exactly(
                    1,
                    onto.UniaxialMagnetocrystallineAnisotropy | onto.CubicMagnetocrystallineAnisotropy,
                )
            ]

        class ExchangeStiffnessConstant(onto.LineEnergy):
            """Exchange constant, A, in the continuum theory of micromagnetism.

            The exchange stiffness A is related to the Curie temperature TC:
            A is roughly k_B T_c/(2 a_0), where a_0 is the lattice parameter in
            a simple structure."""

            prefLabel = en("ExchangeStiffnessConstant")
            altLabel = pl("A")

        class IntrinsicMagneticProperties(onto.Property):
            """Intrinsic magnetic properties refer to atomic-scale magnetism and
            depend on the crystal structure."""

            prefLabel = en("IntrinsicMagneticProperties")
            is_a = [
                onto.hasProperty.some(onto.SpontaneousMagnetization),
                onto.hasProperty.some(onto.SpontaneousMagneticPolarization),
                onto.hasProperty.some(onto.MagnetocrystallineAnisotropy),
                onto.hasProperty.some(onto.ExchangeStiffnessConstant),
                onto.hasProperty.some(onto.CurieTemperature | onto.NeelTemperature),
            ]
