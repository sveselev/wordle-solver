# Copyright (c) 2022 CloudZero - ALL RIGHTS RESERVED - PROPRIETARY AND CONFIDENTIAL
# Unauthorized copying of this file and/or project, via any medium is strictly prohibited.
# Direct all questions to legal@cloudzero.com
import random
import statistics
from typing import NamedTuple, List, Optional

from toolz import count, iterate, take

from src.common import player, game
from src.common.data import word_lists
from src.common.game import ResultElement, WINNING_RESULT, MAX_GUESSES
from src.common.util import takeuntil

MAX_ATTEMPTS = 10


class Attempt(NamedTuple):
    new_possible_words: List[str]
    guess: Optional[str] = None
    result: Optional[List[ResultElement]] = None

    @property
    def is_winning_attempt(self) -> bool:
        return self.result == WINNING_RESULT


class EvaluationResult(NamedTuple):
    failure_rate: float
    average_guesses: float
    average_guesses_for_win: Optional[float]


def simulate(i=0, goal=None, show_tries=False):
    goal = goal or random.choice(word_lists.get_goal_words())

    def get_next_attempt(last_attempt: Attempt):
        words = last_attempt.new_possible_words
        guess = player.get_best_guess(words)
        result = game.get_result(guess, goal)
        new_possible_words = player.apply_guess(words, guess, result)
        return Attempt(guess=guess, result=result, new_possible_words=new_possible_words)

    first_attempt = get_next_attempt(Attempt(new_possible_words=word_lists.get_valid_words()))
    possible_attempts = iterate(get_next_attempt, first_attempt)
    attempts = list(take(MAX_ATTEMPTS, takeuntil(lambda x: x.is_winning_attempt, possible_attempts)))

    if show_tries:
        for attempt in attempts:
            print(f'{attempt.guess} => {"".join([x.value for x in attempt.result])}')

    guesses = [x.guess for x in attempts]
    print(f'{i}) {goal} => {guesses}')
    return guesses


def evaluate(total_simulations: int) -> EvaluationResult:
    simulations = [simulate(i) for i in range(total_simulations)]
    numbers_of_guesses = [len(x) for x in simulations]
    guesses_for_win = [x for x in numbers_of_guesses if x <= MAX_GUESSES]
    return EvaluationResult(
        failure_rate=count(x for x in numbers_of_guesses if x > MAX_GUESSES) / total_simulations,
        average_guesses=statistics.mean(numbers_of_guesses),
        average_guesses_for_win=statistics.mean(guesses_for_win) if guesses_for_win else None
    )
