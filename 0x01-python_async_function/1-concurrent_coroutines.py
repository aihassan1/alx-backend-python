#!/usr/bin/env python3
"""takes in 2 int arguments (in this order): n and max_delay
and returns a list of delays"""
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """spawns the wait_random function n times"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for task in range(n)]

    results = []
    for future in asyncio.as_completed(tasks):
        result = await future
        results.append(result)

    return results
