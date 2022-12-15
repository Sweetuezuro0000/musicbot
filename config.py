## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AQCgtvEJsux3iGhXPBiH9zcsXybcOHJYDKj8NsuO9OcYsoNz0apr_QY2rWPoXKJ7Gc61GpAwC4t5ZoeopILwxii9kiiIXs8MM6xZZkouJ-oA-hOFYCe7S1hUTPVuqUET90PlrsTYeqRGkIPy9TiE0OhJKisLRFf544vhRGlNtHOJcTfYohiROsVassYhV6qmmMtldUQNqYQ6Un4DZk-YLUFeypl8OR7TQ36hbvHoyCitjax6KL1KLcc8QhTCeA2L1hZ7G_V1yGzN53yeUUiLrj5JDbsitB0m6hSuW5b2ZR3Qzv1gdLK0hrzFua6rjJmTEKiLHBK3DRoUaEp0Yohn_HdVAAAAAVKTWLgA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "5887815440:AAF95gTRiUm0Dl81zOazBBLaF0hO01xb0dc")
BOT_NAME = getenv("BOT_NAME", "Wild")

API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "aakash")
OWNER_USERNAME = getenv("OWNER_USERNAME", "notaakash")
ALIVE_NAME = getenv("ALIVE_NAME", "WiLd")
BOT_USERNAME = getenv("BOT_USERNAME", "wildx_Robot")
OWNER_ID = getenv("OWNER_ID", "1669178360")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "offline_xdx")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "GFC_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "wildupdates")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5540577046").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "540000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/30444b973fc9a8100152e.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/30444b973fc9a8100152e.jpg")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
