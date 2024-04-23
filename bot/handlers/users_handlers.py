from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from sqlalchemy.ext.asyncio import AsyncSession
from .base_handler import router
from services.users_services import check_user, create_user
from keyboards.keyboard import kb


@router.message(CommandStart())
async def cuser_register(message: Message, session: AsyncSession):
    # async with get_db() as session:
    user = await check_user(user_id=message.from_user.id, session=session)
    if user:
        await message.answer(f'Welcome {message.from_user.username}', reply_markup=kb)
    await create_user(message=message, session=session)
    await message.answer(f'User {message.from_user.username} register!', reply_markup=kb)

