#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random
is being called
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that takes two numbers and executes n times
    the wait_random function """
    list_of_random_numbers: List[float] = []
    for x in range(n):
        list_of_random_numbers.append(await task_wait_random(max_delay))
        list_of_random_numbers.sort()
    return list_of_random_numbers
