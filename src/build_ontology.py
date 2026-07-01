"""Script for building the ontology.

Default annotation language policy:
- If the prefLabel does not contain regional variants, use @en.
- If the prefLabel contains regional variants, use @enUS for prefLabel
  and include the @enGB variant as altLabel.
- Use English (@en) as default for textual annotations.
- Use plain strings (@pl) for strings containing only symbols or formulas.
- Keep exactly one prefLabel per entity and use altLabel for alternatives,
  consistent with EMMO governance naming conventions.

Reuse by specialization (subclassing) of imported ontology classes.
Define a domain subclass (specialization) of emmo:Material in an ontology
that imports EMMO, e.g. class NonMagneticMaterial(emmo.Material).

https://github.com/emmo-repo/domain-atomistic/blob/master/domain-atomistic.py
was taken as an example while writing this script.
"""

from __future__ import annotations

import argparse
import os
import re
from pathlib import Path
from typing import TYPE_CHECKING

from ontopy import World

from annotation_properties import add_annotation_properties
from characterization_data import add_characterization_data_entities
from crystal_structure import add_crystal_structure_entities
from energy import add_energy_entities
from granular_structure import add_granular_structure_entities
from hysteresis_properties import add_hysteresis_properties_entities
from intrinsic_magnetic_properties import add_intrinsic_magnetic_properties_entities
from local_properties import add_local_properties_entities
from magnetic_fields import add_magnetic_fields_entities
from magnetotransport import add_magnetotransport_entities
from microstructure import add_microstructure_entities
from thermodynamics import add_thermodynamics_entities
from util import en

if TYPE_CHECKING:
    import ontopy.ontology


VERSION = "0.0.6"
MAGMO_IRI = "https://w3id.org/emmo/domain/magnetic-materials"
ROOT_DIR = Path(__file__).parent.parent.resolve()


def define_ontology(annotate_metadata: bool = True, local_imports: bool = False) -> ontopy.ontology.Ontology:
    """Define ontology classes.

    Args:
        annotate_metadata: Whether to fill the ontology metadata.
        local_imports: Use local imports instead of loading online dependencies.
    """
    # Define ontology imports
    world = World()
    if local_imports:
        contributors = world.get_ontology(f"{ROOT_DIR}/contributors.ttl").load()
        dependencies = world.get_ontology(f"{ROOT_DIR}/magnetic-materials-dependencies").load()
    else:
        contributors = world.get_ontology(f"{MAGMO_IRI}/{VERSION}/contributors").load()
        dependencies = world.get_ontology(f"{MAGMO_IRI}/{VERSION}/magnetic-materials-dependencies").load()

    # Create a new ontology with imports
    onto = world.get_ontology(f"{MAGMO_IRI}#")
    onto.imported_ontologies.append(contributors)
    onto.imported_ontologies.append(dependencies)

    # Add new classes and object/data properties needed by the use case.
    # The order is important. Some entities depend on other entities.
    add_annotation_properties(onto)
    add_crystal_structure_entities(onto)
    add_energy_entities(onto)
    add_intrinsic_magnetic_properties_entities(onto)
    add_characterization_data_entities(onto)
    add_granular_structure_entities(onto)
    add_magnetic_fields_entities(onto)
    add_hysteresis_properties_entities(onto)
    add_microstructure_entities(onto)
    add_local_properties_entities(onto)
    add_magnetotransport_entities(onto)
    add_thermodynamics_entities(onto)
    onto.sync_attributes(name_policy="uuid", class_docstring="elucidation", name_prefix="EMMO_")

    # Add metadata
    if annotate_metadata:
        onto.metadata.comment.append(
            "Created within the EU project MaMMoS. Grant number 101135546 (HORIZON-CL4-2023-DIGITAL-EMERGING-01)."
        )

        onto.metadata.abstract.append(
            en(
                "An EMMO-based domain-ontology for magnetic materials. "
                "Created within the EU project MaMMoS. "
                "Grant number 101135546 (HORIZON-CL4-2023-DIGITAL-EMERGING-01). "
                "The Magnetic Materials Ontology is released under the Creative Commons "
                "Attribution 4.0 International license (CC BY 4.0)."
            )
        )

        onto.metadata.title.append(en("Magnetic Materials Ontology (MagMO)"))
        onto.metadata.creator.append(contributors.WilfriedHortschitz)
        onto.metadata.creator.append(contributors.ThomasSchrefl)
        onto.metadata.creator.append(contributors.SantaPile)
        onto.metadata.contributor.append(contributors.WilliamRigaut)
        onto.metadata.contributor.append(contributors.AndreaPetrocchi)
        onto.metadata.contributor.append(contributors.MartinLang)
        onto.metadata.contributor.append(contributors.SamuelHolt)
        onto.metadata.contributor.append(contributors.SwapneelAmitPathak)
        onto.metadata.contributor.append(contributors.HansFangohr)
        onto.metadata.contributor.append(contributors.JonasWinkler)
        onto.metadata.status.append(world.get_ontology("http://purl.org/ontology/bibo/term_status/unstable"))
        onto.metadata.preferredNamespacePrefix.append("magmo")
        onto.metadata.preferredNamespaceUri.append("https://w3id.org/emmo/domain/magnetic-materials")
        onto.metadata.license.append(world.get_ontology("https://creativecommons.org/licenses/by/4.0/legalcode"))
        onto.metadata.publisher.append(world.get_ontology("https://mammos-project.github.io"))
        onto.metadata.versionInfo.append(VERSION)
        onto.metadata.comment.append(
            en("Contacts: Wilfried Hortschitz (DISS-UWK), wilfried.hortschitz@donau-uni.ac.at")
        )

    # Set version of ontology
    onto.set_version(
        version=VERSION,
        version_iri=f"{MAGMO_IRI}/{VERSION}",
        set_priorVersion=False,
    )

    return onto


