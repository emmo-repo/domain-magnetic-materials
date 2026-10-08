# Overview

The MaMMoS magnetic materials ontology is a domain ontology which uses EMMO as top and middle level ontology. The magnetic material ontology reflects the hierarchical structure of the magnet. It reveals its physical parts at different length scales.

## Magnet

A magnet is functionally defined material. Possible subclasses of a magnet are bulk magnet, thin film magnet, or multilayer magnet. A magnet may have a granular microstructure.

![Magnet entity graph](graphs/magnet.svg)

## Bulk Magnet

A bulk magnet is a piece of matter made of one or more magnetic material.

![Magnet entity graph](graphs/bulk_magnet.svg)

## Granular Microstructure

The spatial parts of the granular microstructure are the *main magnetic phase*, the *grain boundary phase*, and *secondary phase*.

The granular microstructure consists of a *main magnetic phase*, possible *grain boundary phases*, and *secondary phases*.

![Granular microstructure entity graph](graphs/granular_microstructure.svg)

## Magnetic material

The main magnetic phase is a *magnetic material*. A magnetic material has
*intrinsic magnetic properties* and a *chemical composition*. A magnetic material can be amorphous
or crystalline.

![Magnetic material entity graph](graphs/magnetic_material.svg)

## Crystalline magnetic material

A *crystalline magnetic material* is a *granular structure*. Properties of the granular structure are a *crystal structure* and a *grain size distribution*. *X-ray diffraction data* may have been measured.

![Crystalline magnetic material entity graph](graphs/crystalline_magnetic_material.svg)

## Intrinsic magnetic properties

The *intrinsic magnetic properties* depend on the chemical composition and the crystal structure. They are a property of the *magnetic material*.

![Intrinsic magnetic properties entity graph](graphs/intrinsic_magnetic_properties.svg)

## Extrinsic magnetic properties

Whereas the intrinsic magnetic properties are a property of a magnetic material, the *extrinsic magnetic properties* depend on the microstructure and shape of the magnet. They are a property of the magnet. An important subset of the extrinsic magnetic properties are the *magnetic hysteresis properties*.

![Extrinsic magnetic properties entity graph](graphs/extrinsic_magnetic_properties.svg)
