"""Annotation properties add information to individial entities.

- IECEntry is the relevant entry on Electropedia defined by the
  International Electrotechnical Commission (IEC), if available.
- wikipediaReference is the relevant entry on Wikipedia, if available.
- wikidataReference is the relevant entry on Wikidata, if available.
"""

from owlready2 import AnnotationProperty


def add_annotation_properties(onto):
    """Add additional annotation properties not found in EMMO."""
    with onto:

        class IECEntry(AnnotationProperty):
            pass

        class wikipediaReference(AnnotationProperty):
            pass

        class wikidataReference(AnnotationProperty):
            pass
