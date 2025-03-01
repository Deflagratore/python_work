import pytest
from employer import Employ 

@pytest.fixture
def test_get_raise():
    employ = Employ("John", "Doe", 50000)
    assert employ.get_raise() == 55000

def test_custom_raise(test_get_raise):
    employ = Employ("John", "Doe", 50000)
    salary = employ.get_raise(10000)
    assert salary == 60000