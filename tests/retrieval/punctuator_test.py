from app.retrieval.punctuator import punctuate

raw_input = 'the atm protein is a single high molecular weight protein predominantly confined to the nucleus of human fibroblasts but is present in both nuclear and microsomal fractions from human lymphoblast cells and peripheral blood lymphocytes atm protein levels and localization remain constant throughout all stages of the cell cycle truncated atm protein was not detected in lymphoblasts from ataxia telangiectasia patients homozygous for mutations leading to premature protein termination exposure of normal human cells to gamma irradiation and the radiomimetic drug neocarzinostatin had no effect on atm protein levels in contrast to a noted rise in p53 levels over the same time interval these findings are consistent with a role for the atm protein in ensuring the fidelity of dna repair and cell cycle regulation following genome damage'

expected_result = 'The ATM protein is a single, high-molecular-weight protein predominantly confined to the nucleus of human fibroblasts, but is present in both nuclear and microsomal fractions from human lymphoblast cells and peripheral blood lymphocytes. ATM protein levels and localization remain constant throughout all stages of the cell cycle. Truncated ATM protein was not detected in lymphoblasts from ataxia-telangiectasia-patients homozygous for mutations leading to premature protein termination. Exposure of normal human cells to gamma-irradiation and the radiomimetic drug neocarzinostatin had no effect on ATM protein levels, in contrast to a noted rise in p53 levels over the same time interval. These findings are consistent with a role for the ATM protein in ensuring the fidelity of DNA repair and cell-cycle regulation following genome damage. '


def test_punctuator():
    assert punctuate(raw_input) == expected_result
