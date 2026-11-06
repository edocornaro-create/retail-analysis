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

def test_normalize_ids_both_in_dataframe():
    values = pd.DataFrame({
        'customer_id': [' "c002 "c002', " c003 "],
        'customer_name': ['John', 'Mark', "Paul"]
    })
    result = normalize_ids(values['customer_id'])
    assert result.iloc[0] == 'C001'
    assert result.iloc[1] == 'C002'
    assert result.iloc[2] == 'C003'
    