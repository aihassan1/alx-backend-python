#!/usr/bin/env python3
"""func that takes a coroutine and returned a task"""
import asyncio


wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """takes a maxdelay and return a task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
