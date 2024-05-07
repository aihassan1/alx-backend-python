This is the README file for a project on Python Asynchronous Programming.

Project Title: Python Async Functionalities

Project Description:

This project focuses on exploring asynchronous programming concepts in Python. It covers tasks like creating asynchronous coroutines, running them concurrently, measuring execution time, and working with asyncio Tasks.

Learning Objectives:

By completing this project, i was able to:

Explain async and await syntax in Python.
Execute an async program using asyncio.
Run multiple coroutines concurrently.
Create asyncio tasks.
Utilize the random module.
Project Requirements:

Tasks:
Implement an asynchronous coroutine named wait_random that waits for a random delay (between 0 and the provided max_delay) and returns the delay value. It should use the random module.
Create an async function named wait_n that takes two integer arguments (n and max_delay). It should spawn wait_random n times and return a list of delays in ascending order (without using sort).
Develop a function named measure_time that calculates the total execution time for wait_n(n, max_delay) and returns the average execution time per coroutine. It should utilize the time module.
Write a function named task_wait_random that takes an integer max_delay and returns an asyncio.Task object (without using async syntax).
Create a new function named task_wait_n that is similar to wait_n but uses task_wait_random to call the coroutines.
Resources:

Async IO in Python: A Complete Walkthrough https://realpython.com/async-io-python/
asyncio - Asynchronous I/O https://docs.python.org/3/library/asyncio.html
random.uniform https://docs.python.org/3/library/random.html
