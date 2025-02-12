
from src.masks import  get_mask_card_number
from src.masks import  get_mask_account
from src.widget import  mask_account_card
from src.widget import  get_date
from src.processing import  filter_by_state
from src.processing import  sort_by_date

def test_code():
    assert get_mask_card_number("a", 123) != None

def test_code2():
    assert get_mask_account ("b", 456)!= None

def test_code3():
    assert mask_account_card ("12345689") != None

def test_code4():
    assert get_date("ytrewq")!= None

def test_code5():
    assert filter_by_state([],None)!= None

def test_code6():
    assert sort_by_date([], True)!= None