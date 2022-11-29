## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "AQAKedUjm_J6N6lq4P5BCSBwNvOJvfejEAEF9oaTPoofe_ABAtjCmo43FH6YLOtAFmkfV-NI76EOISjMF45cu_EIrjN1AYq9tXdaVAWv9_fARYYvgwyZzJx04NIOr4RQUh9kXxv_x8XLpYYZWpds8erSizo-f_yqhr4ijYXLw3hUaSEgdWznZPMiL3QXTi_FXAh-Af4QLqig9bw5ZrNoqZr-hHGRY_xNu4KHjPKwGrPlEUuu3j9NVXGtFj9TZI9dJWwIRGLef6KbTyPX3SAE1ETphwRSAuEO0uGjEZBADD7zHYA8sL57qVEZaC05pmq_n9ySIEhFivBAF13LCcuq-sG5AAAAAUT_6vMA")

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

BOT_TOKEN = getenv("BOT_TOKEN", "5558919970:AAHwr6Dk1DbJ0WuOx2PWThaLkoLfmuod-9E")
BOT_NAME = getenv("BOT_NAME", "Umk")

API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "aakash")
OWNER_USERNAME = getenv("OWNER_USERNAME", "wtfaakashxd")
ALIVE_NAME = getenv("ALIVE_NAME", "WiLd")
BOT_USERNAME = getenv("BOT_USERNAME", "wildx_Robot")
OWNER_ID = getenv("OWNER_ID", "1669178360")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "wildmusicass")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "GFC_SUPPORT")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "GFC_C0MMUNITY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5746406426").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "54000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/30444b973fc9a8100152e.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/30444b973fc9a8100152e.jpg")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
