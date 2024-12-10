#!/usr/bin/env python3
""" this module contains a function  coroutine"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Mesure le temps nécessaire pour exécuter
    async_comprehension quatre fois en parallèle."""
    start_time = time.perf_counter()
    # Exécute quatre fois async_comprehension en parallèle
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    end_time = time.perf_counter()
    return end_time - start_time
