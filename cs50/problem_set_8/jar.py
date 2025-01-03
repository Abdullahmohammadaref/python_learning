class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Jar capacity must be a none-negative integer")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return self.size * "🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Cannot deposit more than capacity")
        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError("there aren’t that many cookies in the cookie jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

