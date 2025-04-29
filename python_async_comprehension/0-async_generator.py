#!/usr/bin/env python3
"""this module contains a function  coroutine"""
import asyncio
import random
import typing

async def async_generator(): -> typing.Generator[float, None, None]:
    """Coroutine qui génère 10 nombres aléatoires entre 0 et 10,
    avec une pause d'une seconde entre chaque génération."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
