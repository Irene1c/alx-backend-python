#!/usr/bin/env python3
"""  Run time for four parallel comprehensions """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Function that measures the total runtime and return it """

    start_time = time.time()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    end_time = time.time()
    runtime = end_time - start_time
    return runtime
