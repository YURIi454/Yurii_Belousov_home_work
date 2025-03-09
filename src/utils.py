import json
from typing import Any

from src.external_api import get_convert_currency


def read_json(path: str = "") -> list[dict]:
    """Чтение файлов json, преобразование в объект python."""

    try:
        with open(path, "r", encoding="utf-8") as file:
            file_decode = json.load(file)
            if not isinstance(file_decode, list):
                return []
    except TypeError:
        return []
    except FileNotFoundError:
        return []

    return file_decode


def transactions(operations: Any) -> Any:
    """Принимает транзакцию в рублях, USD или EUR и возвращает сумму транзакции.
    Обращается к внешнему API для корректировки курса валют и конвертации
    суммы операции в рубли."""

    for elem in operations:
        if not len(elem):
            continue

        if elem["operationAmount"]["currency"]["code"] == "RUB":
            return float(elem["operationAmount"]["amount"])
        else:
            return get_convert_currency(elem["operationAmount"]["amount"], elem["operationAmount"]["currency"]["code"])
