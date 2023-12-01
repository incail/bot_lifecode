from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Гайд', callback_data='guide')
        ],
        [
            InlineKeyboardButton('Курсы', callback_data='archive')
        ],
        [
            InlineKeyboardButton('Книги', callback_data='book')
        ],
        [
            InlineKeyboardButton('Premium Code', callback_data='premium_code')
        ],
    ]

)

kb_sub = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Подписка', callback_data='sub', url='https://t.me/premium_code_bot')
        ],
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
