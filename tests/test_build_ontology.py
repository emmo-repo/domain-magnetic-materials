"""Test that generated ontology is equivalent to the committed one."""

from pathlib import Path

import pytest
from ontopy import World


def _compare(iter_1, iter_2):
    """Compare two iterables by strings.

    In most of these tests we need to compare set of strings generated
    by two iterables `iter_1` and `iter_2`.
    """
    return set(str(obj) for obj in iter_1) == set(str(obj) for obj in iter_2)


def test_existence_turtle_files():
    """Test that the two ontologies exist.

    `generated` is the ontology generated from `build_ontology.py`.
    `magnetic-materials.ttl` is the committed ontology.
    """
    assert Path("generated.ttl").exists()
    assert Path("magnetic-materials.ttl").exists()


@pytest.fixture(scope="session")
def generated_ontology():
    return World().get_ontology("generated.ttl").load()


@pytest.fixture(scope="session")
def committed_ontology():
    return World().get_ontology("magnetic-materials.ttl").load()


# Explanation for accessing 'metadata.type' in the two metadata fixtures
#
# When I load an ontology, the first time I run `magmo.metadata.type` I get
# back a list of strings: `['http://www.w3.org/2002/07/owl#Ontology']`.
# From the second time, `magmo.metadata.type` returns a list of
# Things: `[owl.Ontology]`.
# If I run `magmo.metadata` and then `magmo.metadata.type`, I get a list of
# things.
# If I assign `md = magmo.metadata`:
# - `md.type` is a list of strings
# - `magmo.metadata.type` is a list of strings.
# So what we are assuming is that something is called either when calling the
# `type` field directly or during the `str` and `repr` of magmo.metadata
# (which is a `owlready2.namespace.Metadata` object) that makes owlready2 load
# the Things.
# Weirdly enough, the Thing is returned after the first call (even directly
# `magmo.metadata.type[0]` returns at first the string
# `'http://www.w3.org/2002/07/owl#Ontology'` and from the second time the
# Thing).


@pytest.fixture
def generated_metadata(generated_ontology):
    metadata = generated_ontology.metadata
    _ = metadata.type
    return metadata


@pytest.fixture
def committed_metadata(committed_ontology):
    metadata = committed_ontology.metadata
    _ = metadata.type
    return metadata


def test_metadata(generated_metadata, committed_metadata, subtests):
    """Test that the metadata between the two ontologies matches.

    First we test that the metadata object from both ontologies has the same keys.
    Then we iterate for each key and test that the stored information matches.
    """
    assert set(str(k) for k in generated_metadata.keys()) == set(str(k) for k in committed_metadata.keys())
    for k in generated_metadata.keys():
        with subtests.test(msg=k):
            assert _compare(generated_metadata[k], committed_metadata[k])


def test_same_classes_iris(generated_ontology, committed_ontology):
    assert set(entity.iri for entity in generated_ontology.classes()) == set(entity.iri for entity in committed_ontology.classes())


def test_annotations(generated_ontology, committed_ontology, subtests):
    """Test that the annotations of all entity classes match between the different ontologies.

    This test checks all annotations at the same time:
    - IECEntry
    - altLabel
    - comment
    - elucidation
    - prefLabel
    - wikidataReference
    - wikipediaReference

    Not all entities classes have all of the annotations defined.

    For each entity we first check that it contains the same annotation fields
    in the different ontologies. Then, we check the content of the annotations
    to make sure they match.
    """
    for entity in generated_ontology.classes(imported=True):
        gen_anns = entity.get_annotations()
        com_anns = committed_ontology[entity.iri].get_annotations()
        assert gen_anns.keys() == com_anns.keys()

        if entity.prefLabel:
            msg = f"{entity.prefLabel[0]} ({entity.name})"
        else:
            msg = f"({entity.name})"
        for field, annotation in gen_anns.items():
            with subtests.test(msg=f"{msg}: {field}"):
                assert _compare(annotation, com_anns[field])


def test_annotation_properties(generated_ontology, committed_ontology, subtests):
    """Test all additional annotation properties.

    While in the above tests we test certain fields of entity classes,
    here we check iris and annotations of the annotation properties themselves.

    In particular, we only test the annotation properties we define,
    such as `IECEntry`, `wikidataReference`, and `wikipediaReference`.
    """
    gen_iri_set = set(prop.iri for prop in generated_ontology.annotation_properties())
    com_iri_set = set(prop.iri for prop in committed_ontology.annotation_properties())
    assert gen_iri_set == com_iri_set

    for prop in generated_ontology.annotation_properties():
        gen_prop_anns = prop.get_annotations()
        com_prop_anns = committed_ontology[prop.iri].get_annotations()
        assert gen_prop_anns.keys() == com_prop_anns.keys()

        if prop.prefLabel:
            msg = f"{prop.prefLabel[0]} ({prop.name})"
        else:
            msg = f"({prop.name})"
        with subtests.test(msg=f"{msg}: iri"):
            assert prop.iri == committed_ontology[prop.iri].iri
        for field, annotation in gen_prop_anns.items():
            with subtests.test(msg=f"{msg}: {field}"):
                assert _compare(annotation, com_prop_anns[field])
