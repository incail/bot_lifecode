from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Гайд', callback_data='guide')
        ],
        [
            InlineKeyboardButton('Курсы', callback_data='archive')
        ]
    ]

)

kb_check = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Подписаться', url='https://t.me/codel1fe')
        ],
        [
            InlineKeyboardButton('Проверить', callback_data='check')
        ]
    ]
)

