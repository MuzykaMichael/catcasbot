import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
import json
from aiogram.dispatcher.filters import Text

# Объект бота
bot = Bot(token="5200289645:AAF_Ni-pFBC31H3cEz65CEYZHlpgoVdPPWk")
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Популярные игры", "Приветственный бонус"]
    keyboard.add(*buttons)
    await message.answer("Приветствуем всех, кто любит играть и поднимать! Мы собрали самое лучшее для тебя! Бонусы, лучшие слоты, джекпоты – всё, чтобы крутить в кайф!", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Популярные игры" or message.text == "Приветственный бонус")
async def cmd_inline_url(message: types.Message):
    if message.text == "Популярные игры":
        photo = open('multibonus.jpg', 'rb')
        buttons = [
            types.InlineKeyboardButton(text="💥Погнали!💥", url="https://excellentchoice.space/GM52pxds")
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
        await message.answer("""Понедельники бывают не только счастливыми, но и драйвовыми с безумной акцией от Favbet! Крути слоты — лови спины и отрывайся на максимум 🥳

 """, reply_markup=keyboard)
        photo.close()
    elif message.text == "Приветственный бонус":
        photo2 = open('bonuscat.png', 'rb')
        buttons = [
            types.InlineKeyboardButton(text="Топовый приветственный БОНУС от Favbet 🤑", url="https://excellentchoice.space/GM52pxds")
        ]
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        keyboard.add(*buttons)
        await bot.send_photo(chat_id=message.chat.id, photo=photo2)
        await message.answer("""Новенький?\n 
Будь внутри игры с зажигательными бонусами.\n
Регистрируйся, делай депозит от 100 гривен и получи ставку без риска до 500 гривен +100% к депозиту.\n""", reply_markup=keyboard)
        photo2.close()
    else:
        await message.answer("Напишите /start чтобы увидеть кнопки!")


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
