import pytest
from utils.replace_misheards import replace_misheards


def random_case(command):
    return replace_misheards(command) 

def test_random_case():
    assert random_case('ride terry five') == ['right', 'turn', 'five']
    assert random_case('go forward to fifty') == ['go', 'forward', 'two', 'fifty']
    assert random_case('turn left through eighty') == ['turn', 'left', 'three', 'eighty']
    assert random_case('lottery') == ['battery']
    assert random_case('turn ride o for fifty') == ['turn', 'right', 'oh', 'four', 'fifty']
    assert random_case('go for or to sixty') == ['go', 'forward', 'two', 'sixty']
    assert random_case('turning ride party') == ['turn', 'right', 'forty']
