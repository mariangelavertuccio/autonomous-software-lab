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

    first_average = first_result["average_seconds"]
    second_average = second_result["average_seconds"]

    if first_average < second_average:
        faster_function = "first_function"
        improvement_percentage = (
            (second_average - first_average) / second_average
        ) * 100
    elif second_average < first_average:
        faster_function = "second_function"
        improvement_percentage = (
            (first_average - second_average) / first_average
        ) * 100
    else:
        faster_function = "tie"
        improvement_percentage = 0.0

    return {
        "first_function": first_result,
        "second_function": second_result,
        "faster_function": faster_function,
        "improvement_percentage": improvement_percentage,
    }

def format_comparison_report(comparison: dict[str, Any]) -> str:
    """Format a readable report comparing two functions."""

    first = comparison["first_function"]
    second = comparison["second_function"]
    faster = comparison["faster_function"]
    improvement = comparison["improvement_percentage"]

    if faster == "tie":
        conclusion = "Both functions have the same average execution time."
    else:
        conclusion = (
            f"The faster function is: {faster} "
            f"({improvement:.2f}% less execution time)"
        )

    return (
        "Function Comparison Report\n"
        "==========================\n"
        "\n"
        "First function:\n"
        f"  Minimum: {first['minimum_seconds']:.6f} seconds\n"
        f"  Maximum: {first['maximum_seconds']:.6f} seconds\n"
        f"  Average: {first['average_seconds']:.6f} seconds\n"
        "\n"
        "Second function:\n"
        f"  Minimum: {second['minimum_seconds']:.6f} seconds\n"
        f"  Maximum: {second['maximum_seconds']:.6f} seconds\n"
        f"  Average: {second['average_seconds']:.6f} seconds\n"
        "\n"
        f"Improvement: {improvement:.2f}%\n"
        f"Conclusion: {conclusion}"
    )
