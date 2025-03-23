from typing import Any, Generator

from custom_loger import get_logger

logger = get_logger()


def filter_by_currency(data: list[dict], key_word: str = "") -> list[dict]:
    """Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции, с заданной валютой."""

    logger.info("Start!")
    if not key_word:
        return data
    filtered_transactions = []

    for item in data:
        logger.info("Перебор элементов")
        if not len(item):
            continue
        try:
            if item.get("operationAmount", {}).get("currency", {}).get("code", {}) == key_word:
                filtered_transactions.append(item)
            if item.get("currency_code", {}) == key_word:
                filtered_transactions.append(item)
            if item.get("currency_name", {}) == key_word:
                filtered_transactions.append(item)

        except KeyError as error:
            logger.warning(f"{error}")
    logger.info("Successful!")
    return filtered_transactions


def transaction_descriptions(data: Any) -> Generator[str]:
    """Принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди."""
    logger.info("TEST")
    for descript_operation in data:
        yield descript_operation["description"]


def card_number_generator(start_number: int, stop_number: int) -> Generator[str]:
    """Генератор номеров в формате XXXX XXXX XXXX XXXX
    в диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    logger.info("TEST")
    finish_number = 9999_9999_9999_9999
    card_number = ""  # type: ignore[no-redef]

    if start_number > finish_number:
        return

    if start_number < 1:
        start_number = 1
    if stop_number > finish_number:
        stop_number = finish_number

    for number in range(start_number, stop_number + 1):
        str_number = str(number)
        str_number = str_number.rjust(16, "0")

        output_number = []
        for item in range(0, 16, 4):
            output_number.append(str_number[item : item + 4])

            card_number: str = " ".join(output_number)  # type: ignore[no-redef]

        yield card_number
