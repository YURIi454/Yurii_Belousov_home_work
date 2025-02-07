def filter_by_state(us_dt: list, key_word="EXECUTED") -> list:
    """Функция принимает список словарей и значение ключа фильтра (default='EXECUTED').
    Возвращает отфильтрованный список словарей."""

    new_list = []

    for item in us_dt:
        if item.get("state") == key_word:
            new_list.append(item)

    return new_list


def sort_by_date(us_dt: list, rev_=False) -> list:
    """Функция принимает список словарей и параметр,
    задающий порядок сортировки (default="reverse=False").
    Функция возвращает новый список, отсортированный по дате."""

    sort_list = sorted(us_dt, reverse=rev_, key=lambda x: x["date"])

    return sort_list
