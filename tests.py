import asyncio as aio


async def a():
    print('a1')
    await aio.sleep(10)
    print('a2')
    return True


async def aa():
    print('aa1')
    await aio.sleep(7)
    print('aa2')
    return True


async def aaa():
    print('aaa1')
    await aio.sleep(9)
    print('aaa2')
    return True


async def aaaa():
    print('aaaa1')
    await aio.sleep(5)
    print('aaaa2')


async def sus1():
    await aio.gather(aaaa(), aa())


async def sus2():
    await aio.gather(a(), aaa())


async def main():
    await aio.gather(sus1(), sus2())
    await aio.sleep(2)


if __name__ == '__main__':
    aio.run(main())
