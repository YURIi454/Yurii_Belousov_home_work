import pytest


@pytest.fixture
def test_module_processing(data_for_test):
 data_for_test = [
    {"test": "ok_c_1", "state": "CANCELED"},
    {"test": "ok_e_1", "state": "EXECUTED"},
    {"test": "ok_c_2", "state": "CANCELED"},
    {"test": "ok_e_2", "state": "EXECUTED"},
    {"test": "ok_c_3", "state": "CANCELED"},
    {"test": "ok_e_3", "state": "EXECUTED"},
    {"test": "ok_c_4", "state": "CANCELED"},
    {"test": "ok_e_4", "state": "EXECUTED"}
]
 filter_by_state()
