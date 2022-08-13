from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import menu

from loader import dp


@dp.message_handler(CommandStart())
async def bot_help(msg: types.Message):
    ans = f"<b>Botdan unimli foydalanish uchun quydagi ko'rinishda xabar yozing:</b>" + "\n"
    ans += "<b>{sura tartib raqami}:{oyat raqami}</b>" + "\n\n"
    ans += "Misol uchun bizga oyatul kursi kerak bulsa <b>(Baqara surasi, 255-oyat), </b>" \
           "botga quyidagicha murojat qilishingiz mumkin: "
    ans += "<b>2:255</b>"+ "\n\n"
    ans += "Yoki istalgan surani eshtish uchun quyidagi (🔠) tugmadan sura raqamini tanlang 👇"

    await msg.answer(ans, reply_markup=menu)
