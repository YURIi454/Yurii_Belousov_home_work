import json
import logging
from typing import Any

from custom_loger import get_logger
from src.external_api import get_convert_currency

logger = get_logger()


def read_json(path: str) -> list[dict]:
    """Чтение файлов json и преобразование в объект python."""

    logging.info("Начало работы.")

    try:
        with open(path, "r", encoding="utf-8") as file:
            file_decode = json.load(file)
            if not isinstance(file_decode, list):
                return []

    except (FileNotFoundError, TypeError) as er:
        logging.error(f"Ошибка {er}")
        return []

    logging.info("Successful !")

    return file_decode


def transactions(operations: list[dict]) -> Any:
    """Возвращает сумму транзакции из списка.
    Транзакции в другой валюте обрабатываются через API-запрос."""

    logging.info("Начало работы.")
    try:
        for elem in operations:
            logger.info("Перебор элементов")
            if not len(elem):
                continue

            if elem["operationAmount"]["currency"]["code"] == "RUB":
                logging.info("Successful !")
                return float(elem["operationAmount"]["amount"])
            else:
                logging.info("Successful !")
                return get_convert_currency(
                    elem["operationAmount"]["amount"], elem["operationAmount"]["currency"]["code"]
                )

    except Exception as er:
        logging.error(f" Ошибка {er}")
