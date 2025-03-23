import re

from config import PATH_CSV, PATH_JSON, PATH_XLSX
from custom_loger import get_logger
from src.csv_xlsx_ import read_csv, read_xlsx
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.transactions_search import filter_transactions
from src.utils import read_json
from src.widget import get_date, mask_account_card

logger = get_logger()


def main():
    """Основная функция, запуска приложения."""

    logger.info(f"Запуск основной функции из {__file__}")

    print(
        """'
    Привет! Добро пожаловать в приложение для банковскими транзакциями.

    Выберите необходимый пункт меню:

    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """
    )

    while True:
        choice_type_file = input()
        if not re.search(r"[1-3]", choice_type_file):
            print("Пожалуйста, введите один из вариантов! (1, 2, 3)")
            logger.warning(f'Ввод  - "{choice_type_file}"')
        else:
            break

    choice_type_file = int(choice_type_file)

    type_files = ("JSON", "CSV", "XLSX")

    print(f"Для обработки выбран {type_files[choice_type_file - 1]}-файл.")

    read_file = (read_json(PATH_JSON), read_csv(PATH_CSV), read_xlsx(PATH_XLSX))

    final_data = read_file[choice_type_file - 1]

    print(
        """Введите статус, операции который вам нужен.
    Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
    )

    while True:
        status = input().upper()
        if status not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Статус операции {status} недоступен")
        else:
            break

    print(f"Выбран статус {status}")
    final_data = filter_by_state(final_data, status)
    print("Отсортировать операции по дате? (Да / Нет)")

    sort_order = input().upper()
    if "ДА" in sort_order:
        sort_order = False
    else:
        sort_order = True
    final_data = sort_by_date(final_data, sort_order)

    print("Отсортировать по возрастанию или по убыванию? (Да / Нет)")
    sort_rev = input().lower()
    if sort_rev == "да":
        sort_rev = False
    else:
        sort_rev = True
    try:
        logger.info("Сортировка через в main.")
        final_data = sorted(final_data, reverse=sort_rev, key=lambda x: x["amount"])
        final_data = sorted(final_data, reverse=sort_rev, key=lambda x: x["operationAmount"]["currency"]["code"])
    except KeyError as error:
        logger.warning(f"{error}")

    print("Выводить только рублевые транзакции? Да/Нет")
    choice_currency = input().upper()
    if "ДА" in choice_currency:
        currency = "RUB"
    else:
        currency = ""
    final_data = filter_by_currency(final_data, currency)

    print("Отфильтровать список транзакций по определенному слову в описании?")
    word_to_search = input("Что будем искать?\n").lower()

    final_data = filter_transactions(final_data, word_to_search)

    print("Подготовка списка транзакций...")

    if not len(final_data):
        print("Не нашлось  ни одной операции, с такими параметрами.")
    else:
        print(f"Всего банковских операций найдено: {len(final_data)}\n")

        for i in final_data:
            logger.info(f"Перебор элементов{i['id']}")
            if choice_type_file == 1:
                print(
                    f"{get_date(i['date'])} {i['description']}\n"
                    f"{mask_account_card(i.get('from'))} >>> {mask_account_card(i['to'])} \n"
                    f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['code']}\n"
                )
            if choice_type_file >= 2:
                print(
                    f"{get_date(i['date'])} {i['description']}\n"
                    f"{mask_account_card(i['from'])} >>> {mask_account_card(i['to'])} \n"
                    f"{i['amount']} {i['currency_code']}\n"
                )
    logger.info("Завершение работы")


if __name__ == "__main__":
    main()
