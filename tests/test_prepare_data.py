import pandas as pd
from retail_analysis.prepare_data import normalize_ids

def test_normalize_ids_remove_whitespaces():

    values = pd.Series([ 'C001'])

    result = normalize_ids(values)

    assert result.iloc[0] == 'C001'

def test_normalize_ids_lower_case_to_upper_case():

    values = pd.Series(['c001'])

    result = normalize_ids(values)

    assert result.iloc[0] == 'C001'