# Autonomous Software Lab

A Python-based project for automated testing, performance measurement, and software quality analysis.

## Overview

Autonomous Software Lab is a personal software engineering project focused on software testing, performance analysis, and continuous improvement.

The project provides tools to measure function execution times, compare alternative implementations, and generate readable performance reports.

It also uses automated tests and continuous integration to help verify code correctness as the project evolves.

## Features

- **Execution time measurement:** Measure the minimum, maximum, and average execution time of a function.
- **Function comparison:** Compare the execution times of two functions.
- **Performance improvement analysis:** Calculate the relative execution-time improvement of the faster function.
- **Readable reports:** Generate text reports containing performance metrics and comparison results.
- **Automated testing:** Use pytest to verify expected behavior.
- **Continuous integration:** Run automated tests through GitHub Actions.

## Technologies

- Python
- pytest
- Git and GitHub
- GitHub Actions

## Project Structure

```text
autonomous-software-lab/
├── src/
│   ├── performance_analyzer.py
│   └── tests/
│       └── test_performance_analyzer.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── requirements.txt
└── README.md
```

## Getting Started

### Requirements

- Python 3.12 or compatible version
- pip

### Install Dependencies

Clone the repository and enter the project directory:

```bash
git clone YOUR_REPOSITORY_URL
cd autonomous-software-lab
```

Replace `YOUR_REPOSITORY_URL` with the actual clone URL of your repository before running the command.

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Running the Tests

Run the automated test suite with:

```bash
python -m pytest
```

GitHub Actions also runs the tests automatically when changes are pushed or a pull request is opened.

## Example

The performance analyzer can measure the execution time of a function:

```python
from src.performance_analyzer import measure_execution


def example_function():
    return sum(range(1000))


metrics = measure_execution(example_function, repetitions=5)

print(metrics)
```

The result contains the minimum, maximum, and average execution time in seconds.

Functions can also be compared:

```python
from src.performance_analyzer import (
    compare_functions,
    format_comparison_report,
)


def first_function():
    return sum(range(1000))


def second_function():
    return sum(range(2000))


comparison = compare_functions(
    first_function,
    second_function,
    repetitions=5,
)

print(format_comparison_report(comparison))
```

The comparison report includes execution-time metrics and the relative improvement percentage of the faster function.

## Current Status

The project includes execution-time measurement, function comparison, performance reporting, automated tests, and a GitHub Actions workflow.

Additional capabilities, such as memory profiling, static code analysis, and performance regression detection, may be explored in future iterations.

## Engineering Philosophy

**Measure. Verify. Understand. Improve.**

The goal is to develop a practical understanding of software quality, reproducible testing, and performance analysis through iterative development.
