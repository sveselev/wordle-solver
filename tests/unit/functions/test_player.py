# Copyright (c) 2022 CloudZero - ALL RIGHTS RESERVED - PROPRIETARY AND CONFIDENTIAL
# Unauthorized copying of this file and/or project, via any medium is strictly prohibited.
# Direct all questions to legal@cloudzero.com
import pytest

from src.common import player
from src.common.game import ResultElement

TEST_WORDS = ['sasin', 'caron', 'shend', 'rehab', 'palps', 'seeld', 'calks', 'clomp', 'aorta', 'holds']


@pytest.mark.unit
@pytest.mark.parametrize(
    'guess,result,expected_words', [
        ('stand', 'BBBBB', TEST_WORDS),
        ('stand', 'GBBBB', ['sasin', 'shend', 'seeld']),
        ('stand', 'GBBBG', ['shend', 'seeld']),
        ('stand', 'GBBGG', ['shend']),
        ('stand', 'GGBGG', []),
    ])
def test_apply_guess_should_reduce_word_list_for_green_results(guess, result, expected_words):
    new_words = player.apply_guess(TEST_WORDS, guess, [ResultElement(x) for x in result])
    assert sorted(new_words) == sorted(expected_words)
