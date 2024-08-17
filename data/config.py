from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("bot_token")  # Bot tokeni
ADMINS = env.list("admins")  # adminlar ro'yxati
IP = env.str("ip")  # Hosting ip manzili
