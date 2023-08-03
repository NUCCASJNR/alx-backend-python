#!/usr/bin/env python3

"""
This module contains a type-annotated function that takes in multiple data
types and returns their sum as a float
"""

from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
    a type-annotated function sum_mixed_list which takes a list mxd_lst of
    integers and floats and returns their sum as a float.
    Args:
        mxd_list: list of int and float
    """

    mxd_lst_elements_sum = 0
    for mxd_ele in mxd_lst:
        mxd_lst_elements_sum += mxd_ele
    return mxd_lst_elements_sum
