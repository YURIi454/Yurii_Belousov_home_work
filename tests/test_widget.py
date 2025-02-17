from src.widget import mask_account_card
from src.widget import get_date
import pytest

''' Тестирование модуля widget.py '''


@pytest.mark.parametrize(("data", "mod_data"),
                         (("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                          ("Счет 64686473678894779589", "Счет **9589"),
                          ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                          ("Счет 35383033474447895560", "Счет **5560"),
                          ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                          ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                          ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                          ("Счет 73654108430135874305", "Счет **4305")))
def test_widget_0(data, mod_data):
    assert mask_account_card(data) == mod_data


@pytest.mark.parametrize(("date", "reformat_date"),
                         (("2019-07-03T18:35:29.512364", "03.07.2019"),
                          ("2018-06-30T02:08:58.425572", "30.06.2018"),
                          ("2018-09-12T21:27:25.241689", "12.09.2018"),
                          ("2018-10-14T08:21:33.419441", "14.10.2018"),
                          ("2016-02-29T08:21:33.419441", "29.02.2016"),
                          ("", "01.01.2000"),
                          ("   ", "01.01.2000")))
def test_widget_1(date, reformat_date):
    assert get_date(date) == reformat_date
