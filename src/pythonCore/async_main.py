import asyncio
# from src.pythonCore.Generator import gencube

async def task(name, delay):
    print(f"Start {name}")
    await asyncio.sleep(delay)
    print(f"End {name}")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1)
    )

asyncio.run(main())



#asyncio : is Python’s library for writing single-threaded, non-blocking, concurrent code using async/await.
#Key idea: one thread, many tasks, no waiting.
