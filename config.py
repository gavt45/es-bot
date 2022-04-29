import os
from util import Singleton


class Config(metaclass=Singleton):
    TOKEN = os.environ["TOKEN"]
    GROUP_ID = int(os.environ["GROUP_ID"])

    PG_USER = os.environ["USER"]
    PG_PASS = os.environ["PASS"]
    PG_ADDR = os.environ["DB_ADDR"]

    def __init__(self):
        self.api_ctx = None
        self.uploader = None

