#!/usr/bin/env python3
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Attend un délai aléatoire entre 0 et max_delay secondes, puis le retourne.

    Args:
        max_delay (int): Durée maximale du délai en secondes. Valeur par défaut : 10.

    Returns:
        float: Durée du délai aléatoire.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
