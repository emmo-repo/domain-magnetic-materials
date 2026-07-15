"""Thermodynamics."""

from util import en, pl


def add_thermodynamics_entities(onto):
    """Add thermodynamics entities."""
    with onto:

        class BinderCumulant(onto.ISQDimensionlessQuantity):
            """A dimensionless fourth-order cumulant of magnetization, defined as U4 = 1 −
            <m^4>/(3 <m^2>^2), where m is the normalised magnetization (magnetization per
            site). It is used in finite-size scaling as an approximately scale-independent
            measure of critical fluctuations: curves for different system sizes intersect
            near the phase-transition temperature, enabling estimation of Tc without direct
            extrapolation to infinite system size.
            """

            comment = pl(
                'Binder, K. (1981). "Finite size scaling analysis of ising model block '
                'distribution functions". Zeitschrift für Physik B: '
                "Condensed Matter. 43 (2): 119–140. https://doi.org/10.1007/bf01293604"
            )
            prefLabel = en("BinderCumulant")
            altLabel = [pl("U_L"), en("BinderParameter")]
            wikidataReference = pl("https://www.wikidata.org/wiki/Q4913987")
            wikipediaReference = pl("https://en.wikipedia.org/wiki/Binder_parameter")
