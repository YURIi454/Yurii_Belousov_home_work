import json
import logging
from typing import Any

from src.external_api import get_convert_currency
from src.logging_my import get_logger

logger = get_logger()


def read_json(path: str = "") -> list[dict]:
    """Чтение файлов json, преобразование в объект python."""

    logging.info("Начало работы.")

    try:
        with open(path, "r", encoding="utf-8") as file:
            file_decode = json.load(file)
            if not isinstance(file_decode, list):
                return []
    except TypeError as er:
        logging.error(f"Ошибка {er}")
        return []
    except FileNotFoundError as er:
        logging.error(f"Ошибка {er}")
        return []

    logging.info("Конец работы.")

    return file_decode


def transactions(operations: Any) -> Any:
    """Принимает транзакцию в рублях, USD или EUR и возвращает сумму транзакции.
    Обращается к внешнему API для корректировки курса валют и конвертации
    суммы операции в рубли."""

    logging.info("Начало работы.")
    try:
        for elem in operations:
            if not len(elem):
                continue

            if elem["operationAmount"]["currency"]["code"] == "RUB":
                logging.info("Конец работы.")
                return float(elem["operationAmount"]["amount"])
            else:
                logging.info("Конец работы.")
                return get_convert_currency(
                    elem["operationAmount"]["amount"], elem["operationAmount"]["currency"]["code"]
                )

    except Exception as er:
        logging.error(f" Ошибка {er}")
