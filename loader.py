from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode # Bot xabar matnlarini qanday usulda parse qilib berishi

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML) # Bot obyekti yaratiladi
dp = Dispatcher(bot=bot, storage=MemoryStorage()) # Botda ish jarayonini boshqarish va birlashtirish uchun Dispatcher yaratiladi
