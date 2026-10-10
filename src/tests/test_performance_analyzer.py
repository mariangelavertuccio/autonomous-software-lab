import pytest

from src.performance_analyzer import measure_execution

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
