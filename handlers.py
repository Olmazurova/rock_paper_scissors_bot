from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from lexicon import LEXICON_RU
from other_functions import determine_winner, LAYOUT

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU["/start"]
        reply_markup=keyboard_start
    )


@router.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await messsage.answer(
        text=LEXICON_RU["/help"],
        reply_keyboard=keyboard_start
    )


@router.message(F.text == "Давай!")
async def process_agree_answer(message: Message):
    await message.answer(
        text=LEXICON_RU["yes"],
        reply_keyboard=keyboard_game
    )


@router.message(F.text == "Не хочу")
async def process_refusal_answer(message: Message):
    await message.answer(
        text=LEXICON_RU["no"]
    )


@router.message(F.text.in_([LAYOUT.keys()]))
async def process_game_answer(message: Message):
    # записать ответ
    # выбор бота и кто побетитель
    result = determine_winner(message.text)
    await message.answer(
        text=LEXICON_RU[result],
        reply_keyboard=keyboard_start
    )


@router.message()
async def process_other_answers(message: Message):
    await message.answer(
        text=LEXICON_RU["other"]
    )
