import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

# Токен будет взят из переменных окружения на Render
API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        "✅ *Бот успешно запущен!*\n\n"
        "🎉 Он работает 24/7 на Render.com\n\n"
        "📌 Команды:\n"
        "/ping - проверка работы",
        parse_mode="Markdown"
    )

@dp.message(Command("ping"))
async def ping_cmd(message: Message):
    await message.answer("🏓 Pong! Бот работает!")

async def main():
    print("🤖 Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
