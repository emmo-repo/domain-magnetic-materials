"""Internal and magnetic fields."""

from util import en, enGB, pl


def add_magnetic_fields_entities(onto):
    """Add internal and external magnetic fields entities."""
    with onto:

        class ExternalMagneticField(onto.ElectromagneticQuantity):
            """The external field H′, acting on a sample that is produced by
            electric currents or the stray field of magnets outside the sample
            volume, is often called the applied field."""

            prefLabel = en("ExternalMagneticField")
            altLabel = [
                en("AppliedMagneticField"),
                pl("H'"),
            ]
            is_a = [onto.hasMeasurementUnit.some(onto.MagneticFieldStrengthUnit)]

        class DemagnetizingField(onto.ElectromagneticQuantity):
            """The magnetic field produced by the magnetization distribution
            of the sample itself."""

            prefLabel = en("DemagnetizingField")
            altLabel = [
                enGB("DemagnetisingField"),
                pl("Hd"),
            ]
            wikidataReference = pl("https://www.wikidata.org/wiki/Q5255001")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Demagnetizing_field")
            is_a = [onto.hasMeasurementUnit.some(onto.MagneticFieldStrengthUnit)]

        class InternalMagneticField(onto.ElectromagneticQuantity):
            """The internal field in the sample in the continuous medium
            approximation is the sum of the external field H′ and the
            demagnetizing field Hd."""

            prefLabel = en("InternalMagneticField")
            altLabel = pl("H")
            is_a = [onto.hasMeasurementUnit.some(onto.MagneticFieldStrengthUnit)]
