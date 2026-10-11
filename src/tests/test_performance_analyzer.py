import pytest

from src.performance_analyzer import (
    compare_functions,
    format_comparison_report,
    format_report,
    measure_execution,
)


def test_measure_execution_returns_valid_metrics():
    def add_numbers(a, b):
        return a + b

    result = measure_execution(
        add_numbers,
        2,
        3,
        repetitions=3,
    )

    assert result["minimum_seconds"] >= 0
    assert result["maximum_seconds"] >= result["minimum_seconds"]
    assert result["minimum_seconds"] <= result["average_seconds"]
    assert result["average_seconds"] <= result["maximum_seconds"]


def test_measure_execution_rejects_invalid_repetitions():
    with pytest.raises(ValueError):
        measure_execution(lambda: None, repetitions=0)


def test_format_report_contains_execution_metrics():
    metrics = {
        "minimum_seconds": 0.1,
        "maximum_seconds": 0.5,
        "average_seconds": 0.3,
    }

    report = format_report(metrics)

    assert "Performance Report" in report
    assert "Minimum: 0.100000 seconds" in report
    assert "Maximum: 0.500000 seconds" in report
    assert "Average: 0.300000 seconds" in report

def test_compare_functions_returns_valid_results():
def first_function():
return sum(range(100))

def second_function():
    return sum(range(200))
result = compare_functions(
    first_function,
    second_function,
    repetitions=3,
)
assert "first_function" in result
assert "second_function" in result
assert result["faster_function"] in (
    "first_function",
    "second_function",
    "tie",
)

def test_format_comparison_report_contains_results():
results = {
“first_function”: {
“minimum_seconds”: 0.1,
“maximum_seconds”: 0.3,
“average_seconds”: 0.2,
},
“second_function”: {
“minimum_seconds”: 0.2,
“maximum_seconds”: 0.4,
“average_seconds”: 0.3,
},
“faster_function”: “first_function”,
}

report = format_comparison_report(results)
assert "Function Comparison Report" in report
assert "First function average: 0.200000 seconds" in report
assert "Second function average: 0.300000 seconds" in report
assert "first_function is faster." in report
