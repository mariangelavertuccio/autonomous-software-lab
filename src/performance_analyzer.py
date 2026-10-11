from time import perf_counter
from collections.abc import Callable
from typing import Any


def measure_execution(
    function: Callable[..., Any],
    *args: Any,
    repetitions: int = 5,
    **kwargs: Any,
) -> dict[str, float]:
    """Measure repeated executions of a function."""

    if repetitions < 1:
        raise ValueError("repetitions must be at least 1")

    durations = []

    for _ in range(repetitions):
        start = perf_counter()
        function(*args, **kwargs)
        elapsed = perf_counter() - start
        durations.append(elapsed)

    return {
        "minimum_seconds": min(durations),
        "maximum_seconds": max(durations),
        "average_seconds": sum(durations) / len(durations),
    }

def format_report(metrics: dict[str, float]) -> str:
    """Format execution metrics as a readable report."""

    return (
        "Performance Report\n"
        f"Minimum: {metrics['minimum_seconds']:.6f} seconds\n"
        f"Maximum: {metrics['maximum_seconds']:.6f} seconds\n"
        f"Average: {metrics['average_seconds']:.6f} seconds"
    )

def compare_functions(
    first_function: Callable[..., Any],
    second_function: Callable[..., Any],
    *args: Any,
    repetitions: int = 5,
    **kwargs: Any,
) -> dict[str, Any]:
    """Compare the execution times of two functions."""

    first_result = measure_execution(
        first_function,
        *args,
        repetitions=repetitions,
        **kwargs,
    )

    second_result = measure_execution(
        second_function,
        *args,
        repetitions=repetitions,
        **kwargs,
    )

    if first_result["average_seconds"] < second_result["average_seconds"]:
        faster_function = "first_function"
    elif second_result["average_seconds"] < first_result["average_seconds"]:
        faster_function = "second_function"
    else:
        faster_function = "tie"

    return {
        "first_function": first_result,
        "second_function": second_result,
        "faster_function": faster_function,
    }

def format_comparison_report(comparison: dict[str, Any]) -> str:
    """Format function comparison results as a readable report."""

    first = comparison["first_function"]
    second = comparison["second_function"]
    faster = comparison["faster_function"]

    return (
        "Function Comparison Report\n"
        f"First function average: {first['average_seconds']:.6f} seconds\n"
        f"Second function average: {second['average_seconds']:.6f} seconds\n"
        f"Faster function: {faster}"
    )
