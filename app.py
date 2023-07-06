from utils.db_api import db_gino
from utils.db_api.db_gino import db
from utils.set_bot_commands import set_default_commands


async def on_startup(dp):
    import filters
    import middlewares
    filters.setup(dp)
    # middlewares.setup(dp)

    from utils.notify_admins import on_startup_notify

    print("Подключим БД")
    await db_gino.on_startup(dp)
    print("Готов!")

    # print("Очистим базу")
    # await db.gino.drop_all()

    print("Создаем таблицу")
    await db.gino.create_all()

    await on_startup_notify(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup)
