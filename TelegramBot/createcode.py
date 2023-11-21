def create_callback(href: str) -> str:
    result = f'''
@dp.callback_query(F.data == '{href}')
async def my_callback(call: CallbackQuery):
    await call.message.answer('https://freemusicarchive.org/music/{href}')'''

    return result


def new_callback(href):
    result = f'''
@TelegramBot.dp.callback_query(F.data == '{href}')
async def new_callback(call: CallbackQuery):
    await call.message.answer('https://freemusicarchive.org/music/{href}')
    
TelegramBot.new_callback = new_callback'''
    
    return result