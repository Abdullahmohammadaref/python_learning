import pytest
import twttr

from twttr import  shorten

def test_shorten():

    assert shorten("Hello World") == "Hll Wrld"


