# Copyright (c) 2022 CloudZero - ALL RIGHTS RESERVED - PROPRIETARY AND CONFIDENTIAL
# Unauthorized copying of this file and/or project, via any medium is strictly prohibited.
# Direct all questions to legal@cloudzero.com

from functools import lru_cache
from typing import List
from src.common.game import MAX_FREQ

@lru_cache
def _get_lines(file: str) -> List[str]:
    with open(file) as f:
        return [x.strip() for x in f]


def get_valid_words() -> List[str]:
    return _get_lines('data/words.txt')


def get_goal_words() -> List[str]:
    return _get_lines('data/goal.txt')


def _get_head(file: str, top: int) -> List[str]:
    with open(file) as f:
        return [next(f) for x in range(top)]


def get_sorted_words() -> List[str]:
    valid_words = get_valid_words()
    word_freq_lst = _get_head('data/word_freq.txt', MAX_FREQ)
    sorted_words = [split[0] for split in [wf.split(' ') for wf in word_freq_lst] if split[0] in valid_words]
    sorted_words.extend([w for w in valid_words if w not in sorted_words])
    return sorted_words
