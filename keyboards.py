from aiogram.utils.keyboard import ReplyKeyboardBilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_builder = ReplyKeyboardBuilder() # создаём конструктор клавиатур: создаёт список списков из кнопок, а в параметры метода as_markup передаём атрибуты клавиатуры

# создание кнопок
button_yes = KeyboardButton(text="Давай!")
button_no = KeyboardButton(text="Не хочу")

buttons_game = [KeyboardButton(text=name) for name in ["Камень", "Ножницы", "Бумага"]]
kb_builder.row(*buttons_game, width=3)

# создаём клавиатуру без билдера
keyboard_start = ReplyKeyboardMarkup(
    keyboard=[[button_yes, button_no]],
    resize_keyboard=True, # маленький размер кнопок
    one_time_keyboard=True # сворачивание клавиатуры после нажатия
)

keyboard_game = kb_builser.as_markup( # на выходе ReplyKeyboardMarkup объект
    resize_keyboard=True, # маленький размер кнопок
    one_time_keyboard=True # сворачивание клавиатуры после нажатия
)