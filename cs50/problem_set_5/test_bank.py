import bank

from bank import value

def test_default():
    assert value("welcome, how can i help you today") == "$100"
def test_startwith_hello():
    assert value("hello, how can i help you today.") == "$0"
def test_uppercase():
    assert value("Hello, how can i help you today.") == "$0"
def test_startwith_h():
    assert value("hi, how can i help you today.") == "$20"

