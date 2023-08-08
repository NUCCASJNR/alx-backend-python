#!/usr/bin/python3

def number_generator(limit):
    for num in range(0, limit + 1):
        yield num
gen = number_generator(5)
for num in gen:
    print(num)
