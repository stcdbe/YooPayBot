import string
import random

from aiogram.types import Message, CallbackQuery, InputFile
from yoomoney import Quickpay, Client

from bot.kyeboards import getstartkb
from bot.db import opendb, closedb, adduser, getlabel
from bot.config import YOOTOKEN, RECEIVER, TARGETS


async def on_startup(_) -> None:
    await opendb()


async def on_shutdown(_) -> None:
    await closedb()


async def hello(message: Message) -> None:
    await message.answer(text='Для покупки нажми /pay')


async def pay(message: Message) -> None:
    letters_and_digits = string.ascii_lowercase + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, 10))
    quickpay = Quickpay(receiver=RECEIVER,
                        quickpay_form='shop',
                        targets=TARGETS,
                        paymentType='SB',
                        sum=2,
                        label=rand_string)
    await adduser(message, label=rand_string)
    await message.answer_photo(photo=InputFile(path_or_bytesio='bot/images/product.png'),
                               caption='Товар\nНаименование:\nОписание:\nЦена:',
                               reply_markup=await getstartkb(quickpay.redirected_url))


async def checkpayment(callback: CallbackQuery) -> None:
    await callback.answer()
    label = await getlabel(userid=callback.from_user.id)
    client = Client(YOOTOKEN)
    history = client.operation_history(label=label)
    operation = history.operations
    if operation:
        checkoperation = history.operations[-1]
        if checkoperation.status == 'success':
            await callback.message.answer(text='Товар')
    else:
        await callback.message.answer(text='Товар не оплачен')
