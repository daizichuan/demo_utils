import asyncio

async def get_number(n):
    await asyncio.sleep(1)  # 模拟耗时操作
    return n

async def main():
    tasks = []
    for i in range(100):
        tasks.append(asyncio.create_task(get_number(i)))
    numbers = await asyncio.gather(*tasks)
    print(numbers)

if __name__ == '__main__':
    asyncio.run(main())


# import asyncio
#
# async def task(n):
#     await asyncio.sleep(1)  # 模拟耗时操作
#     return n
#
# async def main():
#     tasks = [asyncio.create_task(task(i)) for i in range(100)]
#     results = await asyncio.gather(*tasks)
#     print(results)
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())
#     loop.close()