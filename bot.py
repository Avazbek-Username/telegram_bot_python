# This is a echo bot.
# It echoes any incoming text messages.


import logging

from aiogram import Bot, Dispatcher, executor, types
import wikipedia

API_TOKEN = '6558858241:AAH-rc8jD-AB99m_LBJyVbb8MKlN_x122n8'
wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Bizning test botimizga xush kelibsiz😊")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/help` command
    """
    await message.reply("Sizda qandaydir muammo bo'lsa @Avazbek_Dev ga yozishingiz mumkin👍")



@dp.message_handler()
async def echo(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.text("Bu mavzuga oid maqola topilmadi")  
        




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)