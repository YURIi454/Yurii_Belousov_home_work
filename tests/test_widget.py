from src.widget import mask_account_card
from src.widget import get_date
import pytest

''' Тестирование модуля widget.py '''


@pytest.mark.parametrize(("data", "mod_data"),
                         (("12345689357356756756756756756", " **6756"),
                          ("only letters", "only letters  ** **** "),
                          ("Letters and 36521474", "Letters and 3652 14** **** ")))
def test_widget_0(data, mod_data):
    assert mask_account_card(data) == mod_data


@pytest.mark.parametrize(("date", "reformat_date"),
                         (("22.22.2222", "22.22.2222"),
                         ("2020-25-12-1245-458", "12.25.2020"),
                          ("","01.01.2000"),
                          ("abc","01.01.2000")))
def test_widget_1(date,reformat_date):
    assert get_date(date) == reformat_date
