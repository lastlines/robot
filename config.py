from os import getenv

from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}


SESSION_NAME = getenv("SESSION_NAME", "BQAfX-b4mqNmKjHPVvm41hV31UbZPQPAPhMtj2GpqCtgrxGdd7_IYNi1lthcMPfNsTXR3jjv64gY7CxkmsvWZJiS-4XGKN2Jw9GqiE88H81mZP_foZqOn4JlJKeskmPCj4uV7Yc8QpHlF55TxpePae2-3OhRykpqKdW3pkgdET93Ek73e1eQfKGm1hwRREudifctV29AnsSXBgfaRCju9DE1N02-5JL12cxg0KogkVeoLJSex13-09MRfvrysYl5DnXKP9-ClzDV39-fnrZ1ASO8aU5yf5ACbnGkU5ZiY7kTaLjUO2Z5E-zOmJ0aoQhHp2Ws1wXfoJQWjy62xqGc3gdJO0OarQA")
BOT_TOKEN = getenv("BOT_TOKEN", "1864672623:AAHdmuI8Wrv5ncaeE9FuQWlm8ECPoQ_dW3g")
BOT_NAME = getenv("BOT_NAME", "𝐑𝐨𝐛𝐨𝐭𝐌𝐮𝐬𝐢𝐜𝐁𝐨𝐭")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "-1001319845035")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/031fc9e0713224a151a2e.png")
API_ID = int(getenv("API_ID", "3448718"))
API_HASH = getenv("API_HASH", "5e6d19055850eb5b35720a87e798d0b0")
BOT_USERNAME = getenv("BOT_USERNAME", "robotxmusic_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "robotassisten")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "robotprojectx")
PROJECT_NAME = getenv("PROJECT_NAME", "𝐑𝐨𝐛𝐨𝐭𝐌𝐮𝐬𝐢𝐜𝐁𝐨𝐭")
OWNER = getenv("OWNER", "@justthetech")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamDaisyX")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "15"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "994286253").split()))
