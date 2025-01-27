def get_mask_card_number(card_number: int) -> str:
    """Принимает номер карты. Возвращает замаскированный номер карты."""

    card_number = str(card_number)

    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: int) -> str:
    """Принимает номер счёта. Возвращает замаскированный номер счёта."""

    account_number = str(account_number)

    return f"**{account_number[-4:]}"
