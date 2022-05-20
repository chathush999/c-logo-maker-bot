
"/app/Github_Repo/null.py", line 1, in <module>
2022-05-20T11:55:22.603821+00:00 app[worker.1]:     from null import app
2022-05-20T11:55:22.603848+00:00 app[worker.1]: ImportError: cannot import name 'app' from partially initialized module 'null' (most likely due to a circular import) (/app/Github_Repo/null.py)

from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# API By TechZBots || https://t.me/TechZBots
LOGO_API_URL1 = "https://techzbotsapi.herokuapp.com/logo?text="

LOGO_API_URL2 = "https://techzbotsapi.herokuapp.com/logo?square=true&text="
