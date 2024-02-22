from aiogram.types import Message
from aiogram.filters import CommandStart

from loader import dp

# Start - bu kommanda botni ishga tushirish
# hamda yangilanishlarni qabul qilish uchun ham ishlaydi
@dp.message(CommandStart())
async def bot_start(message: Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    print(dp.get())
