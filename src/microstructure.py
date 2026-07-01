"""Microstructure."""

from util import en, pl


def add_microstructure_entities(onto):
    """Add microstructure entities."""
    with onto:

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
