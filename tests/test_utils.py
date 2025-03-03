import json
from src.utils import transactions, read_json


with open('../data/operations.json', "r", encoding="utf-8") as file:
    operations = json.load(file)


def test_transactions():
    assert transactions([]) == []
    assert read_json([]) == []


def test_transactions_1():
      assert transactions(operations) == operations

print(operations)