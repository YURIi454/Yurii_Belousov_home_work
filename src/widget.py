from src.masks import get_mask_card_number


def mask_account_card(user_data):
    name_bank = ""
    number_account = ""
    for symbol in user_data:
        if symbol.isalpha():
            name_bank = "".join([name_bank, symbol])

        if symbol.isdigit():
            number_account = "".join([number_account,symbol])

    number_account = int(number_account)
    print(name_bank, number_account)

    return  get_mask_card_number(name_bank, number_account)


mask_account_card("Счет 35383033474447895560")
