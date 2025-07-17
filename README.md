# advent-of-code-python
My solutions to the [Advent of Code](https://adventofcode.com/) problems for the years I chose to do in Python

Individual solutions located in `year##/days/day##`.

| Year | Completion Percentage             |
|------|-----------------------------------|
| 2022 | ![](https://geps.dev/progress/12) |


Note: These solutions are not intended to be elegant; I began solving Advent of Code problems in 2023
while taking a data structures course in undergrad. I originally solved multiple problems from prior 
years in Java (at [this](https://github.com/n-cipolla/advent-of-code-java/tree/main) link) but wanted
to try others in Python.


<small>Repository structure below.</small>

```
└── 'Advent of Code'
    └── year##
        ├── days
        │   ├── __init__.py
        │   ├── day01.py
        │   ├── day02.py
        │   └── ...
        ├── run_day.py
        └── tools.py
```

To run a particular day, run `run_day.py` with `argument_0` as the day number and `argument_1` as the part number, e.g.,
`python run_day.py 1 1` would run Day 1, Part 1 with the given input file.
