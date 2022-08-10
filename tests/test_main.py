# because pytest is a mess the directory containing tests should have __init__.py, otherwise import fails
import pytest
from main import recognize_minerals, recognize_gas, yell_minerals

# minerals and gas use same test pics

# def test_recognize_minerals():
#     assert recognize_minerals('tests/test_150.png') == 150
#     assert recognize_minerals('tests/test_minerals_1495.png') == 1495
#     assert recognize_minerals('tests/test_no_number.png') == 'failed to recognize number'
#
#
# def test_recognize_gas():
#     assert recognize_gas('tests/test_150.png') == 150
#     assert recognize_gas('tests/test_minerals_1495.png') == 1495
#     assert recognize_gas('tests/test_no_number.png') == 'failed to recognize number'


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


# how to check that function does something ???
# def test_yell_minerals():
#     assert yell_minerals(0) is None
#     assert yell_minerals(500) is None
#     assert yell_minerals(1001) ==
#     assert yell_minerals('failed to recognize number') is None

