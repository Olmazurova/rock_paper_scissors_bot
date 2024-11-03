from random import choice

LAYOUT = {
    "Камень": "Ножницы",
    "Ножницы": "Бумага",
    "Бумага": "Камень"
}

def bot_choice() -> str:
    return choice(LAYOUT.keys())


def determine_winner(user_answer: str, bot_answer: str) -> str:
    
    if bot_answer == user_answer:
        return "draw"
    elif layout[user_answer] == bot_answer:
        return "winner_you"
    return "winner_bot"
