from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


image_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Black', callback_data='black_white')],
    [InlineKeyboardButton(text='Hot', callback_data='hot_image')],
    [InlineKeyboardButton(text='Noise', callback_data='noise_image')],
    [InlineKeyboardButton(text='Resize', callback_data='resize_image')]
])
