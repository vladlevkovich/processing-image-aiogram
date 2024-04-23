from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/start')],
    [KeyboardButton(text='/help'), KeyboardButton(text='/description')],
    [KeyboardButton(text='/about'), KeyboardButton(text='/processing')]
], resize_keyboard=True)
