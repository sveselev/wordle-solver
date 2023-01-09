# Copyright (c) 2022 CloudZero - ALL RIGHTS RESERVED - PROPRIETARY AND CONFIDENTIAL
# Unauthorized copying of this file and/or project, via any medium is strictly prohibited.
# Direct all questions to legal@cloudzero.com

import argparse
import sys

from src.common import simulator


def _parse_args(args):
    parser = argparse.ArgumentParser(description='Calculate Budgets')
    parser.add_argument('--goal', type=str, help='Goal word to test.')
    parser.add_argument('--evaluate', type=int,
                        help='Run a number of random iterations to evaluate the overall performance.')
    return parser.parse_args(args)


def solve_for_goal(goal: str):
    simulator.simulate(goal=goal, show_tries=True)


def run_evaluation(iterations: int):
    result = simulator.evaluate(iterations)
    print(f'''
Failure Rate: {result.failure_rate * 100}%
Average Guesses: {result.average_guesses}
Average Guesses For Win: {result.average_guesses_for_win}''')


if __name__ == '__main__':
    args = _parse_args(sys.argv[1:])
    if args.goal:
        solve_for_goal(args.goal)

    if args.evaluate:
        run_evaluation(args.evaluate)
