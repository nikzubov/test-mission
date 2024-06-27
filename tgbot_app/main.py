import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import DefaultKeyBuilder, RedisStorage
from aiogram.fsm.strategy import FSMStrategy

from config import settings
from handlers.user_private import user_private_router

BOT = Bot(
    token=settings.T_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN)
)

REDIS_URL_1 = f'redis://:{settings.R_PASSWORD}@redis:6379/0?decode_responses=True&protocol=3'

redis_fsm_storage = RedisStorage.from_url(
    url=REDIS_URL_1,
    key_builder=DefaultKeyBuilder(
        with_bot_id=True,
        with_destiny=True
    )
)

logging.basicConfig(
    level=logging.INFO,
    filename='bot_log.log',
    format="%(asctime)s %(levelname)s %(message)s"
)

ALLOWED_UPDATES = ['message', 'edited_message', 'callback_query']

dp = Dispatcher(
    fsm_strategy=FSMStrategy.GLOBAL_USER,
    storage=redis_fsm_storage
)

dp.include_router(user_private_router)


@dp.shutdown()
async def on_shutdown():
    """Закрытие сессии redis перед выключением бота"""
    await redis_fsm_storage.close()


async def main():
    await BOT.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(BOT, allowed_updates=ALLOWED_UPDATES)


if __name__ == "__main__":
    asyncio.run(main())
