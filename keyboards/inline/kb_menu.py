from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Гайд', callback_data='guide')
        ],
        [
            InlineKeyboardButton('Архив кодера', callback_data='archive')
        ]
    ]

)

kb_check = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Подписаться', url='https://t.me/l1fecode')
        ],
        [
            InlineKeyboardButton('Проверить', callback_data='check')
        ]
    ]
)

