from aiogram import types
from aiogram.filters import Command
from loader import dp


# Help - bu kommanda botda qanday foydalanishlarni ko'rsatadi
@dp.message(Command('help'))
async def bot_help(message: types.Message):
    # text - da bu haqida ma'lumot berilmoqda
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))