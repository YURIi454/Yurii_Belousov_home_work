import logging

from custom_loger import get_logger

logger = get_logger()


def get_mask_card_number(name: str, card_number: str) -> str:  # type:ignore
    """Принимает тип карты в виде текста и номер карты.
    Возвращает тип карты без изменений и замаскированный номер карты."""

    logging.info("Start.")

    if len(card_number) == 16:

        logging.info("Successful !")
        return f"{name} {card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"

    else:
        logging.error("Неверная длинна номера!")
        return ""


def get_mask_account(name: str, card_number: int) -> str:  # type:ignore
    """Принимает название счёта и номер счёта.
    Возвращает название счёта без изменений и замаскированный номер счёта."""

    logging.info("Start.")

    if len(str(card_number)) == 20:

        logging.info("Successful !")
        return f"{name} **{str(card_number)[-4:]}"

    else:
        logging.error("Неверная длинна номера!")
        return ""
