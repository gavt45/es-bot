import json
import logging
import random

from vkwave.bots import DefaultRouter, SimpleBotEvent, simple_bot_message_handler, PayloadFilter, PayloadContainsFilter, \
    PhotoUploader
from vkwave.bots import Keyboard, ButtonColor
from vkwave.bots import EventTypeFilter, BotEvent
from vkwave.types.bot_events import BotEventType
from vkwave.bots.fsm import FiniteStateMachine, StateFilter, ForWhat, State, ANY_STATE

import locales
from config import Config
from db import DB
from db.db import TestResult
from locales import INPUT_NAME_TEXT


# MENU_KB.add_row()
# MENU_KB.add_text_button(text="Профиль", payload={"command": "profile"}, color=ButtonColor.SECONDARY)
# MENU_KB.add_row()
# MENU_KB.add_text_button(text="Бонус", payload={"command": "bonus"}, color=ButtonColor.POSITIVE)
# from nft_things.NftSender import NFTSender

test_router = DefaultRouter()

test_router.registrar.add_default_filter(
    EventTypeFilter(BotEventType.MESSAGE_NEW.value))  # we don't want to write it in all handlers.


# #  exiting from poll (works on any state)
# @test_router.registrar.with_decorator(
#     lambda event: event.object.object.message.text == "exit",
#     StateFilter(fsm=fsm, state=ANY_STATE, for_what=ForWhat.FOR_USER)
# )
# async def simple_handler(event: BotEvent):
#     # Check if we have the user in database
#     if await fsm.get_data(event, for_what=ForWhat.FOR_USER) is not None:
#         await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
#     return "You are quited!"

@test_router.registrar.with_decorator(
    PayloadContainsFilter("test"),# for state in States.questions[:-1]]
)
async def main_part_handle(event: BotEvent):
    user_id = event.object.object.message.from_id
    payload = json.loads(event.object.object.message.payload)

    botevent = SimpleBotEvent(event)
    state_idx = int(payload["test"])
    logging.debug(f"State index: {state_idx}")


    q_res = payload['q'] if 'q' in payload else None
    logging.debug(f"Qres: {q_res}")

    # extra_state_data works as fsm.add_data(..., state_data={"name": event.object.object.message.text})
    logging.debug(f"Got text: {event.object.object.message.text}")

    if q_res:
        DB().update_test_result(user_id, question=state_idx, answer=q_res)

    if state_idx + 1 < len(locales.questions):
        return await botevent.answer(
            message=locales.questions[state_idx + 1][0],
            keyboard=locales.questions[state_idx + 1][1].get_keyboard(),
        )
    else:
        # todo add task to send user an image here
        # Config().nft_sender.add_task()
        logging.warn("Sending attach!")
        big_attachment = await Config().uploader.get_attachments_from_paths(
            peer_id=user_id,
            file_paths=["img.jpg"],
        )
        await Config().api_ctx.messages.send(
            user_id=user_id, attachment=big_attachment, random_id=0
        )
        return await botevent.answer(
            message=locales.LAST_MESSAGE,
            keyboard=locales.LAST_MESSAGE_KB.get_keyboard(),
        )

# @test_router.registrar.with_decorator(
#     StateFilter(fsm=fsm, state=MyState.age, for_what=ForWhat.FOR_USER),
# )
# async def simple_handler(event: BotEvent):
#     if not event.object.object.message.text.isdigit():
#         return f"Please, send only positive numbers!"
#     await fsm.add_data(
#         event=event,
#         for_what=ForWhat.FOR_USER,
#         state_data={"age": event.object.object.message.text},
#     )
#     user_data = await fsm.get_data(event=event, for_what=ForWhat.FOR_USER)
#
#     # finish poll and delete the user
#     # `fsm.finish` will do it
#     await fsm.finish(event=event, for_what=ForWhat.FOR_USER)
#     return f"Your data - {user_data}"
