from aiogram import types, exceptions
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.alQuranCloud import get_sura_name
from utils.quranEnc import get_data
from loader import dp


@dp.message_handler()
async def send_data(msg: types.Message):
    if len(msg.text.split(':')) == 2:
        if get_data(msg.text):
            output = get_data(msg.text)
            output['surah_name'] = get_sura_name(msg.text)

            caption = (
                f"<b>«{output['surah_name']}» surasi, {output['number_in_surah']}-oyat</b>",
                "<b>Alafasy qiroati</b>"
            )

            ans = output['text'] + '\n\n'
            ans += f"<b>{output['translation']}</b>\n"
            ans += f"<a href='{output['image_url']}'> </a>\n"
            ans += f"«{output['surah_name']}» surasi, {output['number_in_surah']}-oyat." + "\n\n"

            if output['footnotes'] != '':
                ans += output['footnotes'] + "\n\n"

            ans += "— Алауддин Мансур тафсири"

            await msg.answer_voice(output['audio'], "\n\n".join(caption))
            await msg.answer(ans)
        else:
            await msg.reply("Malumot topilmadi.")
    else:
        try:
            try:

                if send_audio(int(msg.text)):
                    name = get_sura_name(f'{int(msg.text)}:1')
                    await msg.answer_audio(
                        send_audio(int(msg.text)),
                        caption=f"«{name}» surasi | Mishary Alafasy"
                    )
                else:
                    ans = (
                        "Qurʼonda 114 sura mavjud.</b>",
                        "Iltimos, 1 dan 114 gacha son kiriting"
                    )
                    await msg.reply('\n\n'.join(ans))
            except exceptions.WrongFileIdentifier:
                ans = (
                    "Botda xatolik yuz berdi, bu xatolik ustida ishlayabmiz"
                    "<a href='https://telegra.ph/Xatolik-uchun-uzur-suraymiz-08-13'> </a>",
                    "Telegram-da bot orqali 50 MB hajmdan ko'p bo'lgan audio jo'natsa "
                    "bo'lmas ekan."
                    "Bazi suralarning hajmi 50 MB dan oshib ketyabdi, shu sababdan xatolik yuz beryabdi. ",
                    "Ammo bu surani istalgan oyatini junata olamiz buning uchun shu sura raqami va oyat raqamini kiriting.",
                    "Misol uchun: 2:55 , bu Baqara surasining 55-oyati.",
                    "Noqulaylik uchun uzur suraymiz. Surani kanalimizdan topishingiz mumkin",
                )
                await msg.answer('\n\n'.join(ans), reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton('Kanalga o`tish', url='https://t.me/the_way_of_tears')
                        ]
                    ],
                ))
        except ValueError:
            text = ("Botni ishlatishda xatolikka yo'l qo'ydingiz, iltimos to'g'ri so'rov yuboring.",
                    "Agar botni ishlatishga tushunmasangiz, /help ni bosing."
                    )
            await msg.reply("\n\n".join(text))


def send_audio(num):
    if num < 10:
        return f'http://server8.mp3quran.net/afs/00{num}.mp3'
    elif num < 100:
        return f'http://server8.mp3quran.net/afs/0{num}.mp3'
    elif num <= 114:
        return f'http://server8.mp3quran.net/afs/{num}.mp3'
    else:
        return False
