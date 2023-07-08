import logging

from aiogram import executor, Dispatcher, Bot

from bot.config import APITOKEN
from bot.handlers import on_startup, on_shutdown, hello, pay, checkpayment


def main() -> None:

    logging.basicConfig(level=logging.INFO)

    bot = Bot(APITOKEN)
    dp = Dispatcher(bot)

    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(pay, commands=['pay'])
    dp.register_callback_query_handler(checkpayment, lambda callback: callback.data == 'claim')

    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
