#!/usr/bin/env python3
"""function that takes an arg (int )
waits for a random delay and return the
time of the random delay
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """wait for a random amount of time between 0 and max_delay"""
    actual_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(actual_delay)
    return actual_delay
