import asyncio

from data import config
from utils.db_api import quick_commands
from utils.db_api.db_gino import db


async def test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    print(f"Add users:")
    await quick_commands.add_user(1, "One", "email")
    await quick_commands.add_user(2, "MJ", "MJ@gmail.com")
    await quick_commands.add_user(3, "KD", "KD@gmail.com")
    await quick_commands.add_user(4, "Jokic", "Nikola@yandex.ru")
    # await quick_commands.add_user(5, 1, 3)
    users = await quick_commands.select_all_users()
    print(f"After addition all users: {users}")

    user_count = await quick_commands.count_users()
    print(f"Amount of users: {user_count}")

    user = await quick_commands.select_user(id=4)
    print(f"Obtained user = {user}")

loop = asyncio.get_event_loop()
loop.run_until_complete(test())