from src.masks import get_mask_card_number
from src.masks import get_mask_account
"""Проверка другой версии кода. После проверки удалить"""
def mask_account_card(user_data):
    user_data = user_data.split(" ")
    name_bank = " ".join(user_data[:-1])
    number_account = "".join(user_data[-1])
    #print( " ".join(user_data[-1]))
    number_account = int(number_account)
    #print("ok_widget")
    if len(str(number_account)) > 17:
        print(get_mask_account(name_bank,  number_account))
        return get_mask_account(name_bank,  number_account)
    else:
        print(get_mask_card_number(name_bank, number_account))
        return get_mask_card_number(name_bank, number_account)


def test_production():

    data_test = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "Master Card 7158300734726758",
    "Счет 35383033474447895560",
    "Visa  Classic 6831982476737658",
    'Visa Platinum 8990922113665229',
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305"
]

    for i in data_test:
        mask_account_card(i)


test_production()