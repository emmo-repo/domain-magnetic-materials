"""Entities related to crystal structure."""

from util import en, pl


def add_crystal_structure_entities(onto):
    """Define entities related to crystal structure."""
    with onto:

        class SpaceGroup(onto.NominalProperty):
            """A spacegroup is the symmetry group of all symmetry operations
            that apply to a crystal structure.

            The complete symmetry of a crystal, including the Bravais lattice and
            any translational symmetry elements, is given by one of the 240 space
            groups.

            A space group is identified by its Hermann-Mauguin symbol or space
            group number (and setting) in the International tables of
            Crystallography."""

            prefLabel = en("SpaceGroup")
            is_a = [onto.hasStringValue.some(onto.String)]
            wikidataReference = pl("https://www.wikidata.org/wiki/Q899033")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Space_group")

        class LatticeConstantA(onto.Length):
            """The length of lattice vectors `a`, where lattice vectors
            `a`, `b` and `c` define the unit cell."""

            prefLabel = en("LatticeConstantA")
            altLabel = en("LatticeParameterA")
            IECEntry = pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=561-07-13")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q625641")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Lattice_constant")

        class LatticeConstantB(onto.Length):
            """The length of lattice vectors `b`, where lattice vectors `a`, `b`
            and `c` define the unit cell."""

            prefLabel = en("LatticeConstantB")
            altLabel = en("LatticeParameterB")
            IECEntry = pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=561-07-13")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q625641")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Lattice_constant")

        class LatticeConstantC(onto.Length):
            """The length of lattice vectors `c`, where lattice vectors `a`, `b`
            and `c` define the unit cell."""

            prefLabel = en("LatticeConstantC")
            altLabel = en("LatticeParameterC")
            IECEntry = pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=561-07-13")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q625641")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Lattice_constant")

        class LatticeConstantAlpha(onto.Angle):
            """The angle between lattice vectors `b` and `c`, where lattice
            vectors `a`, `b` and `c` define the unit cell."""

            prefLabel = en("LatticeConstantAlpha")
            altLabel = en("LatticeParameterAlpha")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q625641")

        class LatticeConstantBeta(onto.Angle):
            """The angle between lattice vectors `a` and `c`, where lattice
            vectors `a`, `b` and `c` define the unit cell."""

            prefLabel = en("LatticeConstantBeta")
            altLabel = en("LatticeParameterBeta")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q625641")

        class LatticeConstantGamma(onto.Angle):
            """The angle between lattice vectors `a` and `b`, where lattice
            vectors `a`, `b` and `c` define the unit cell."""

            prefLabel = en("LatticeConstantGamma")
            altLabel = en("LatticeParameterGamma")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q625641")

        class CellVolume(onto.Volume):
            """Volume of the unit cell."""

            prefLabel = en("CellVolume")
            altLabel = en("UnitCellVolume")

        class CrystalStructure(onto.Property):
            """Description of ordered arrangement of atoms."""

            prefLabel = en("CrystalStructure")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q895901")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Crystal_structure")
            is_a = [
                onto.hasProperty.exactly(1, SpaceGroup),
                onto.hasProperty.exactly(1, LatticeConstantA),
                onto.hasProperty.exactly(1, LatticeConstantB),
                onto.hasProperty.exactly(1, LatticeConstantC),
                onto.hasProperty.exactly(1, LatticeConstantAlpha),
                onto.hasProperty.exactly(1, LatticeConstantBeta),
                onto.hasProperty.exactly(1, LatticeConstantGamma),
                onto.hasProperty.exactly(1, CellVolume),
            ]
