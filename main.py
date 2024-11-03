import asyncio


from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
import handlers

async def main() -> None:
    '''Функция настройки(конфигурирования) и запуска бота'''

    config = load_config() # загружаем конфигурацию

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # Регистрация диспетчеров
    dp.include_router(handlers.router)

    # Пропускаем апдейты
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