def save_ontology(onto: ontopy.ontology.Ontology, output_ttl: os.PathLike = "magnetic-materials.ttl") -> None:
    """Save ontology as turtle file.

    Args:
        onto: Ontology object to be saved.
        output_ttl: Path of saved turtle file.
    """
    onto.save(
        output_ttl,
        overwrite=True,
        namespaces={
            "emmo": "https://w3id.org/emmo#",
        },
    )


def apply_fixes(
    input_ttl: os.PathLike = "magnetic-materials.ttl",
    output_ttl: os.PathLike = "magnetic-materials.ttl",
) -> None:
    """Apply fixes to adhere to the best practices.

    As sometimes owlready2 or EMMOntoPy miss the required best practices,
    we have to apply some fixes ourselves.

    Args:
        input_ttl: Path of the ontology to be modified.
        output_ttl: Path to the fixed ontology.
    """
    with open(input_ttl) as f:
        text = f.read()
    text = apply_fix_1(text)
    text = apply_fix_2(text)
    with open(output_ttl, mode="w") as f:
        f.write(text)


def apply_fix_1(text: str) -> str:
    """Apply fix: add `versionIRI` to imports.

    EMMOntoPy writes imports with their base IRI, without version number.
    Issue raised in https://github.com/emmo-repo/EMMOntoPy/issues/1010.
    """
    text = text.replace(f"<{MAGMO_IRI}/contributors>", f"<{MAGMO_IRI}/{VERSION}/contributors>")
    text = text.replace(f"<{MAGMO_IRI}/dependencies>", f"<{MAGMO_IRI}/{VERSION}/dependencies>")
    return text


def apply_fix_2(text: str) -> str:
    """Apply fix: define dcterms:mediator metadata.

    Metadata `dcterms:mediator` is not found when importing the dependencies.
    Issue raised https://github.com/emmo-repo/EMMOntoPy/issues/1003.
    """
    license_line = re.search(r"\n +dcterms:license <.+> ;", text).group()
    post_indent = license_line.find("dcterms:license")
    indent = " " * len(license_line[:post_indent].lstrip(r"\n"))
    text = text.replace(
        license_line,
        license_line + f"\n{indent}dcterms:mediator emmo:EMMC_ASBL ;",
    )
    return text


def main(
    output: os.PathLike,
    annotate_metadata: bool = True,
    local_imports: bool = False,
    skip_fixes: bool = False,
) -> None:
    """Build ontology.

    Args:
        output: Output
        annotate_metadata: Whether to add metadata to the ontology.
        local_imports: Whether to build the ontology by reading local dependencies instead of
            reading them from `https://w3id.org/emmo/domain/magnetic-materials/`.
        skip_fixes: Whether to skip fixes to owlready2 and EMMOntoPy, such as fixes
            to the imports IRIs.
    """
    onto = define_ontology(annotate_metadata=annotate_metadata, local_imports=local_imports)
    save_ontology(onto, output)
    if not skip_fixes:
        apply_fixes()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o",
        "--output",
        default="magnetic-materials.ttl",
        help="path to output ttl file",
    )
    parser.add_argument(
        "--local_imports",
        action="store_true",
        help="build ontology by reading local dependencies",
    )
    parser.add_argument(
        "--skip-fixes",
        action="store_true",
        help="skip ontology fixes such as iri fixes",
    )
    args = parser.parse_args()
    main(
        output=args.output,
        annotate_metadata=True,
        local_imports=args.local_imports,
        skip_fixes=args.skip_fixes,
    )
