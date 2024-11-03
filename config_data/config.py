from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    '''Класс содержащий токен'''
    token: str


@dataclass
class Config:
    '''Класс содержащий тг бот ??? можно без него обойтись???'''
    tg_bot: TgBot


def load_config(path: str| None = None) -> Config:
    '''Функция возвращающая объект конфигурации бота'''

    env = Env() # переменная виртуального окружения
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env("BOT_TOKEN")))
