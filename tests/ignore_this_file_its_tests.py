#
# # Проверка  работы кода и функций.
#
# from src.masks import get_mask_card_number
# from src.masks import get_mask_account
# from src.processing import filter_by_state
# from src.processing import sort_by_date
#
#
# """Проверка и отладка"""
#
# def mask_account_card(user_data):
#     """Тест"""
#
#     user_data = user_data.split(" ")
#     name_bank = " ".join(user_data[:-1])
#     number_account = "".join(user_data[-1])
#
#     print( "".join(user_data[-1])) # лишний пробел, уронил функцию.
#
#     number_account = int(number_account)
#
#     print("testing \033[32m widget.py - OK! \033[39m")
#
#     if len(str(number_account)) > 16:
#         print(get_mask_account(name_bank,  number_account))
#         return get_mask_account(name_bank,  number_account)
#
#     else:
#         print(get_mask_card_number(name_bank, number_account))
#         return get_mask_card_number(name_bank, number_account)
#
#
# def test_():
#     """Функция тестирования домашки 10.1"""
#     print(filter_by_state(
#      [
#      {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#      {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#      {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#      ], "EXECUTED"   ))
#
#     print(sort_by_date(
#         [
#             {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#             {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#             {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#             {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#         ], True
#     ))
#
# def test_production():
#     """Функция тестирования домашки 9.2"""
#
#     data_test = [
#     "Maestro 1596837868705199",
#     "Счет 64686473678894779589",
#     "Master Card 7158300734726758",
#     "Счет 35383033474447895560",
#     "Visa  Classic 6831982476737658",
#     'Visa Platinum 8990922113665229',
#     "Visa Gold 5999414228426353",
#     "Счет 73654108430135874305"
# ]
#
#     for i in data_test:
#         mask_account_card(i)
#
#
# test_production()
#
# if __name__ == "__main__":
#     print("Запуск из модуля из \033[32m ignore_this_file_tests.py\033[39m")
#     test_()
#
# else:
#     print("Запуск из \033[31mимпорта\033[39m")