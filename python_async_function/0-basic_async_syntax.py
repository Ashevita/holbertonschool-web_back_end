#!/usr/bin/env python3
""" this module contains a async function """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ random await excution delay """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
