from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishlatish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("/suralar", "Suralar nomlari"),
            types.BotCommand("/zikrlar", "Zikrlar"),
            types.BotCommand("/duolar", "Duolar"),
            types.BotCommand("/tonggi", "Tonggi zikrlar"),
            types.BotCommand("/tungi", "Tungi zikrlar"),
        ]
    )
