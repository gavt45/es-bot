from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler
import locales

menu_router = DefaultRouter()


@simple_bot_message_handler(menu_router,)
async def menu(event: SimpleBotEvent):
    return await event.answer(
        message=locales.MENU,
        keyboard=locales.MENU_KB.get_keyboard(),
    )