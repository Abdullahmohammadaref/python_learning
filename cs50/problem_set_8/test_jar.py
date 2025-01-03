from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar_2 = Jar(5)
    assert jar_2.capacity == 5

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(11)
    assert jar.size == 11
    jar.deposit(1)
    assert jar.size == 12



def test_withdraw():
    jar = Jar()
    jar.deposit(7)
    jar.withdraw(5)
    assert jar.size == 2
    jar.withdraw(1)
    assert jar.size == 1