# Solutions for Advent of Code 2023

## Puzzle website
[Advent of Code 2023](https://adventofcode.com/2023)

## Setup
Create python virtual env & activate it

```sh
❯ python -m venv .venv && source .venv/bin/activate && pip install --upgrade pip setuptools
```

Install requirements

```sh
❯ python -m pip install -r requirements.txt
```


## Test
Run unit tests for a day using test runner 'pytest'

```sh
❯ cd day_01
❯ pytest -v
```

## Run
To get the results of the puzzles (part-1 and part-2) of the day

```sh
❯ cd day_01
❯ python solution.py input.txt
```

## To implement solutions for a day
Folder 'day_template' is used to create the folder for a day

```sh
❯ cp -R day_template day_01
```

## Folder structure
```sh
❯ tree day_02       
```

```
day_02  # folder for a day
├── README.md  # Puzzle (part-1 & part-2)
├── __init__.py
├── example.txt  # Example text from the puzzle (README.md) used an input for tests under test_solution.py. Sample of input.txt
├── input.txt  # Puzzle' main input.
├── solution.py  # Solution runnable as a script
└── test_solution.py  # Unit tests, utilizes example.txt
```

If there were different examples for part-1 an part-2 of the puzzle of the day, then there would be two example files (example1.txt and example2.txt)


