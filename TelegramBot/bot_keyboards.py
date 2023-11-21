from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


def inline(films):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=film['name'],
                callback_data=film['href']
            )] for film in films
        ],
        resize_keyboard=True
    )
    return keyboard


def reply():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='хочу подивитись фільм')],
            [KeyboardButton(text='хочу послухати музику')]
        ],
        resize_keyboard=True
    )
    return keyboard