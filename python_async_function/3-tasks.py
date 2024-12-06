#!/usr/bin/env python3
""" this mofule contains a function """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ function that returns asyncio task """
    return asyncio.create_task(wait_random(max_delay))
