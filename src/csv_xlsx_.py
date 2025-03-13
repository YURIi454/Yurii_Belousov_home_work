import csv
from typing import Any

import pandas as pd

from custom_loger import get_logger

logging = get_logger()


def read_csv(path: str = "") -> list[dict[Any, Any]]:
    """Принимает файл формата CSV, возвращает список словарей с транзакциями."""

    logging.info("Start.")
    try:
        if ".csv" not in path:
            logging.error(f"Неверный формат файла! ......{path[-10:]}")
            return []
        with open(path, mode="r", encoding="UTF-8") as file_csv:

            logging.info("Successful !")
            reader_dict = csv.DictReader(file_csv, delimiter=";")

            transactions_list = [row for row in reader_dict]
            return transactions_list
    except Exception as error:
        logging.info(f"Ошибка {type(error)}")
        return []


def read_xlsx(path: str = "") -> list[dict[Any, Any]]:
    """Принимает файл формата XLSX, возвращает словарей с транзакциями."""

    logging.info("Start.")
    try:
        if ".xlsx" not in path:
            logging.error(f"Неверный формат файла! ......{path[-10:]}")
            return []
        logging.info("Successful !")
        return pd.read_excel(path).to_dict(orient="records")
    except Exception as error:
        logging.error(f"Ошибка {type(error)}")
        return []
