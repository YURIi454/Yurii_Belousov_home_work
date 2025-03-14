import pytest

from src.masks import get_mask_account, get_mask_card_number

""" Тестирование модуля masks.py """


@pytest.mark.parametrize(
    ("name", "card_number", "result"),
    (
        ("", " ", ""),
        ("", "445566", ""),
        ("Maestro", "3652125478546985", "Maestro 3652 12** **** 6985"),
    ),
)
def test_masks_0(name: str, card_number, result: str):  # type: ignore
    assert get_mask_card_number(name, card_number) == result


@pytest.mark.parametrize(
    ("name", "card_number", "result"), (("", None, ""), ("b", 0, ""), ("b", 95135745698732146597, "b **6597"))
)
def test_masks_1(name: str, card_number, result: int):  # type: ignore
    assert get_mask_account(name, card_number) == result
