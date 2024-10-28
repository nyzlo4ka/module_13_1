import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for i in range(1, 6):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    tasks = [
        start_strongman('Нафаня', 2),
        start_strongman('Вовочка', 3),
        start_strongman('Кузя', 4)
    ]
    await asyncio.gather(*tasks)
asyncio.run(start_tournament())
