import pytest

from src.performance_analyzer import format_report, measure_execution


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
