from aiogram.types import Message

from loader import dp


# Echo bot - bu bot kommandalari ichida yo'q xabarlar yuborilganda ishlaydi
@dp.message()
async def bot_echo(message: Message):
    await message.answer(message.text)
