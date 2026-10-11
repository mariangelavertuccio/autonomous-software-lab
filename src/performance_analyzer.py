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
