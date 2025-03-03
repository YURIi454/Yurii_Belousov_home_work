import json


# путь ("C:/Users/Sergey/PycharmProjects/Yurii_Belousov/data/operations.json", "r", encoding="utf-8")

def transactions(operations: list[dict]):
    return operations


def read_json(path=None) -> list[dict]:
    with open(path) as file:
        file = json.load(file)
        return transactions(file)

# with open("C:/Users/Sergey/PycharmProjects/Yurii_Belousov/data/operations.json", "r", encoding="utf-8") as file:
#     operations = json.load(file)
#
# print(len(list(operations)))

# import chardet
#
# # Определяем кодировку
# with open("C:/Users/Sergey/PycharmProjects/Yurii_Belousov/data/operations.json", 'rb') as file:
#     encoding = chardet.detect(file.read())['encoding']
# print(encoding)
