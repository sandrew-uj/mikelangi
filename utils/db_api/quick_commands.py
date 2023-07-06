from asyncpg import UniqueViolationError

from utils.db_api.db_gino import db
from utils.db_api.schemas.user import User


async def add_user(id: int, name: str, age: int = None, description: str = None,
                   gender: str = None, interest: str = None, image=None):
    # try:
        user = User(id=id, name=name, age=age, description=description, gender=gender,
                    interest=interest, image=image)
        await user.create()

    # except UniqueViolationError:
    #     pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.first()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total


async def update_user_name(id, name):
    user = await User.get(id)
    await user.update(name=name).apply()


async def update_user_age(id, age):
    user = await User.get(id)
    await user.update(age=age).apply()


async def update_user_image(id, image):
    user = await User.get(id)
    await user.update(image=image).apply()


async def update_user_gender(id, gender):
    user = await User.get(id)
    await user.update(gender=gender).apply()


async def update_user_interest(id, interest):
    user = await User.get(id)
    await user.update(interest=interest).apply()


async def update_user_description(id, description):
    user = await User.get(id)
    await user.update(description=description).apply()