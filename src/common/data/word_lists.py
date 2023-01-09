# Copyright (c) 2022 CloudZero - ALL RIGHTS RESERVED - PROPRIETARY AND CONFIDENTIAL
# Unauthorized copying of this file and/or project, via any medium is strictly prohibited.
# Direct all questions to legal@cloudzero.com

from functools import lru_cache
from typing import List


@lru_cache
def _get_lines(file: str) -> List[str]:
    with open(file) as f:
        return [x.strip() for x in f]


def get_valid_words() -> List[str]:
    return _get_lines('data/words.txt')


def get_goal_words() -> List[str]:
    return _get_lines('data/goal.txt')
