#@cantarellabots
import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.environ.get("API_ID", "36428426"))
API_HASH = os.environ.get("API_HASH", "30cba30aa38699e77ce264365e327528")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8858829135:AAHgq28I0gTGfrcDUoL2kh4cE4RFXsUivWs")

SET_INTERVAL = int(os.environ.get("SET_INTERVAL", 60))  # in seconds, default 1 hour
TARGET_CHAT_ID = os.environ.get("TARGET_CHAT_ID", "-1003911956936")
MAIN_CHANNEL = os.environ.get("MAIN_CHANNEL", "-1003937893306") # Change as needed
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1003912488328")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://animekyoto:W5Itr6v2bZ3KpQF8@cluster0.trg5dtc.mongodb.net/?appName=Cluster0")
MONGO_NAME = os.environ.get("MONGO_NAME", "cantarellabots")
OWNER_ID = int(os.environ.get("OWNER_ID", "8663573756"))
ADMIN_URL = os.environ.get("ADMIN_URL", "@nyx_lostcore")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Sasaki_AnimexBot")
FSUB_PIC = os.environ.get("FSUB_PIC", "https://files.catbox.moe/bli70r.jpg")
FSUB_LINK_EXPIRY = int(os.environ.get("FSUB_LINK_EXPIRY", 600))
START_PIC =os.environ.get("START_PIC", "https://files.catbox.moe/4b8jvw.jpg")

# ─── Filename & Caption Formats ───
FORMAT = os.environ.get("FORMAT", "{title} - [S{season}-E{episode}] [{quality}] [{audio}] @Anime_Kyoto")
CAPTION = os.environ.get("CAPTION", "{FORMAT}")

# ─── Progress Bar Settings ───
PROGRESS_BAR = os.environ.get("PROGRESS_BAR", """
<blockquote> {bar} </blockquote>
<blockquote>📁 <b>{title}</b>
⚡ Speed: {speed}
📦 {current} / {total}</blockquote>
""")

# ─── Response Images ───
# Rotating anime images sent with every bot reply. Add as many as you like.
RESPONSE_IMAGES = [
    "https://files.catbox.moe/5oonsm.jpg",
    "https://files.catbox.moe/9ufgme.jpg",
    "https://files.catbox.moe/4b8jvw.jpg",
    "https://files.catbox.moe/bli70r.jpg",
    "https://files.catbox.moe/uce0lw.jpg",
    "https://files.catbox.moe/is7q4q.jpg"
]
