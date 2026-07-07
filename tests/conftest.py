"""Common configuration for tests."""

from pathlib import Path

import pytest
import tomllib
import yaml


@pytest.fixture(scope="session")
def magmo_iri():
    """Read MagMO IRI from `.ontokit_conf.yml`."""
    with open(Path(__file__).parent.parent / ".ontokit_conf.yml", "rb") as f:
        return yaml.safe_load(f)["ONTOLOGY_IRI"]


@pytest.fixture(scope="session")
def magmo_version():
    """Read version string from pixi.toml."""
    with open(Path(__file__).parent.parent / "pixi.toml", "rb") as f:
        return tomllib.load(f)["workspace"]["version"]
