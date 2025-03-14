from unittest.mock import patch

import pandas as pd

from src.csv_xlsx_ import read_csv, read_xlsx


def test_read_csv_0():  # type:ignore
    assert read_csv("") == []
    assert read_csv(".csv") == []


def test_read_xlsx_0():  # type:ignore
    assert read_xlsx("") == []
    assert read_xlsx(".xlsx") == []


@patch("src.csv_xlsx_.pd.read_excel")
def test_read_xlsx_1(mock_read_exel):  # type:ignore
    mock_df = pd.DataFrame([{"id": 1, "amount": 100}, {"id": 2, "amount": 200}])
    mock_read_exel.return_value = mock_df

    result = read_xlsx("data.xlsx")
    assert result == [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]
