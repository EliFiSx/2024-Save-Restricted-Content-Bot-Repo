#Join me at telegram @dev_gagan

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "17152322" config("API_ID", default=None, cast=int)
API_HASH = "79d60e6b081d5ea6c3e7d81b4b6d2f28" config("API_HASH", default=None)
BOT_TOKEN = "5670586163:AAGpkeRtZyqt84IauR1r4UoOY7sg8ux642I" config("BOT_TOKEN", default=None)
SESSION = "AQDNvmIAH9aYLKTw4abaqhyOtu1Pg0lIzR2zxiOdAzgsgo830WdVfL9kCKwlbJK7gB0ivvs_7otOIHY7yKwAKOCRDXfU3RLAlQmTyB_g3bmIDAh6-_dRicF1KKCojpXkcMCHEg-DNNoMWqP7q5PIyj6kdW5gA1XYUhXeybJMQpabwxYPJNbjVNMdgWCk1C4fGno1sX0Qcwyw91O7h0D4GISo2YquPzoj0HPmIQ93C_VfA0wu0mxLMbXSYlnq969qSrWiFyZVClIscqydi9kEHBDzbBChheMcNKiyCjJTS0GAKUxRJpPVxNHGSVtnx0Hm_Kccf7CUU2JHteEOBsK13BLjk_FHbQAAAAAjWxWuAA" config("SESSION", default=None)
FORCESUB = "save_restricted_EliFiS" config("FORCESUB", default=None)
AUTH = "593171886" config("AUTH", default=None)
SUDO_USERS = "1095846869" []

if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Your session expired please re add that... thanks @dev_gagan.")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
