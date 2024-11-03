from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from lexicon import LEXICON_RU
from services import determine_winner, LAYOUT, bot_choice
from keyboards import keyboard_start, keyboard_game

router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU["/start"],
        reply_markup=keyboard_start
    )


@router.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer(
        text=LEXICON_RU["/help"],
        reply_markup=keyboard_start
    )


@router.message(F.text == LEXICON_RU['yes_button'])
async def process_agree_answer(message: Message):
    await message.answer(
        text=LEXICON_RU["yes"],
        reply_markup=keyboard_game
    )


@router.message(F.text == LEXICON_RU['no_button'])
async def process_refusal_answer(message: Message):
    await message.answer(text=LEXICON_RU["no"])


@router.message(F.text.in_(LAYOUT.keys()))
async def process_game_answer(message: Message):
    # записать ответ
    bot_answer = bot_choice()
    result = determine_winner(message.text, bot_answer)
    await message.answer(
        text=f'{LEXICON_RU["bot_choice"]} - {bot_answer}'
    )

    await message.answer(
        text=LEXICON_RU[result],
        reply_markup=keyboard_start
    )


@router.message()
async def process_other_answers(message: Message):
    print(message.text)
    await message.answer(
        text=LEXICON_RU["other"]
    )
