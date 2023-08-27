#!/usr/bin/env python3

def add(x, y):
    try:
        if isinstance(x, int) and isinstance(y, int):
            return x + y
    except TypeError:
        return f"Typeof x and y must be an integer"

def square(x: int | float)-> int | float:
    return x * x

class ReadOnly:
    @property
    def read_only(self):
        return 42

if __name__ == "__main__":
    read = ReadOnly()
    print(read.read_only)
    print(add(1, 3))
    print(square(7))