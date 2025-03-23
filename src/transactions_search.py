import re
from collections import Counter

from custom_loger import get_logger

logger = get_logger()


def filter_transactions(data: list[dict], find_word: str) -> list[dict]:
    """Поиск совпадений по введённым данным."""

    logger.info("Start")
    if not find_word:
        return data
    else:
        filtered_transaction = [
            pcs
            for pcs in data
            if isinstance(pcs.get("description", ""), str)
            and re.search(find_word, pcs.get("description", ""), flags=re.IGNORECASE)
        ]
        logger.info("Successful")
        return filtered_transaction


def filter_category_transactions(data: list[dict], category: list) -> dict:
    """Поиск категорий по введённым данным."""

    logger.info("Start")

    info_transaction = [
        elem["description"] for elem in data if elem["description"] in list(map(lambda x: x, category))
    ]
    count_by_category = dict(Counter(info_transaction))
    logger.info("Successful")
    return count_by_category
