import logging

from vkwave.bots import SimpleLongPollBot

from blueprints import (
    menu_router, test_router,
)
from config import Config
from middlewares import UserMiddleware

logging.basicConfig(level="DEBUG")

bot = SimpleLongPollBot(Config.TOKEN, group_id=Config.GROUP_ID)

bot.middleware_manager.add_middleware(UserMiddleware())


bot.dispatcher.add_router(test_router)
# bot.dispatcher.add_router(games_router)
# bot.dispatcher.add_router(coin_flip_router)
# bot.dispatcher.add_router(bonus_router)

# регаем последним чтобы сначала проверялись все остальные команды
bot.dispatcher.add_router(menu_router)

bot.run_forever()