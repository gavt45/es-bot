from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler
import locales

# MENU_KB.add_row()
# MENU_KB.add_text_button(text="Профиль", payload={"command": "profile"}, color=ButtonColor.SECONDARY)
# MENU_KB.add_row()
# MENU_KB.add_text_button(text="Бонус", payload={"command": "bonus"}, color=ButtonColor.POSITIVE)

menu_router = DefaultRouter()


@simple_bot_message_handler(menu_router,)
async def menu(event: SimpleBotEvent):
    return await event.answer(
        message=f"Привет!",
        keyboard=locales.MENU_KB.get_keyboard(),
    )