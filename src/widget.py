
from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(user_data: str) -> str:
    """Функция принимает наименование карты и её номер или наименование счёта и его номер.
    Возвращает наименование карты / счёта без изменений и замаскированный номер."""

    import re

    name_bank = re.findall(r'[a-zA-Z]+', user_data)
    number_account = re.findall(r'\d+', user_data)
    name_bank = " ".join(name_bank)
    number_account = " ".join(number_account)

    if len(str(number_account)) > 16:
        return get_mask_account(name_bank, int(number_account))

    else:
        return get_mask_card_number(name_bank, number_account)


def get_date(date: str) -> str:
    """Функция принимает дату формата "ISO 8601" .
    Возвращает дату привычного формата ХХ.ХХ.ХХХХ. ."""

    date = date[:10].split("-")
    date = ".".join(reversed(date))
    return date
