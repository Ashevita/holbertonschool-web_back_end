#!/usr/bin/env python3
""" this  module contains a async function"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait for tasks """
    tasks = []
    delays_of_tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays_of_tasks.append(delay)
    return delays_of_tasks
