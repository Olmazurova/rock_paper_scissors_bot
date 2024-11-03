from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from lexicon import LEXICON_RU

kb_builder = ReplyKeyboardBuilder() # создаём конструктор клавиатур: создаёт список списков из кнопок, а в параметры метода as_markup передаём атрибуты клавиатуры

# создание кнопок
button_yes = KeyboardButton(text=LEXICON_RU["yes_button"])
button_no = KeyboardButton(text=LEXICON_RU["no_button"])

buttons_game = [KeyboardButton(text=name) for name in [LEXICON_RU["rock"], 
                                                       LEXICON_RU["scissors"], 
                                                       LEXICON_RU["paper"]]]
kb_builder.row(*buttons_game, width=3)

# создаём клавиатуру без билдера
keyboard_start = ReplyKeyboardMarkup(
    keyboard=[[button_yes, button_no]],
    resize_keyboard=True, # маленький размер кнопок
    one_time_keyboard=True # сворачивание клавиатуры после нажатия
)

keyboard_game = kb_builder.as_markup( # на выходе ReplyKeyboardMarkup объект
    resize_keyboard=True, # маленький размер кнопок
)
