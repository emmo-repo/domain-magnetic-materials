"""Test dependencies ttl file."""

from ontopy import World


def test_dependencies_ttl(magmo_iri, magmo_version):
    """Test content of `magnetic-materials-dependencies.ttl`."""
    dependencies = World().get_ontology("magnetic-materials-dependencies.ttl").load()
    assert dependencies.get_version() == magmo_version
    assert dependencies.get_iri() == f"{magmo_iri}/dependencies"
    assert dependencies.get_version(as_iri=True) == f"{magmo_iri}/{magmo_version}/dependencies"
