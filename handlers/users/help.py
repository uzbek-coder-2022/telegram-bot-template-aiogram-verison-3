from aiogram import types
from aiogram import Router
from aiogram.filters import Command

help_router = Router()

# Help - bu kommanda botda qanday foydalanishlarni ko'rsatadi
@help_router.message(Command(commands=["help"]))
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "1. /start - Botni ishga tushirish",
            "2. /help - Yordam")

    await message.answer("\n".join(text))
