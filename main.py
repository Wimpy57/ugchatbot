from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

import config
import asyncio


APP_TOKEN = config.TOKEN
bot = Bot(token=APP_TOKEN)
dp = Dispatcher()

@dp.message()
async def start(message:types.Message):
    web_app = WebAppInfo(url='asdfasdf')
    button = KeyboardButton(text='Открыть веб-приложение', web_app=web_app)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button)
    await message.answer("Нажмите кнопку ниже для запуска веб-приложения", reply_markup=keyboard)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
