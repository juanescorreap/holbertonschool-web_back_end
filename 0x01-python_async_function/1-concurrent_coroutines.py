#!/usr/bin/env python3
"""
async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. You will spawn wait_random
n times with the specified max_delay.
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that takes two numbers and executes n times
    the wait_random function """
    list_of_random_numbers: List[float] = []
    for x in range(n):
        list_of_random_numbers.append(await wait_random(max_delay))
    return sorted(list_of_random_numbers)
