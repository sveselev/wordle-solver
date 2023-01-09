# Copyright (c) 2022 CloudZero - ALL RIGHTS RESERVED - PROPRIETARY AND CONFIDENTIAL
# Unauthorized copying of this file and/or project, via any medium is strictly prohibited.
# Direct all questions to legal@cloudzero.com
import random
from typing import List

from src.common import game
from src.common.game import ResultElement


def get_best_guess(possible_words: List[str]) -> str:
    return random.choice(possible_words)


def apply_guess(current_words: List[str], guess: str, result: List[ResultElement]) -> List[str]:
    def is_possible(word: str) -> bool:
        return all(word[n] == guess[n] for n, element in enumerate(result) if element == ResultElement.green)

    return [w for w in current_words if is_possible(w)]
