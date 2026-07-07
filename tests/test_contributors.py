"""Test contributors ttl file."""

from ontopy import World


def test_contributors_ttl(magmo_iri, magmo_version):
    """Test content of `contributors.ttl`."""
    contributors = World().get_ontology("contributors.ttl").load()
    assert contributors.get_version() == magmo_version
    assert contributors.get_iri() == f"{magmo_iri}/contributors"
    assert contributors.get_version(as_iri=True) == f"{magmo_iri}/{magmo_version}/contributors"
