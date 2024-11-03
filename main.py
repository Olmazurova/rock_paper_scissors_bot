import asyncio
import logging


from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
import handlers
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


logger = logging.getLogger(__name__)
async def main() -> None:
    '''Функция настройки(конфигурирования) и запуска бота'''
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    config: Config = load_config() # загружаем конфигурацию

    bot = Bot(token=config.tg_bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML)) # чтобы распознавать теги
    dp = Dispatcher()

    # Регистрация диспетчеров
    dp.include_router(handlers.router)

    # Пропускаем апдейты
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
