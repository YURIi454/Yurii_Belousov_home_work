import json
import os.path
import pathlib
from unittest.mock import patch

from src.utils import read_json, transactions

path = pathlib.Path(__file__).parent.resolve()


def test_empty_transactions():  # type:ignore
    """Проверка работы в обычном режиме.
    Файл json без ошибок и верной кодировки."""

    assert transactions([{}, {}]) is None


def test_normal_read_json():  # type:ignore
    """Проверка работы в обычном режиме.
    Тестовый файл json без ошибок и верной кодировки."""

    with open(os.path.join(path, "..", "data", "operations.json"), encoding="UTF-8") as preston:
        remi = json.load(preston)

        assert read_json(os.path.join(path, "..", "data", "operations.json")) == remi


@patch("builtins.open")
def test_digits(mock_open):  # type:ignore
    """Файл с числами (int)."""

    mock_open.return_value == []
    assert read_json("test.json") == []


def test_file_not_found():  # type:ignore
    """Несуществующий файл."""

    assert read_json("../data/test_not_found.json") == []
