"""Entities related to energy terms.

Reused/adapted concepts from domain-crystallography (grouped for provenance):
- Space group and unit-cell descriptors:
  SpaceGroup, LatticeConstantA, LatticeConstantB, LatticeConstantC,
  LatticeConstantAlpha, LatticeConstantBeta, LatticeConstantGamma,
  CellVolume, CrystalStructure.

Future checks:
- Crystallography source used for comparison:
  https://github.com/emmo-repo/domain-crystallography
- EMMO releases:
  https://github.com/emmo-repo/EMMO/releases
"""

from util import add_altLabel, en, enUS


def add_energy_entities(onto):
    """Define entities related to energy terms."""
    with onto:

        class EnergyDensityUnit(onto.SIDimensionalUnit):
            """Unit of energy density. Defined using SI base units."""

            prefLabel = en("EnergyDensityUnit")
            is_a = [onto.hasDimensionString.value("T-2 L-1 M+1 I0 Θ0 N0 J0")]

        # Assert JoulePerCubicMetre as subclass of EnergyDensityUnit
        onto.JoulePerCubicMetre.is_a.append(EnergyDensityUnit)
        add_altLabel(onto.JoulePerCubicMetre, enUS("JoulePerCubicMeter"))
        # Assert MegaJoulePerCubicMetre as subclass of EnergyDensityUnit
        onto.MegaJoulePerCubicMetre.is_a.append(EnergyDensityUnit)
        add_altLabel(onto.MegaJoulePerCubicMetre, enUS("MegaJoulePerCubicMeter"))

        class EnergyDensity(onto.PhysicalQuantity):
            """Energy Density."""

            prefLabel = en("EnergyDensity")
            is_a = [
                onto.hasMeasurementUnit.some(EnergyDensityUnit),
            ]

        class LineEnergyUnit(onto.SIDimensionalUnit):
            """Unit of energy per unit length. Defined using SI base units."""

            prefLabel = en("LineEnergyUnit")
            is_a = [onto.hasDimensionString.value("T-2 L+1 M+1 I0 Θ0 N0 J0")]

        # Assert JoulePerMetre as subclass of LineEnergyUnit
        onto.JoulePerMetre.is_a.append(LineEnergyUnit)
        add_altLabel(onto.JoulePerMetre, enUS("JoulePerMeter"))

        class LineEnergy(onto.PhysicalQuantity):
            """Energy per unit length."""

            prefLabel = en("LineEnergy")
            altLabel = [en("EnergyPerUnitLength"), en("EnergyPerLength")]
            is_a = [
                onto.hasMeasurementUnit.some(LineEnergyUnit),
            ]
