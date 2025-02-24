def get_mask_card_number(name: str, card_number: str) -> str:
    """Принимает тип карты в виде текста и номер карты.
    Возвращает тип карты без изменений и замаскированный номер карты."""

    if len(card_number) != 16:
        print(" \033[31m Некорректная длина номера!\033[39m")

    return f"{name} {card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(name: str, card_number: int) -> str:
    """Принимает название счёта и номер счёта.
    Возвращает название счёта без изменений и замаскированный номер счёта."""

    if len(str(card_number)) != 20:
        print(" \033[31m Некорректная длина номера!\033[39m")

    return f"{name} **{str(card_number)[-4:]}"
