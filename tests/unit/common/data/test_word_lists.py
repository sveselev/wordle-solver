# Copyright (c) 2022 CloudZero - ALL RIGHTS RESERVED - PROPRIETARY AND CONFIDENTIAL
# Unauthorized copying of this file and/or project, via any medium is strictly prohibited.
# Direct all questions to legal@cloudzero.com
import pytest

from src.common.data import word_lists


@pytest.mark.unit
def test_get_valid_words_should_return_all_valid_words():
    words = word_lists.get_valid_words()
    assert len(words) == 12972


@pytest.mark.unit
def test_get_goal_words_should_return_all_goal_words():
    words = word_lists.get_goal_words()
    assert len(words) == 2315


@pytest.mark.unit
def test_all_goal_words_should_be_valid_words():
    valid_words = set(word_lists.get_valid_words())
    goal_words = set(word_lists.get_goal_words())
    assert goal_words.issubset(valid_words)
