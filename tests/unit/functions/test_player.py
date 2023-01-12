# Copyright (c) 2022 CloudZero - ALL RIGHTS RESERVED - PROPRIETARY AND CONFIDENTIAL
# Unauthorized copying of this file and/or project, via any medium is strictly prohibited.
# Direct all questions to legal@cloudzero.com
import pytest

from src.common import player
from src.common.game import ResultElement

TEST_WORDS = ['shore', 'hello', 'merge', 'rehab', 'score', 'sound', 'group', 'clomp', 'aorta', 'speed', 'sweep']
ASCII1 = 'bcefghijklmopqruvwxyz'
ASCII2 = 'bcefghijklmopqrsuvwxyz'
ASCII3 = 'bcdefghijklmopqrsuvwxyz'
ASCII4 = 'bcdefghijklmnopqrsuvwxyz'
ASCII5 = 'bcdefghijklmnopqrstuvwxyz'

@pytest.mark.unit
@pytest.mark.parametrize(
    'guess,result,expected_words,word_vector', [
        ('stand', 'BBBBB', ['clomp', 'merge', 'group', 'hello'], [ASCII1, ASCII1, ASCII1, ASCII1, ASCII1]),
        ('stand', 'GBBBB', ['sweep', 'shore', 'score'], ['s', ASCII2, ASCII2, ASCII2, ASCII2]),
        ('stand', 'GBBBG', ['speed'],  ['s', ASCII3, ASCII3, ASCII3, 'd']),
        ('stand', 'GBBGG', ['sound'], ['s', ASCII4, ASCII4, 'n', 'd']),
        ('stand', 'GGBGG', [], ['s', 't', ASCII5, 'n', 'd']),
    ])
def test_apply_guess_should_reduce_word_list_for_green_results(guess, result, expected_words, word_vector):
    new_words, _ = player.apply_guess(TEST_WORDS, guess, [ResultElement(x) for x in result], word_vector)
    assert sorted(new_words) == sorted(expected_words)
