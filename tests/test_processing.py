from src.processing import filter_by_state
from src.processing import sort_by_date

''' Тестирование модуля processing.py '''


def test_processing_1():
    assert filter_by_state([], "CANCELED") == []


def test_processing_2():
    assert filter_by_state([], "EXECUTED") == []


def test_processing_3():
    assert filter_by_state(
        [{"test": "pass", "": ""}, {"test": "ok", "state": "EXECUTED"}], "CANCELED"
    ) == []


def test_processing_4():
    assert filter_by_state(
        [{"test": "pass", "state": "CANCELED"}, {"test": "ok", "state": "EXECUTED"}], "EXECUTED"
    ) == [{"test": "ok", "state": "EXECUTED"}]


def test_processing_5():
    assert sort_by_date([{"date": "0"}, {"date": "1"}, {"date": "2"}, {"date": "3"}], False) == [
        {"date": "0"},
        {"date": "1"},
        {"date": "2"},
        {"date": "3"},
    ]


def test_processing_6():
    assert sort_by_date([{"date": "0"}, {"date": "1"}, {"date": "2"}, {"date": "3"}], True) == [
        {"date": "3"},
        {"date": "2"},
        {"date": "1"},
        {"date": "0"},
    ]


def test_processing_7():
    assert sort_by_date([{"date": "0"}, {"date": "0"}, {"date": "0"}, {"date": "0"}], True) == [
        {"date": "0"},
        {"date": "0"},
        {"date": "0"},
        {"date": "0"},
    ]


def test_processing_8():
    assert sort_by_date([], True) == []


def test_processing_9():
    assert sort_by_date([], False) == []
