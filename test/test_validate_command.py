import pytest
from utils import validate_command as vc
""" Not testing for empty string commands- those are filtered out during speech recognitions.
"""

def empty_case(command):
    return vc.validate_command(command)

def test_empty_case():
    assert empty_case([]) == ['empty']


def one_word_case(command):
    return vc.is_valid_one_word_command(command) 

def test_one_word_case():
    assert one_word_case(['exit']) == ['exit']
    assert one_word_case(['land']) == ['land']
    assert one_word_case(['muttery']) == ['invalid']
    assert one_word_case(['go']) == ['invalid']
    assert one_word_case(['set']) == ['invalid']
    assert one_word_case(['hundred']) == ['invalid']


def two_words_case(command):
    return vc.is_valid_two_words_command(command)

def test_two_words_case():
    assert two_words_case(['take', 'off']) == ['take', 'off']
    assert two_words_case(['take', 'off']) == ['take', 'off']
    assert two_words_case(['stop', 'video']) == ['stop', 'video']
    assert two_words_case(['flip', 'forward']) == ['flip', 'forward']
    assert two_words_case(['flip', 'back']) == ['flip', 'back']
    assert two_words_case(['flip', 'left']) == ['flip', 'left']
    assert two_words_case(['flip', 'right']) == ['flip', 'right']
    assert two_words_case(['turn', 'back']) == ['turn', 'back']
    assert two_words_case(['set', 'speed']) == ['invalid']
    assert two_words_case(['go', 'forward']) == ['invalid']
    assert two_words_case(['stop', 'vid']) == ['invalid']
    assert two_words_case(['flip', 'video']) == ['invalid']
    assert two_words_case(['totally', 'inappropriate']) == ['invalid']



def three_plus_words_case(command):
    return vc.is_valid_three_plus_words_command(command)

def test_three_plus_words_case():
    assert three_plus_words_case(['go', 'forward', 'two', 'fifty']) == ['go', 'forward', 'two', 'fifty']
    assert three_plus_words_case(['go', 'forward', 'hundred']) == ['go', 'forward', 'hundred']
    assert three_plus_words_case(['set', 'speed', 'eighty']) == ['set', 'speed', 'eighty']
    assert three_plus_words_case(['set', 'speed', 'zero', 'fifty', 'five']) == ['invalid']
    assert three_plus_words_case(['set', 'speed']) == ['invalid']



def random_case(command):
    return vc.validate_command(command)

def test_random_case():
    assert random_case(['battery']) == ['battery']
    assert random_case(['take', 'off']) == ['take', 'off']
    assert random_case(['turn', 'back']) == ['turn', 'back']
    assert random_case(['go', 'forward', 'seven', 'hundred']) == ['go', 'forward', 'seven', 'hundred']
    assert random_case(['mercury']) == ['invalid']
    assert random_case(['set', 'speed']) == ['invalid']
    assert random_case(['go', 'forward']) == ['invalid']
    assert random_case(['stop', 'vid']) == ['invalid']
    assert random_case(['go', 'forward', 'seven', 'hundred', 'fifty']) == ['invalid']
    assert random_case(['totally', 'inappropriate']) == ['invalid']
    assert random_case(['totally', 'inappropriate']) == ['invalid']
