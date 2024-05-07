Python Async Comprehension Project

This project explores concepts related to asynchronous generators and asynchronous comprehensions in Python.

Learning Objectives
By the end of this project, you should be able to:

Explain asynchronous generators and asynchronous comprehensions without external help.
Write asynchronous generators using coroutines.
Utilize asynchronous comprehensions for collecting data from asynchronous generators.
Annotate your functions and coroutines with type hints.

Tasks:
Async Generator: Write a coroutine named async_generator that yields 10 random numbers between 0 and 10 using asynchronous waits.
Async Comprehensions: Create a coroutine called async_comprehension that collects 10 random numbers using an asynchronous comprehension over the async_generator function.
Runtime for Parallel Comprehensions: Develop a coroutine named measure_runtime that executes async_comprehension four times concurrently using asyncio.gather. The coroutine should measure and return the total runtime. Explain why the total runtime is roughly 10 seconds.
Resources
PEP 530 – Asynchronous Comprehensions (https://peps.python.org/pep-0530/)
What’s New in Python: Asynchronous Comprehensions / Generators (https://docs.python.org/)
Type-hints for generators (https://mypy.readthedocs.io/en/stable/kinds_of_types.html)
