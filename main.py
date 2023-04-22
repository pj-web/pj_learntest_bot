from aiogram import Bot, Dispatcher, types
import asyncio
token = "6103193076:AAGXfD0e6ChwJTcKZ4dQop5bbeYXz7Q0Uv0"


async def echo(message: types.Message):
    print(message.text)
    await message.answer(message.text)


async def start():
    bots = Bot(token)
    dp = Dispatcher()

    dp.message.register(echo)

    await dp.start_polling(bots)

if __name__ == "__main__":
    asyncio.run(start())
