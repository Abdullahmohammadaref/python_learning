import fuel
import pytest

from fuel import convert
from fuel import gauge


def test_errors():

    with pytest.raises(ZeroDivisionError):
        convert("3/0")

    with pytest.raises(ValueError):
        convert("cat/fish")

def test_input():

    assert   convert ("1/100") == 1 and gauge(1) == "E"
    assert convert ("1/5") == 20 and gauge(20) == "20%"
    assert convert ("99/100") == 99 and gauge(99) == "F"
