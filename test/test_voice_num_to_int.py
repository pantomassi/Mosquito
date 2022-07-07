import pytest
from utils import voice_num_to_int as w2n

# pytest test_word_nums_to_int.py

def one_word_case(number):
    return w2n.conv_one_word_num(number) 

def test_one_word_case():
    assert one_word_case(['oh']) == 0
    assert one_word_case(['six']) == 6
    assert one_word_case(['fifty']) == 50
    assert one_word_case(['hundred']) == 100
    assert one_word_case(['bamboozle']) == None
    assert one_word_case(['not_a_valid_number']) == None



def two_words_case(number):
    return w2n.conv_two_words_num(number)

def test_two_words_case():
    assert two_words_case(['fifty', 'five']) == 55
    assert two_words_case(['one', 'hundred']) == 100
    assert two_words_case(['two', 'fifty']) == 250
    assert two_words_case(['five', 'fifteen']) == 515
    assert two_words_case(['six', 'hundred']) == 600
    assert two_words_case(['oh', 'seventy']) == None
    assert two_words_case(['hundred', 'hundred']) == None
    assert two_words_case(['eighty', 'eighty']) == None
    assert two_words_case(['not_even', 'a_number']) == None



def three_words_case(number):
    return w2n.conv_three_words_num(number)

def test_three_words_case():
    assert three_words_case(['five', 'oh', 'seven']) == 507
    assert three_words_case(['nine', 'ninety', 'nine']) == 999
    assert three_words_case(['hundred', 'fifty', 'seven']) == None
    assert three_words_case(['oh', 'seven', 'seven']) == None
    assert three_words_case(['one', 'hundred', 'hundred']) == None
    assert three_words_case(['five', 'oh', 'not_a_num']) == None
    assert three_words_case(['not', 'a', 'valid', 'number']) == None



def random_case(number):
    return w2n.voice_num_to_int(number)

def test_random_case():
    assert random_case(['ten']) == 10
    assert random_case(['one', 'hundred']) == 100
    assert random_case(['hundred']) == 100
    assert random_case(['one', 'eleven']) == 111
    assert random_case(['one', 'eighty']) == 180
    assert random_case(['five', 'oh', 'seven']) == 507
    assert random_case(['five', 'fifteen']) == 515
    assert random_case(['one', 'hundred', 'hundred']) == None
    assert random_case(['five', 'oh', 'not_a_num']) == None
    assert random_case(['not', 'a', 'valid', 'number']) == None
