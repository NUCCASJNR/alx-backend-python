#!/usr/bin/env/python3

from typing import Callable, Iterator, Union, Optional, TYPE_CHECKING, cast

def stringify(num: int) -> str:
    return str(num)
a = 45
b = print(stringify(a))
print(type(a))
print(type(b))
print(stringify.__annotations__)


def plus(num1: int, num2: int) -> int:
    return num1 + num2

print(plus(8
           , 7))