from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command
from aiogram.enums import ParseMode
from sqlalchemy.ext.asyncio import AsyncSession
from services.users_services import check_user
from keyboards.keyboard import kb


router = Router()


@router.message(Command('help'))
async def user_helper(message: Message, session: AsyncSession):
    user = await check_user(user_id=message.from_user.id, session=session)
    if user:
        commands = ["1. /processing \- image processing menu",
                    "2. /description \- Bot description",
                    "3. /about \- About developer the team"
                    ]
        commands_text = "\n".join(commands)
        await message.answer(f"Commands:\n\n{commands_text}", parse_mode=ParseMode.MARKDOWN_V2)


@router.message(Command('description'))
async def bot_description(message: Message):
    description = ('Image Master is a powerful and multifunctional image processing bot for Telegram.'
                   ' It allows you to edit, enhance, and convert images in various ways right in the messenger.')
    await message.answer(description, parse_mode=ParseMode.HTML)


@router.message(Command('about'))
async def about(message: Message):
    await message.answer('We developers telegram bot')
