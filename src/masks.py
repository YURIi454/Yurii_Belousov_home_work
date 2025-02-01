def get_mask_card_number(name:str, card_number:int) -> str:
    """Принимает номер карты. Возвращает замаскированный номер карты."""

    card_number = str(card_number)
    #print('ok_masks')
    return f"{name} {card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(name:str, card_number:int) -> str:
    """Принимает номер счёта. Возвращает замаскированный номер счёта."""

    card_number = str(card_number)

    return f"{name} **{card_number[-4:]}"
