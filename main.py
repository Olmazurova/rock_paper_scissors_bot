import asyncio


from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config

def main() -> None:
    '''Функция настройки(конфигурирования) и запуска бота'''

    config = load_config() # загружаем конфигурацию

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # Регистрация диспетчеров

    # Пропускаем апдейты

asyncio.run(main())
