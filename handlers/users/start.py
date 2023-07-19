from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.inline.kb_menu import kb
from utils.misc.throttling import rate_limit


@rate_limit(limit=5, key="/start")
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer_photo(photo=open('картинка_кодер.jpg', 'rb'),
                               caption=f'👁‍🗨Здарова, Кодеры, вы за ништяками? \n\n'
                                       f'💬СHAT - https://t.me/lifec0de_community\n'
                                       f'📱INST - https://instagram.com/lifec0de'
                                       f'?igshid=YmMyMTA2M2Y=\n\n\n'
                                       f'                                         ⬇️ Забирай скорее ⬇️',
                               reply_markup=kb)
