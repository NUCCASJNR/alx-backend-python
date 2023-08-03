#!/usr/bin/env python3

"""
Ducks an iterable object
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Ducks an iterable"""
    return [(i, len(i)) for i in lst]
