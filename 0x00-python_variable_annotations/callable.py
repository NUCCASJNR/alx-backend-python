#!/usr/bin/env python3

from typing import Callable

def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def perform_operation(operation: Callable[[int, int], int], a: int, b: int) -> int:
    return operation(a, b)

result1 = perform_operation(add, 5, 3)
result2 = perform_operation(subtract, 10, 4)

print(result1)
print(result2)