def create_callback(href: str) -> str:
    result = f'''
@dp.callback_query(F.data == '{href}')
async def my_callback(call: CallbackQuery):
    await call.message.answer('{href}')'''

    return result