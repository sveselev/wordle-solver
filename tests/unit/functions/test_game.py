# Copyright (c) 2022 CloudZero - ALL RIGHTS RESERVED - PROPRIETARY AND CONFIDENTIAL
# Unauthorized copying of this file and/or project, via any medium is strictly prohibited.
# Direct all questions to legal@cloudzero.com
import pytest

from src.common import game


@pytest.mark.unit
@pytest.mark.parametrize(
    'guess,goal,expected_result', [
        ('circs', 'leafy', 'BBBBB'),
        ('fuddy', 'leafy', 'YBBBG'),
        ('gloze', 'leafy', 'BYBBY'),
        ('brand', 'incur', 'BYBYB'),
        ('shrub', 'torus', 'YBGGB'),
        ('shrub', 'shrub', 'GGGGG'),
    ])
def test_get_result_should_return_correct_result_for_guess_and_goal(guess, goal, expected_result):
    result = game.get_result(guess, goal)
    result_str = ''.join(x.value for x in result)
    assert result_str == expected_result


@pytest.mark.unit
@pytest.mark.parametrize(
    'guess,goal,expected_result', [
        ('steer', 'cheer', 'BBGGG'),
        ('steer', 'corse', 'YBYBY'),
        ('rears', 'voars', 'BBGGG'),
        ('rears', 'river', 'GYBYB')
    ])
def test_get_result_should_return_correct_result_for_duplicate_letters(guess, goal, expected_result):
    result = game.get_result(guess, goal)
    result_str = ''.join(x.value for x in result)
    assert result_str == expected_result
