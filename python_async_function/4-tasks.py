#!/usr/bin/env python3
""" this  module contains a async function"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ wait for tasks """
    tasks = []
    delays_of_tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays_of_tasks.append(delay)
    return delays_of_tasks
