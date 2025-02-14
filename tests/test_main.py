from src.masks import get_mask_card_number
from src.masks import get_mask_account
from src.widget import mask_account_card
from src.widget import get_date
from src.processing import filter_by_state
from src.processing import sort_by_date


def test_masks_0():
    assert get_mask_card_number("", None) == " None ** **** "


def test_masks_1():
    assert get_mask_card_number("", 445566) == " 4455 66** **** "


def test_masks_2():
    assert get_mask_card_number("a", 3652125478546985) == "a 3652 12** **** 6985"


def test_masks_3():
    assert get_mask_account("b", 0) == "b **0"


def test_masks_4():
    assert get_mask_account("b", 45676) == "b **5676"


def test_widget_0():
    assert mask_account_card("12345689357356756756756756756") == " **6756"


def test_widget_1():
    assert mask_account_card("only letters") == "only letters  ** **** "


def test_widget_2():
    assert mask_account_card("Letters and 36521474") == "Letters and 3652 14** **** "


def test_widget_3():
    assert get_date("22.22.2222") == "22.22.2222"


def test_widget_4():
    assert get_date("9876-25-12-1245-458") == "12.25.9876"


def test_processing_0():
    assert filter_by_state([], " ") == []


def test_processing_1():
    assert filter_by_state([], "CANCELED") == []


def test_processing_2():
    assert sort_by_date([{"date": "0"}, {"date": "1"}, {"date": "2"}, {"date": "3"}], False) == [
        {"date": "0"},
        {"date": "1"},
        {"date": "2"},
        {"date": "3"},
    ]


def test_processing_3():
    assert sort_by_date([{"date": "0"}, {"date": "1"}, {"date": "2"}, {"date": "3"}], True) == [
        {"date" "3"},
        {"date": "2"},
        {"date": "1"},
        {"date": "0"},
    ]


def test_processing_4():
    assert sort_by_date([{"date": "0"}, {"data": "0"}, {"data": "0"}, {"date": "0"}], True) == [
        {"date": "0"},
        {"date": "0"},
        {"date": "0"},
        {"date": "0"},
    ]
