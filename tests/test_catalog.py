"""Test coherence of version numbers in all files."""

import xml.etree.ElementTree as ET


def test_catalog_xml(magmo_iri, magmo_version):
    """Test `catalog-v001.xml`.

    This file should be compliant with the practices described in
    https://github.com/emmo-repo/.github/wiki/DomainOntologiesBestPractices.
    """
    tree = ET.parse("catalog-v001.xml")
    root = tree.getroot()
    assert root.tag == "{urn:oasis:names:tc:entity:xmlns:xml:catalog}catalog"
    assert root.attrib == {"prefer": "public"}
    assert len(root) == 1  # the root should only have one child
    group = root[0]
    assert group.tag == "{urn:oasis:names:tc:entity:xmlns:xml:catalog}group"
    assert group.attrib == {
        "id": "Folder Repository, directory=, recursive=true, Auto-Update=false, version=2",
        "prefer": "public",
        "{http://www.w3.org/XML/1998/namespace}base": "",
    }
    assert len(group) == 3
    assert group[0].get("uri") == "magnetic-materials.ttl"
    assert group[0].get("name") == f"{magmo_iri}/{magmo_version}/magnetic-materials"
    assert group[1].get("uri") == "magnetic-materials-dependencies.ttl"
    assert group[1].get("name") == f"{magmo_iri}/{magmo_version}/dependencies"
    assert group[2].get("uri") == "contributors.ttl"
    assert group[2].get("name") == f"{magmo_iri}/{magmo_version}/contributors"
