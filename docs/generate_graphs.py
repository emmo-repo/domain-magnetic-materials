"""Generate entity graphs for the documentation"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from ontopy import World
from ontopy.graph import OntoGraph, _default_style

if TYPE_CHECKING:
    import ontopy.ontology
    import os


def main():
    """Generate all entity graphs for the MaMMoS overview."""
    ontology_ttl = Path(__file__).parent.parent / "magnetic-materials.ttl"
    onto = World().get_ontology(ontology_ttl).load()

    graphs_dir = Path(__file__).parent / "graphs"
    graphs_dir.mkdir(exist_ok=True)

    generate_graph_magnet(onto, out_dir=graphs_dir)
    generate_graph_bulk_magnet(onto, out_dir=graphs_dir)
    generate_graph_granular_microstructure(onto, out_dir=graphs_dir)
    generate_graph_magnetic_material(onto, out_dir=graphs_dir)
    generate_graph_crystalline_magnetic_material(onto, out_dir=graphs_dir)
    generate_graph_intrinsic_magnetic_properties(onto, out_dir=graphs_dir)
    generate_graph_extrinsic_magnetic_properties(onto, out_dir=graphs_dir)


def generate_graph(
    onto: ontopy.ontology.Ontology,
    root: str,
    out_name: str,
    out_dir: os.PathLike = ".",
    leaves: list[str] = [],
    relations: list[str] = ["isA"],
    parents: int = 1,
    fmt: str = "svg"
) -> None:
    """Generate entity graph.

    This is the utility function that contains the default graph configuration.
    Each entity of interest will refine the parameters further and call this
    function to create and save the graph.

    Args:
        onto: Loaded ontology.
        root: Graph root. Main entity to represent.
            It will be highlighted by a bold contour.
        leaves: Additional highlighted entities.
        out_name: Name of the output graph file.
        out_dir: Directory where to save the output graph file
        relations: List of relations to consider when finding
            entities to add to the graph.
        parents: Level of parents to add to the graph.
        fmt: Format of output graph file.
    """
    style = _default_style
    style["graph"]["rankdir"] = "LR"
    graph = OntoGraph(
        onto,
        root=root,
        leaves=leaves,
        excluded_nodes=None,
        relations=relations,
        parents=parents,
        edgelabels=True,
        addnodes=True,
        addconstructs=False,
        style=style,
    )
    graph.add_legend()
    graph.save(out_dir / out_name, fmt=fmt)


def generate_graph_magnet(
    onto: ontopy.ontology.Ontology,
    out_dir: os.PathLike = ".",
) -> None:
    """Generate entity graph of `Magnet`.

    Args:
        onto: Loaded ontology.
        out_dir: Directory where to save the graph.
    """
    generate_graph(
        onto,
        root="Magnet",
        out_name="magnet",
        leaves=["BulkMagnet"],
        out_dir=out_dir,
        relations=["isA", "hasSpatialPart", "hasSpatialTile"],
        parents=0,
    )


def generate_graph_bulk_magnet(
    onto: ontopy.ontology.Ontology,
    out_dir: os.PathLike = ".",
    fmt: str = "svg"
) -> None:
    """Generate entity graph of `BulkMagnet`."""
    generate_graph(
        onto,
        root="BulkMagnet",
        out_name="bulk_magnet",
        leaves=["GranularMicrostructure"],
        out_dir=out_dir,
        relations=["isA", "hasMeasurementUnit", "hasProperty", "hasSpatialPart"],
    )


def generate_graph_granular_microstructure(
    onto: ontopy.ontology.Ontology,
    out_dir: os.PathLike = ".",
) -> None:
    """Generate entity graph of `GranularMicrostructure`."""
    generate_graph(
        onto,
        root="GranularMicrostructure",
        out_name="granular_microstructure",
        out_dir=out_dir,
        relations=["isA", "hasSpatialPart"],
    )


def generate_graph_magnetic_material(
    onto: ontopy.ontology.Ontology,
    out_dir: os.PathLike = ".",
) -> None:
    """Generate entity graph of `MagneticMaterial`."""
    generate_graph(
        onto,
        root="MagneticMaterial",
        out_name="magnetic_material",
        leaves=["CrystallineMagneticMaterial"],
        out_dir=out_dir,
        relations=["isA", "hasProperty"],
        parents=0,
    )


def generate_graph_crystalline_magnetic_material(
    onto: ontopy.ontology.Ontology,
    out_dir: os.PathLike = ".",
) -> None:
    """Generate entity graph of `CrystallineMagneticMaterial`."""
    generate_graph(
        onto,
        root="CrystallineMagneticMaterial",
        out_name="crystalline_magnetic_material",
        out_dir=out_dir,
        relations=["isA", "hasSpatialPart", "hasProperty"],
    )


def generate_graph_intrinsic_magnetic_properties(
    onto: ontopy.ontology.Ontology,
    out_dir: os.PathLike = ".",
) -> None:
    """Generate entity graph of `IntrinsicMagneticProperties`."""
    generate_graph(
        onto,
        root="IntrinsicMagneticProperties",
        out_name="intrinsic_magnetic_properties",
        out_dir=out_dir,
        relations=["isA", "hasMeasurementUnit", "hasProperty"],
    )


def generate_graph_extrinsic_magnetic_properties(
    onto: ontopy.ontology.Ontology,
    out_dir: os.PathLike = ".",
) -> None:
    """Generate entity graph of `ExtrinsicMagneticProperties`."""
    generate_graph(
        onto,
        root="ExtrinsicMagneticProperties",
        out_name="extrinsic_magnetic_properties",
        out_dir=out_dir,
        relations=["isA", "hasMeasurementUnit", "hasProperty", "hasSpatialPart"],
    )


if __name__ == "__main__":
    main()
