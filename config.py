from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    LOGGER = True

    API_ID = getenv("API_ID", "27175096")
    API_HASH = getenv("API_HASH", "22930f3501fc1c277e707d385c772547
Api hash")
    ARQ_API_KEY = "PMPTTD-HOMLMF-SRBHNH-RZMWXL-ARQ"
    SPAMWATCH_API = None
    TOKEN = getenv("TOKEN", "6560530370:AAGbw_AIz_QQaEETuu2hA4U3DDXcysV-kAk")
    OWNER_ID = int(getenv("OWNER_ID", 5938660179))
    OWNER_USERNAME = getenv("OWNER_USERNAME", "anshull_1")
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "shoko_support")
    LOGGER_ID = int(getenv("LOGGER_ID", "-1001980710142"))
    MONGO_URI = getenv("MONGO_DB_URI", "mongodb+srv://anshul:swayam@cluster0.jiphfti.mongodb.net/?retryWrites=true&w=majority")
    DB_NAME = getenv("DB_NAME", "Komi")
    REDIS_URL = "redis://default:wK6ZCiclq4iQKYpgfY90v6kd6WdPfEwl@redis-10186.c263.us-east-1-2.ec2.cloud.redislabs.com:10186/default"
    DATABASE_URL = getenv("DATABASE_URL", None)

    # ɴᴏ ᴇᴅɪᴛ ᴢᴏɴᴇ
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
