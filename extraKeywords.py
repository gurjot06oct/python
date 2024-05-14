import asyncio

# as - aliasing
import math as m
print(m.sqrt(25))

# async, await
async def example():
    await asyncio.sleep(1)
    print("Async function")

# from, import
from math import sqrt
print(sqrt(16))