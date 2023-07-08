from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def getstartkb(payurl: str) -> InlineKeyboardMarkup:
    startkb = InlineKeyboardMarkup(row_width=1)
    kbtn1 = InlineKeyboardButton(text='Оплата товара', url=payurl)
    kbtn2 = InlineKeyboardButton(text='Подтвердить оплату', callback_data='claim')
    startkb.add(kbtn1, kbtn2)
    return startkb
