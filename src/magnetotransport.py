"""Magnetotransport."""

from owlready2 import Not

from util import en, pl


def add_magnetotransport_entities(onto):
    """Add magnetotransport entities."""
    with onto:

        class Magnetoresistance(onto.RatioQuantity):
            """Change of the resistivity of a substance due to an applied
            magnetic field.

            Magnetoresistance can be defined as MR = [ϱ(B)-ϱ(0)]/ϱ(0).
            """

            prefLabel = en("Magnetoresistance")
            altLabel = pl("MR")
            wikidataReference = pl("https://www.wikidata.org/wiki/Q58347")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Magnetoresistance")
            IECEntry = pl("https://www.electropedia.org/iev/iev.nsf/display?openform&ievref=121-12-83")
            is_a = [
                onto.hasMeasurementUnit.some(onto.DimensionlessUnit),
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
