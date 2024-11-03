from randome import choice

LAYOUT = {
    "Камень": "Ножницы",
    "Ножницы": "Бумага",
    "Бумага": "Камень"
}

def bot_choice() -> str:
    return choice(LAYOUT.keys())


def determine_winner(user_answer: str) -> str:
    bot_answer = bot_choice()
    if bot_answer == user_answer:
        return "draw"
    elif layout[user_answer] == bot_answer:
        return "winner_you"
    return "winner_bot"
