#!/usr/bin/env python3
"""doc string """

import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """should measure the total runtime and return for execution"""
    start = time.perf_counter()

    tasks = [asyncio.create_task(async_comprehension()) for task in range(0, 4)]
    await asyncio.gather(*tasks)
    time_elapsed = time.perf_counter() - start
    return time_elapsed
