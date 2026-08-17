import asyncio

async def download_file(name):
    print("download: ",name)
    await asyncio.sleep(1)
    print("download: ",name)
    return name

async def main():
    name=["filename"]
    reult1,reult2= await asyncio.gather(download_file("download_file1"),download_file("download_file2"))
    print(reult1,':',reult2)
    name += [reult1,reult2]
    print(name)

asyncio.run(main())

'''
simple analogy:
                Multithreading            |  Asyncio
workers:    Multiple cashiers at shop     | 1 casher, but serves next customer while waiting for card payment
CPU usage:  Higher                        | Lower
Best for :  Cpu-heavy tasks (calculations)| Waiting tasks (API calls, file i/o)
Complexity: Harder (race condition, locks)| Simpler
'''