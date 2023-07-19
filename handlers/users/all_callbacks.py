import os

from aiogram import types

from loader import dp
from loader import bot
from keyboards.inline.kb_menu import kb, kb_check
from data.config import MY_CHANNEL


a = os.path.abspath('Гайд_для_начинающих.pdf')
b = os.path.abspath('Житейская_версия.pdf')

a_formatted = a.replace('\\', '/')
b_formatted = b.replace('\\', '/')


@dp.callback_query_handler()
async def call(callback: types.CallbackQuery):

    user_id = callback.message.chat.id
    my_channel_id = MY_CHANNEL
    user_channel_status = await callback.bot.get_chat_member(chat_id=my_channel_id, user_id=user_id)
    if callback.data == 'guide':
        if user_channel_status["status"] != 'left':
            with open(os.path.abspath('Гайд_для_начинающих.pdf'), 'rb') as file:
                await bot.send_document(callback.message.chat.id, file)
            with open(os.path.abspath('Житейская_версия.pdf'), 'rb') as file:
                await bot.send_document(callback.message.chat.id, file)
        else:
            await bot.send_message(user_id,
                                   text=f'{callback.message.chat.first_name}, вы не подписаны на канал 😢'
                                        '\n⬇️Чтобы подписаться или проверить нажмите на кнопку ниже',
                                   reply_markup=kb_check)

    elif callback.data == 'archive':
        if user_channel_status["status"] != 'left':
            await bot.send_message(user_id,
                                   text='https://t.me/+DbzZzGzXx9c3MGNi')
        else:
            await bot.send_message(user_id,
                                   text=f'{callback.message.chat.first_name}, вы не подписаны на канал 😢'
                                        '\n⬇️Чтобы подписаться или проверить нажмите на кнопку ниже',
                                   reply_markup=kb_check)

    elif callback.data == 'check':
        if user_channel_status["status"] != 'left':
            await callback.message.delete()
            await callback.message.answer('Теперь вы можете продолжить ваши запросы', reply_markup=kb)
        else:
            await bot.send_message(user_id,
                                   text=f'{callback.message.chat.first_name}, вы не подписаны на канал 😢'
                                        '\n⬇️Чтобы подписаться или проверить нажмите на кнопку ниже',
                                   reply_markup=kb_check)
