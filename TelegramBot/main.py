from json import load
from logging import basicConfig, INFO
from sys import stdout
import asyncio
from pprint import pprint

from aiogram import Bot, Dispatcher, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import CommandStart

from parsing import ParsingFilm, ParsingMusic
from bot_keyboards import inline, reply
from createcode import create_callback


class TelegramBot:
    tk = load(open(".secret/token.json"))
    bot = Bot(tk.get("bot").get("token"))
    dp = Dispatcher()
    films_args = ["https://multiplex.ua", "#mp_postersList > div", "a.mpp_title"]
    films = ParsingFilm(
        films_args[0], films_args[1], films_args[2]
    ).result
    musics_args = [
        "https://freemusicarchive.org/search/?quicksearch=&search-genre=Jazz",
        "div.w-full.flex.flex-col.gap-3.pt-3 > div",
        "a.font-bold"
    ]
    musics = ParsingMusic(
        musics_args[0], musics_args[1], musics_args[2]
    ).result

    async def main():
        await TelegramBot.dp.start_polling(TelegramBot.bot)


    @dp.message(CommandStart())
    async def com_start(mess: Message):
        await mess.answer(f"Welcome {mess.from_user.first_name}!", reply_markup=reply())

    @dp.message(F.text == "хочу подивитись фільм")
    async def com_film(mess: Message):
        TelegramBot.films = ParsingFilm(
            TelegramBot.films_args[0],
            TelegramBot.films_args[1],
            TelegramBot.films_args[2]
        ).result
        pprint(TelegramBot.films)
        await mess.answer(
            "Який фільм хочеш дивитись?", reply_markup=inline(TelegramBot.films)
        )

    @dp.message(F.text == "хочу послухати музику")
    async def com_music(mess: Message):
        TelegramBot.musics = ParsingMusic(
            TelegramBot.musics_args[0],
            TelegramBot.musics_args[1],
            TelegramBot.musics_args[2]
        ).result
        pprint(TelegramBot.musics)
        await mess.answer(
            "Яку музику хочеш слухати?", reply_markup=inline(TelegramBot.musics)
        )

    @dp.message()
    async def dontunderstand(mess: Message):
        await mess.answer("I don't understand you")


    for film in films:
        href = film["href"]
        exec(create_callback(href))

    for music in musics:
        href = music["href"]
        exec(create_callback(href))


if __name__ == "__main__":
    basicConfig(level=INFO, stream=stdout)
    asyncio.run(TelegramBot.main())