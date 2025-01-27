from masks import get_mask_card_number

number = {'1': 'Visa Platinum 7000792289606361', '2': 'Maestro 7000792289606361', '3': 'Счет 73654108430135874305'}


def mask_account_card(**kwargs):
    number['1'] = get_mask_card_number(card_number: int) -> str:
    return print(mask)

mask_account_card(**number)
'''Аргументом может быть строка типа 
Visa Platinum 7000792289606361
, или 
Maestro 7000792289606361
, или 
Счет 73654108430135874305
. Разделять строку на 2 аргумента (отдельно имя, отдельно номер) нельзя!'''