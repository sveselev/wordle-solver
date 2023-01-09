# feature-wordle-solver

## Problem Statement

We want you to love working at CloudZero. The goal of this work sample is to simulate working at CloudZero in the comfort of your own home or coffee shop.  Of course, we're not actually building Wordle solvers, but we think this problem is fun, and hope you do to. We ask that you take some time to look at the issue we've added and submit a PR to resolve it. We understand that your time is valuable, so this should only take a couple hours. This is a guideline, not a limit -- you don't need to time yourself or to do the problem in one sitting.

## About Wordle
If you are not familiar with the game [Wordle](https://www.nytimes.com/games/wordle/index.html), you try to guess a "goal" word in six tries.  After each attempt the game shows you how close you are by marking each letter:
* Green - this is the correct letter, in the correct location
* Yellow - this letter is in the word, but the wrong location
* Black - this letter is not in the word

### Duplicate Letters
Each letter in the guess which is marked green or yellow is associated with a _unique_ letter in the goal word. This is important if the guess or goal words have a repeated letter.  For example:
```
Goal:   FOODY
Guess:  DODGE
Result: YGBBB
```
Note that the first "D" in DODGE is marked yellow, but the second "D" is marked black.  This is because the goal word FOODY only has one "D".  You can think of the first "D" in DODGE as "using up" the "D" in FOODY.

However:
```
Goal:   TOTAL
Guess:  STUNT
Result: BYBBY
```
In this case both "T"s are marked yellow because there are two "T"s in the goal.

## Solver
This Wordle Solver plays simulated games of Wordle and outputs statistics on how well it performs: success rate (how often it guessed the correct word in at most six tries) and average number of guesses.

### game.py
This module implements the basic game rules.  For a given guess and goal word it outputs the result (green, yellow, black) for each letter.

### simulator.py
This module implements running the simulation.  It will play games of Wordle by picking a random goal word and then gathers statistics on the overall performance -- how often did it win and how many guesses were needed.

### player.py
This module implements the "player" -- the code responsible for choosing each guess.  It consists of two functions:
* `get_best_guess()` -- given a list of possible words, choose the next best guess.
* `apply_guess()` -- given a list of words, a guess, and the result, return a new list of possible words.

## Usage

### Branch

Create a new branch from `develop`

### Working on the Code

#### Python Prerequisites

This work sample requires Python 3.8 or greater and `pip` for dependencies. Please have Python 3.8+ and pip available in your shell when you start working on this project.

#### Python Environment
> NOTE: There are many ways to configure a Python environment. We tried to make this sample as self-contained as possible and work on Mac, Linux, and Windows; to that end, the Makefile or Powershell script will create a virtual environment directory, venv, and use it for all operations. If you decide to use your own virtual environment, you may run into issues.

> NOTE: Most importantly, if you spend more than 5 minutes setting up the environment for this project, please stop and reach out to us. It means this project needs improvement and we will help unblock you. We are here to help you join our team and not to waste your time.

##### Docker

In the case that you want to use Docker to run this application:

```
docker build -t takehome-wordle .
docker run -it -v `pwd`:/app takehome-wordle bash
```

You now have an interactive shell inside the Docker container, you can follow the Linux steps below.

Create a virtual environment in a folder named `venv` and install the dependencies from `requirements.txt` into it:
###### MacOS / Linux
```
make init
```
###### Windows
```
.\make.ps1 init
```

#### Running the Code

Run the Wordle solver with a specific goal word:
###### MacOS / Linux
```
make run goal=<word>
```
###### Windows
```
.\make.ps1 run -goal <word>
```

Or evaluate the overall performance with a bunch of random goal words:
###### MacOS / Linux
```
make evaluate count=<number of words>
```
###### Windows
```
.\make.ps1 evaluate -count <number of words>
```

Go ahead and try it: `make evaluate count=1000`  As you will see, it's currently not a very good player.

### Address the Issue

See ISSUE-1 in this repository for the area we want to improve. The `get_best_guess` function in `src/common/player.py` isn't very good and we want to make it better. What we're looking for is not necessarily the fastest or cleverest algorithm, but rather code that's clean, robust, readable, and simple.

### Submit a PR

Once you've addressed [ISSUE-1](../../issues/1), push your branch and submit a PR to `develop`.

### Send us a link to your PR

Send a link to your PR to your hiring manager.
