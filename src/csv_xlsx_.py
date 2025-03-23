import pandas as pd

from custom_loger import get_logger

logging = get_logger()


def read_csv(path: str) -> list[dict]:
    """Чтение файлов CSV и преобразование в объект python."""

    logging.info("Start.")
    try:
        if ".csv" not in path:
            logging.error(f"Неверный формат файла! ......{path[-10:]}")
        logging.info("Successful !")
        return pd.read_csv(path, delimiter=";").to_dict(orient="records")
    except FileNotFoundError:
        return []


def read_xlsx(path: str) -> list[dict]:
    """Чтение файлов XLSX и преобразование в объект python."""

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
