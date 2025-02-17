
from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(user_data: str) -> str:
    """Принимает наименование карты и её номер или наименование счёта и его номер.
    Возвращает наименование карты / счёта без изменений и замаскированный номер."""

    import re

    name_bank = re.findall(r'[а-яёА-ЯЁa-zA-Z]+', user_data)
    number_account = re.findall(r'\d+', user_data)

    name_bank = " ".join(name_bank)
    number_account = " ".join(number_account)

    if len(number_account) <= 16:
        print("Проверьте корректность данных!")

    if len(number_account) == 20:
        return get_mask_account(name_bank, int(number_account))

    if len(number_account) == 16:
        return get_mask_card_number(name_bank, number_account)


def get_date(date: str) -> str:
    """Принимает дату формата "ISO 8601" .
    Возвращает дату привычного формата ХХ.ХХ.ХХХХ. ."""

    default_date = "01.01.2000"

    if date.isalpha() or date.isspace():
        return default_date

    elif len(date) == 0:
        return default_date

    else:
        date = date[:10].split("-")
        date = ".".join(reversed(date))

        return date
