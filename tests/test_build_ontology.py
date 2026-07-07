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


def test_versions(generated_ontology, committed_ontology, magmo_iri, magmo_version):
    """Test that the two ontologies have the same version and IRI information."""
    assert generated_ontology.get_version() == magmo_version
    assert generated_ontology.get_iri() == f"{magmo_iri}"
    assert generated_ontology.get_version(as_iri=True) == f"{magmo_iri}/{magmo_version}"
    assert committed_ontology.get_version() == magmo_version
    assert committed_ontology.get_iri() == f"{magmo_iri}"
    assert committed_ontology.get_version(as_iri=True) == f"{magmo_iri}/{magmo_version}"


def test_same_classes_iris(generated_ontology, committed_ontology):
    assert set(entity.iri for entity in generated_ontology.classes()) == set(
        entity.iri for entity in committed_ontology.classes()
    )


@pytest.mark.parametrize("field", ["prefLabel", "altLabel", "elucidation"])
def test_same_field(generated_ontology, committed_ontology, field, subtests):
    for entity in generated_ontology.classes(imported=True):
        if entity.prefLabel:
            msg = f"{entity.prefLabel[0]} ({entity.name})"
        else:
            msg = f"({entity.name})"
        with subtests.test(msg=msg):
            assert _compare(entity[field], committed_ontology[entity.iri][field])


def test_same_comments(generated_ontology, committed_ontology, subtests):
    """Test that entities have the same comment.

    We cannot integrate this test in `test_same_field` because entity["comment"] does
    not work in same way as `prefLabel`, `altLabel`, and `elucidation`.
    """
    for entity in generated_ontology.classes(imported=True):
        if entity.prefLabel:
            msg = f"{entity.prefLabel[0]} ({entity.name})"
        else:
            msg = f"({entity.name})"
        with subtests.test(msg=msg):
            assert _compare(entity.comment, committed_ontology[entity.iri].comment)
