from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Get it from my.telegram.org
API_ID = int(getenv("API_ID", "12995565"))
API_HASH = getenv("API_HASH", "f43e63c6eb71cd9ee988e3b13a509f1a")

## Get it from @Botfather in Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "5247120991:AAE5-Tcb4mqAcVAdEsccc_C7T12K8sG06mw")

# API By TechZBots || https://t.me/Mizutsuki_update
LOGO_API_URL1 = "https://techzbotsapi.herokuapp.com/logo?text="

LOGO_API_URL2 = "https://techzbotsapi.herokuapp.com/logo?square=true&text="
