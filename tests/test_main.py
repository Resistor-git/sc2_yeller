# because pytest is a mess the directory containing tests should have __init__.py, otherwise import fails
import pytest
from main import recognize_minerals, recognize_gas

# minerals and gas use same test pics

# list with pairs of screenshot and expected number; used for pytest parametrize
minerals_tst_lst = [('tests/test_150.png', 150), ('tests/test_minerals_1495.png', 1495),
                    ('tests/test_no_number.png', 'failed to recognize number')]

gas_tst_lst = [('tests/test_gas_20.png', 20), ('tests/test_150.png', 150), ('tests/test_gas_508.png', 508),
               ('tests/test_gas_4046.png', 4046), ('tests/test_no_number.png', 'failed to recognize number')]


@pytest.mark.parametrize('test_pic, expected_number', minerals_tst_lst)
def test_recognize_minerals(test_pic, expected_number):
    assert recognize_minerals(test_pic) == expected_number


@pytest.mark.parametrize('test_pic, expected_number', gas_tst_lst)
def test_recognize_gas(test_pic, expected_number):
    assert recognize_gas(test_pic) == expected_number


"""
TODO
add tests for yell
"""


