from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(user_data: str) -> str:
    """Функция принимает наименование карты и её номер или наименование счёта и его номер.
    Возвращает наименование карты / счёта без изменений и замаскированный номер."""

    user_data = user_data.split(" ")
    name_bank = " ".join(user_data[:-1])
    number_account = "".join(user_data[-1])
    number_account = int(number_account)

    if len(str(number_account)) > 16:
        return get_mask_account(name_bank, number_account)

    else:
        return get_mask_card_number(name_bank, number_account)


def get_date(date: str) -> str:
    """Функция принимает дату формата "ISO 8601" .
    Возвращает дату привычного формата ХХ.ХХ.ХХХХ. ."""
    date = date[:10].split("-")
    date = ".".join(reversed(date))
    return date
