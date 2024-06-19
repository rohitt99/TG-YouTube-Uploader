import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6824943579:AAF5GUHPUA5nDZuspI1c24HZr3ywXOMPKI0")

    APP_ID = int(os.environ.get("APP_ID", 25830228))

    API_HASH = os.environ.get("API_HASH", "a23a5133bddbdab87df3df06ccf63a89")

    AUDIO_THUMBNAIL = os.environ.get("AUDIO_THUMBNAIL", "https://graph.org/file/350c9c541ecf4f2c67070.jpg")

    VIDEO_THUMBNAIL = os.environ.get("VIDEO_THUMBNAIL", "https://graph.org/file/fc3fff668765511b35f5b.jpg")
