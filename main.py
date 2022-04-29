import logging

from vkwave.bots import SimpleLongPollBot, PhotoUploader

from blueprints import (
    menu_router, test_router,
)
from config import Config
from middlewares import UserMiddleware
# from nft_things.NftSender import NFTSender

logging.basicConfig(level="DEBUG")

bot = SimpleLongPollBot(Config.TOKEN, group_id=Config.GROUP_ID)

# nft_sender = NFTSender(bot.api_context)
# nft_sender.start()
uploader = PhotoUploader(bot.api_context)
Config().api_ctx = bot.api_context
Config().uploader = uploader

bot.middleware_manager.add_middleware(UserMiddleware())


bot.dispatcher.add_router(test_router)
# bot.dispatcher.add_router(games_router)
# bot.dispatcher.add_router(coin_flip_router)
# bot.dispatcher.add_router(bonus_router)

# регаем последним чтобы сначала проверялись все остальные команды
bot.dispatcher.add_router(menu_router)

bot.run_forever()