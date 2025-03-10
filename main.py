from src.masks import get_mask_card_number, get_mask_account
from src.utils import read_json, transactions


def main():
    """Функция запуска приложения."""

    transact = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]

    get_mask_card_number("Rostovshik_bank", "4561597463587564")
    get_mask_card_number("Rostovshik_bank", "456159746358564")
    get_mask_account("General_scammer", 65987491354102698741)
    get_mask_account("General_scammer", 6598749135102698741)
    read_json("data/operations.json")
    read_json("data/file_not_found.json")
    transactions(transact)


if __name__ == "__main__":
    main()
