# Copyright (c) 2022 CloudZero - ALL RIGHTS RESERVED - PROPRIETARY AND CONFIDENTIAL
# Unauthorized copying of this file and/or project, via any medium is strictly prohibited.
# Direct all questions to legal@cloudzero.com
from enum import Enum
from typing import List

from toolz import countby


class ResultElement(Enum):
    green = 'G'
    yellow = 'Y'
    black = 'B'


WORD_LENGTH = 5
MAX_GUESSES = 6
WINNING_RESULT = [ResultElement.green] * WORD_LENGTH


def get_result(check_word: str, goal_word: str) -> List[ResultElement]:
    green_locations = {i for i, letter in enumerate(goal_word) if check_word[i] == letter}
    remaining_letters = [x for i, x in enumerate(goal_word) if i not in green_locations]
    remaining_letter_counts = {k: v for k, v in countby(lambda x: x, remaining_letters).items()}

    def result_for_position(n):
        if n in green_locations:
            return ResultElement.green

        letter = check_word[n]
        count = remaining_letter_counts.get(letter, 0)
        if count > 0:
            remaining_letter_counts[letter] = count - 1
            return ResultElement.yellow
        return ResultElement.black

    return [result_for_position(n) for n in range(WORD_LENGTH)]
