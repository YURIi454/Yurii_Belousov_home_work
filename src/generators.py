from typing import Any, Generator, Iterator

from custom_loger import get_logger

cstm_loger = get_logger()


def filter_by_currency(data: list[dict], key_word: str) -> Iterator:
    """Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции, с заданной валютой."""

    cstm_loger.info("TEST")

    filtered_data = filter(lambda item: item["operationAmount"]["currency"]["code"] == key_word, data)

    return transaction_descriptions(filtered_data)


def transaction_descriptions(data: Any) -> Generator[str]:
    """Принимает список словарей с транзакциями и возвращает
    описание каждой операции по очереди."""
    cstm_loger.info("TEST")
    for descript_operation in data:
        yield descript_operation["description"]


def card_number_generator(start_number: int, stop_number: int) -> Generator[str]:
    """Генератор номеров в формате XXXX XXXX XXXX XXXX
    в диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    cstm_loger.info("TEST")
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
