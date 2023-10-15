from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
menu = [
    [InlineKeyboardButton(text="💰 Прайс-лист", callback_data="pricelist"),
     InlineKeyboardButton(text="❓ Вопросы", callback_data="question")],

]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])

quiz = [
     [InlineKeyboardButton(text="1. Какие у вас есть бесплатные развлечения?", callback_data="q1")],
     [InlineKeyboardButton(text="2. Сколько стоит стоянка на территории турбазы?", callback_data="q2")],
     [InlineKeyboardButton(text="3. Какой у вас график работы?", callback_data="q3")],
     [InlineKeyboardButton(text="4. Какое минимальное время бронирования для каждой услуги?", callback_data="q4")],
     [InlineKeyboardButton(text="5. Имеются ли свободные вакансии для трудоустройства?", callback_data="q5")],
     [InlineKeyboardButton(text="6. Моего вопроса нет в списке :(", callback_data="q6")]
]
quiz = InlineKeyboardMarkup(inline_keyboard=quiz)
