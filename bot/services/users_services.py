from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.users_models import User


async def check_user(user_id, session: AsyncSession):
    user = await session.scalar(select(User).where(User.user_id == user_id))
    return user


async def create_user(message, session: AsyncSession):
    user_id = message.from_user.id
    username = message.from_user.username if message.from_user.username else None
    user = User(
        user_id=user_id,
        username=username
    )
    session.add(user)
    await session.commit()
