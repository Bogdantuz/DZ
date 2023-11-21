from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)


def inline(films):
    buttons = []

    for film in films:
        name = film['name']
        href = film['href']
        if not len(href) >= 65:
            buttons.append(InlineKeyboardButton(
                text=name,
                callback_data=href
            ))

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [i] for i in buttons
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