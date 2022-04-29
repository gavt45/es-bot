import logging

from vkwave.bots import BaseMiddleware, BotEvent, MiddlewareResult, SimpleBotEvent

from db import DB, Candidate


class UserMiddleware(BaseMiddleware):
    async def pre_process_event(self, event: BotEvent) -> MiddlewareResult:
        db = DB()
        botevent = SimpleBotEvent(event)
        user_id = event.object.object.message.from_id

        user = db.get_user(user_id)
        if not user:
            user_info = await botevent.get_user()
            logging.debug(f"Got user info: {user_info}")
            user = Candidate(id=user_id, sex=user_info.sex, name=user_info.first_name, last_name=user_info.last_name)
            db.add_candidate(user)
            logging.debug(f"Created new user: {user}")
        print(f"Found user: {user}")

        event["current_user"] = user
        return MiddlewareResult(True)
