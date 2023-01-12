# Copyright (c) 2022 CloudZero - ALL RIGHTS RESERVED - PROPRIETARY AND CONFIDENTIAL
# Unauthorized copying of this file and/or project, via any medium is strictly prohibited.
# Direct all questions to legal@cloudzero.com
import random
from typing import List

from src.common.game import ResultElement, WORD_LENGTH

TOPN = 10


def get_best_guess(possible_words: List[str]) -> str:
    n = TOPN if len(possible_words) > TOPN else len(possible_words)
    return random.choice(possible_words[:n])


def apply_guess(current_words: List[str], guess: str, result: List[ResultElement],
                word_vector: List[str]) -> tuple[List[str], List[str]]:

    def process_word_vector():
        yellows = set()
        for idx, element in enumerate(result):
            if element == ResultElement.green:
                word_vector[idx] = guess[idx]
            elif element == ResultElement.yellow:
                yellows.add(guess[idx])
                if len(word_vector[idx]) > 1:
                    word_vector[idx] = word_vector[idx].replace(guess[idx], '')
            elif element == ResultElement.black:
                if guess[idx] in yellows:
                    if len(word_vector[idx]) > 1:
                        word_vector[idx] = word_vector[idx].replace(guess[idx], '')
                else:
                    for i in range(WORD_LENGTH):
                        if len(word_vector[i]) > 1:
                            word_vector[i] = word_vector[i].replace(guess[idx], '')

    def is_possible(word: str) -> bool:
        if 0 in [guess[idx] in word for idx, value in enumerate(result) if value == ResultElement.yellow]:
            return False
        for letter, v_letter in zip(word, word_vector):
            if letter not in v_letter:
                return False
        return True

    process_word_vector()
    return [w for w in current_words if is_possible(w)], word_vector
