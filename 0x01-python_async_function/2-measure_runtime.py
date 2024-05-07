#!/usr/bin/env python3
"""calculates the time needed for each coroutine to be executed """
import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Returns total_time / n for wait_n() execution"""
    time_consumed: float
    start = time.perf_counter()

    asyncio.run(wait_n(n, max_delay))

    time_consumed = time.perf_counter() - start
    return time_consumed / n
