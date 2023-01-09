# Copyright (c) 2022 CloudZero - ALL RIGHTS RESERVED - PROPRIETARY AND CONFIDENTIAL
# Unauthorized copying of this file and/or project, via any medium is strictly prohibited.
# Direct all questions to legal@cloudzero.com
from typing import Callable, Any, List, Iterable


def iterate_with_args(func: Callable, input: Any, arg_list: List[Iterable[Any]]):
    next_input = input
    for args in arg_list:
        yield next_input
        next_input = func(input, *args)


def takeuntil(pred: Callable[[Any], bool], seq: Iterable[Any]):
    it = iter(seq)
    while True:
        val = next(it)
        yield val
        if pred(val):
            break
