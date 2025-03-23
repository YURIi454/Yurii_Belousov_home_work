import re

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_data: str) -> str:  # type: ignore
    """Принимает наименование карты и её номер или наименование счёта и его номер.
    Возвращает наименование карты / счёта и замаскированный номер."""

    if not isinstance(user_data, str):
        return "*не указано*"

    name_bank = re.findall(r"[а-яёА-ЯЁa-zA-Z]+", user_data)
    number_account = re.findall(r"\d+", user_data)

    str_name_bank = " ".join(map(str, name_bank))
    int_number_account = " ".join(map(str, number_account))

    if len(int_number_account) == 20:
        return get_mask_account(str(str_name_bank), int(int_number_account))

    if len(int_number_account) == 16:
        return get_mask_card_number(str(str_name_bank), str(int_number_account))


def get_date(date: str) -> str:
    """Принимает дату формата "ISO 8601"
    Возвращает дату привычного формата ХХ.ХХ.ХХХХ."""

    default_date = "01.01.2000"

    if date.isalpha() or date.isspace():
        return default_date

    elif len(date) == 0:
        return default_date

    else:
        date_split = date[:10].split("-")
        date_reformat = ".".join(reversed(date_split))

        return date_reformat
