from random import randint
import asyncio
import json

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message


class Main():
    tk = json.load(open('BotAssistant/.token.json'))
    bot = Bot(tk.get('bot').get('token'))
    dp = Dispatcher()


    @dp.message(Command(commands="start"))
    async def com_start(mess: Message):
        await mess.answer('Hello')

    @dp.message(Command(commands="saysomething"))
    async def saysomething(mess: Message):
        file = json.load(
            open('BotAssistant/saysomething.json', encoding='utf-8')
        )
        sentence = file.get(f'{randint(1, 10)}')
        text = f'''{sentence.get("Text")}

Автор: {sentence.get("Author")}({sentence.get("Date")})'''
        await mess.answer(text)

    @dp.message(F.text == 'Доброго ранку')
    async def good_morning(mess: Message):
        await mess.answer('Доброго ранку, чим будеш снідати?')


    async def main(self):
        await self.dp.start_polling(self.bot)


if __name__ == "__main__":
    asyncio.run(Main.main(Main()))