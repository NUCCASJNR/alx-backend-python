#!/usr/bin/env python3
"""
Annonated function module
"""

from typing import Union, Mapping, Any, T


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None]) -> \
                     Union[Any, T]:
    """Annotated function"""
    if key in dct:
        return dct[key]
    else:
        return default
