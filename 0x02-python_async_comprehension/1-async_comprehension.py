#!/usr/bin/env python3
""" Async Comprehension """
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Function that collects 10 random numbers using an async
        comprehensing over `async_generator`, returns them
    """

    random_numbers = [i async for i in async_generator()]
    return random_numbers
