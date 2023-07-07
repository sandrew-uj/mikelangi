from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("profile", "Моя анкета"),
        types.BotCommand("edit_profile", "Изменить анкету"),
        types.BotCommand("search", "Найти пару"),
        types.BotCommand("see_love", "Посмотреть кому ты понравился"),
    ])
