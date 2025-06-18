from aiogram import Router, F
from aiogram.filters import Command
from config.settings import ADMIN_ID
import logging

router = Router()
logger = logging.getLogger(__name__)

# Фильтр для команд от админа
async def is_admin(message):
    return message.from_user.id == ADMIN_ID

# Команда /start
@router.message(Command("start"), is_admin)
async def cmd_start(message):
    logger.info(f"Пользователь {message.from_user.id} отправил команду /start")
    await message.answer("Привет! Я бот для автоматического постинга. Используй /help для списка команд.")

# Обработка команд от неадминов
@router.message(Command("start"))
async def cmd_start_non_admin(message):
    logger.warning(f"Неавторизованный пользователь {message.from_user.id} попытался использовать /start")
    await message.answer("У вас нет доступа к этому боту.")