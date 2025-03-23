from custom_loger import get_logger

logger = get_logger()


def filter_by_state(user_data: list, key_word: str) -> list:
    """Принимает список словарей и значение ключа фильтра.
    Возвращает отфильтрованный список словарей."""
    logger.info("Start!")
    new_list: list = []

    if not key_word:
        return new_list

    else:
        for item in user_data:
            logger.info("Перебор элементов")
            if item.get("state", "") == key_word:
                new_list.append(item)
    logger.info("Successful !")
    return new_list


def sort_by_date(user_data: list, rev_: bool = False) -> list:
    """Принимает список словарей и порядок сортировки (default="reverse=False").
    Возвращает список, отсортированный по дате."""

    logger.info("Start!")
    sort_list = sorted(user_data, reverse=rev_, key=lambda x: x["date"])
    logger.info("Successful !")
    return sort_list
