#!/usr/bin/env python3
""""""
import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """Returns total_time / n for wait_n() execution"""
    time_consumed: float
    start = time.perf_counter()

    await wait_n(n, max_delay)

    time_consumed = time.perf_counter() - start
    return time_consumed / n
