import os

from aiogram import types

from loader import dp
from loader import bot
from keyboards.inline.kb_menu import kb, kb_check, kb_sub
from data.config import MY_CHANNEL


# a = os.path.abspath('Гайд_для_начинающих.pdf')
# b = os.path.abspath('Житейская_версия.pdf')

# a_formatted = a.replace('\\', '/')
# b_formatted = b.replace('\\', '/')


@dp.callback_query_handler()
async def call(callback: types.CallbackQuery):

    user_id = callback.message.chat.id
    my_channel_id = MY_CHANNEL
    user_channel_status = await callback.bot.get_chat_member(chat_id=my_channel_id, user_id=user_id)
    if callback.data == 'guide':
        if user_channel_status["status"] != 'left':
            with open(os.path.abspath('Гайд.pdf'), 'rb') as file:
                await bot.send_document(callback.message.chat.id, file)
        else:
            await bot.send_message(user_id,
                                   text=f'{callback.message.chat.first_name}, вы не подписаны на канал 😢'
                                        '\n⬇️Чтобы подписаться или проверить нажмите на кнопку ниже',
                                   reply_markup=kb_check)

    elif callback.data == 'archive':
        if user_channel_status["status"] != 'left':
            await bot.send_message(user_id,
                                   text='🔽Курсы🔽')
            await bot.send_message(user_id,
                                   text='https://t.me/+DbzZzGzXx9c3MGNi')
        else:
            await bot.send_message(user_id,
                                   text=f'{callback.message.chat.first_name}, вы не подписаны на канал 😢'
                                        '\n⬇️Чтобы подписаться или проверить нажмите на кнопку ниже',
                                   reply_markup=kb_check)

    elif callback.data == 'book':
        if user_channel_status["status"] != 'left':
            await bot.send_message(user_id,
                                   text='🔽Книги🔽')
            await bot.send_message(user_id,
                                   text='https://t.me/code_book')
        else:
            await bot.send_message(user_id,
                                   text=f'{callback.message.chat.first_name}, вы не подписаны на канал 😢'
                                        '\n⬇️Чтобы подписаться или проверить нажмите на кнопку ниже',
                                   reply_markup=kb_check)

#     elif callback.data == 'premium_code':
#         if user_channel_status["status"] != 'left':

#             await bot.send_photo(user_id, photo=open('premium_code.png', 'rb'),
#                                  caption="""Premium Code — это тот самый вайбовый канал по айтишке, где вы сможете получить ценный материал и будете находиться в кругу единомышленников.

# Уникальная возможность пообщаться со многими разработчиками и перенять их опыт. А некоторые могут взять к себе на обучение или предложить что-то интересное.

# Также, вы сможете поднять уровень вашего английского языка, так как наш преподаватель предоставит нужный материал, даст советы по улучшению навыков на собеседованиях и правильное применение их в работе.

# А наши кураторы окажут поддержку и ответят на «самые глупые» вопросы. Подкрепят вас нужной мотивацией, направят на правильный путь и не дадут опустить руки.

# Возможно, именно в нашем канале вы сможете найти себе команду на проект или быть её создателем. Получите нужные рекомендации и ништяки от создателей Premium Code.

# Мы создаём окружение кодеров, где каждый сможет найти для себя что-то полезное, а вы можете стать частью этого окружения!""", reply_markup=kb_sub)
#         else:
#             await bot.send_message(user_id,
#                                    text=f'{callback.message.chat.first_name}, вы не подписаны на канал 😢'
#                                         '\n⬇️Чтобы подписаться или проверить нажмите на кнопку ниже',
#                                    reply_markup=kb_check)
    elif callback.data == 'check':
        if user_channel_status["status"] != 'left':
            await callback.message.delete()
            await callback.message.answer('Теперь вы можете продолжить ваши запросы', reply_markup=kb)
        else:
            await bot.send_message(user_id,
                                   text=f'{callback.message.chat.first_name}, вы не подписаны на канал 😢'
                                        '\n⬇️Чтобы подписаться или проверить нажмите на кнопку ниже',
                                   reply_markup=kb_check)
