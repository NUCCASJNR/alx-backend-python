#!/usr/bin/env python3

"""
This module contains annotated list of floats
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Takes a list input_list of floats
    as argument and returns their sum as a float.
    """
    sum_of_list_elements = 0
    for iterator in input_list:
        sum_of_list_elements = sum_of_list_elements + iterator
    return (float(sum_of_list_elements))
