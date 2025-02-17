#####
# from src.masks import get_mask_card_number
# from src.masks import get_mask_account
# from src.widget import mask_account_card
# from src.widget import get_date
# from src.processing import filter_by_state
# from src.processing import sort_by_date
# import pytest

# '''Тесты для модуля masks.py'''

# @pytest.mark.parametrize(("name", "card_number", "result"),
#                          (("", 123, ' 123 ** **** '),
#                           ("", 445566, " 4455 66** **** "),
#                           ("Maestro", 3652125478546985, "Maestro 3652 12** **** 6985")))
# def test_masks_0(name, card_number, result):
#     assert get_mask_card_number(name, card_number) == result
#
#
# @pytest.mark.parametrize(("name", "card_number", "result"),
#                          (("", None, " **None"),
#                          ("b", 0, "b **0"),
#                          ("b", 45676, "b **5676")))
# def test_masks_1(name, card_number, result):
#     assert get_mask_account(name, card_number) == result


# ''' Тесты модуля widget.py'''


# @pytest.mark.parametrize(("data", "mod_data"),
#                          (("12345689357356756756756756756", " **6756"),
#                           ("only letters", "only letters  ** **** "),
#                           ("Letters and 36521474", "Letters and 3652 14** **** ")))
# def test_widget_0(data, mod_data):
#     assert mask_account_card(data) == mod_data
#
#
# @pytest.mark.parametrize(("date", "reformat_date"),
#                          (("22.22.2222", "22.22.2222"),
#                          ("9876-25-12-1245-458", "12.25.9876")))
# def test_widget_1(date,reformat_date):
#     assert get_date(date) == reformat_date


# '''Тесты модуля processing.py'''

# @pytest.mark.parametrize(("list_1", " ", "list_2"),
#                          ([], "CANCELED", []))
# def test_processing_0(a, b, c):
#     assert filter_by_state(a,b) == c
#
#
# def test_processing_1():
#     assert filter_by_state([], "CANCELED") == []
#
#
# def test_processing_2():
#     assert filter_by_state([], "EXECUTED") == []
#
#
# def test_processing_3():
#     assert filter_by_state(
#         [{"test": "pass", "state": "CANCELED"}, {"test": "ok", "state": "EXECUTED"}], "CANCELED"
#     ) == [{"state": "CANCELED", "test": "pass"}]
#
#
# def test_processing_4():
#     assert filter_by_state(
#         [{"test": "pass", "state": "CANCELED"}, {"test": "ok", "state": "EXECUTED"}], "EXECUTED"
#     ) == [{"test": "ok", "state": "EXECUTED"}]
#
#
# def test_processing_5():
#     assert sort_by_date([{"date": "0"}, {"date": "1"}, {"date": "2"}, {"date": "3"}], False) == [
#         {"date": "0"},
#         {"date": "1"},
#         {"date": "2"},
#         {"date": "3"},
#     ]
#
#
# def test_processing_6():
#     assert sort_by_date([{"date": "0"}, {"date": "1"}, {"date": "2"}, {"date": "3"}], True) == [
#         {"date": "3"},
#         {"date": "2"},
#         {"date": "1"},
#         {"date": "0"},
#     ]
#
#
# def test_processing_7():
#     assert sort_by_date([{"date": "0"}, {"date": "0"}, {"date": "0"}, {"date": "0"}], True) == [
#         {"date": "0"},
#         {"date": "0"},
#         {"date": "0"},
#         {"date": "0"},
#     ]
#
#
# def test_processing_8():
#     assert sort_by_date([], True) == []
#
#
# def test_processing_9():
#     assert sort_by_date([], False) == []
