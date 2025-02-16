from src.masks import get_mask_card_number
from src.masks import get_mask_account
import pytest

''' Тестирование модуля masks.py '''


@pytest.mark.parametrize(("name", "card_number", "result"),
                         (("", " ", "   ** **** "),
                          ("", "445566", " 4455 66** **** "),
                          ("Maestro", 3652125478546985, "Maestro 3652 12** **** 6985")))
def test_masks_0(name, card_number, result):
    assert get_mask_card_number(name, card_number) == result


@pytest.mark.parametrize(("name", "card_number", "result"),
                         (("", None, " **None"),
                         ("b", 0, "b **0"),
                         ("b", 45676, "b **5676")))
def test_masks_1(name, card_number, result):
    assert get_mask_account(name, card_number) == result
