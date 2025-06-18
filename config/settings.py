from dotenv import load_dotenv
import os

# Загрузка переменных из .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
SOURCE_CHANNEL_ID = int(os.getenv("SOURCE_CHANNEL_ID"))
TARGET_GROUP_ID = int(os.getenv("TARGET_GROUP_ID"))

# Проверка наличия всех переменных
if not all([BOT_TOKEN, ADMIN_ID, SOURCE_CHANNEL_ID, TARGET_GROUP_ID]):
    raise ValueError("Не все переменные окружения заданы в .env файле")