from aiogram import types

from loader import dp


@dp.message_handler()
async def anything(message: types.Message):
    if message.text:
        await message.answer(text=f'Извините {message.from_user.first_name}, я вас не понимаю 😔')
