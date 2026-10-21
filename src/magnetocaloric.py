"""Magnetocaloric quantities (proof-of-concept placeholder).

This module currently declares a single placeholder class used only to
prove the end-to-end integration between the MagMO build pipeline,
``mammos-entity`` (loaded from the vendored TTL), and ``to-nomad``.

Phase 1 will replace this placeholder with the full set of 13 MCE
quantity classes listed in ``Core ontology quantities for MCE.md``.
"""

from util import en, pl


def add_magnetocaloric_entities(onto):
    """Register magnetocaloric proof-of-concept entities with the ontology."""
    with onto:
        class MagnetocaloricEffectPlaceholder(onto.ElectromagneticQuantity):
            """Placeholder MCE quantity used to prove end-to-end integration.

            Shape mirrors :class:`SpontaneousMagnetization` so that both
            the parent (``ElectromagneticQuantity``) and the expected unit
            (``MagneticFieldStrengthUnit``, i.e. A/m) are known-good in
            ``mammos-entity`` 0.14.0.
            """
            prefLabel = en("MagnetocaloricEffectPlaceholder")
            altLabel = [pl("MCEPlaceholder")]
            is_a = [onto.hasMeasurementUnit.some(onto.MagneticFieldStrengthUnit)]
