import time
import asyncio


async def task1():
    print('Task 1 Started')
    await asyncio.sleep(2)
    print('Task 2 started')

def task2():
    print('Task 3 Started')
    print('Task 4 started')

asyncio.run(task1())
task2()