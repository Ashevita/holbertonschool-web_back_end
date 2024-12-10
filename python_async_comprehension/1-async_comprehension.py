#!/usr/bin/env python3
"""Module contenant une fonction async_comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collecte 10 nombres aléatoires générés par async_generator."""
    return [number async for number in async_generator()]
