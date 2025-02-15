

def filter_by_state(user_data: list, key_word: str = "EXECUTED") -> list:
    """Принимает список словарей и значение ключа фильтра (default='EXECUTED').
    Возвращает отфильтрованный список словарей."""

    new_list = []

    for item in user_data:
        if item.get("state") == key_word:
            new_list.append(item)

    return new_list


def sort_by_date(user_data: list, rev_: bool = False) -> list:
    """Принимает список словарей и параметр,
    задающий порядок сортировки (default="reverse=False").
    Функция возвращает новый список, отсортированный по дате."""

    sort_list = sorted(user_data, reverse=rev_, key=lambda x: x["date"])

    return sort_list
