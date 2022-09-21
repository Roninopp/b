from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("7217645"))
API_HASH = getenv("78ba6352dd5cdc166fdef5aa84ba7c67")

ASS_HANDLER = list(getenv(".").split())
BOT_TOKEN = getenv("2100096282:AAEWuPQVLGtcR_csGOG2oZZYriTH3jlFlzg")

DURATION_LIMIT = int(getenv("90"))
LOGGER_ID = int(getenv("-1001644439158"))
MONGO_DB_URI = getenv("mongodb+srv://DARKAMAN:DARKAMAN@cluster0.snqhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("1793699293").split()))

PING_IMG = getenv("https://te.legra.ph/file/12245022cf675d057b79e.jpg")
START_IMG = getenv("START_IMG")

SUPPORT_CHAT = getenv("https://t.me/Ronin_fighters_fd")
SUPPORT_CHANNEL = getenv(" https://t.me/IMPERIAL_AREnA")

STRING_SESSION = getenv("BQClNwiPkR6W5cDavZcHZOOgfs7IjwfTXpi6bbhPQym72EfoSSTE-AL9Cnm32sHn0mJpDg6qElC13N50592PxeQqNm6oEUVTzKH9Z2XpmLeL1a7V8KYiQGi1lIcGrPO8z27nscpQC3sgE9J8XKgO19zAIQfsqEKGMW6MPzCTWKs3qpcGooGNA5gMH08acDEayUZ_eYV3OrRDik0NS5_MzvLHC8Ocr_n4eqQ9ufF7XWnQEFwb-vsj-iapUnpq_Ju_o2uhynyBODHtoEKQxmgTpAd0ln2wfzXWr79kxtekAZi3UCIcQjt3V0OPc4P0R3GjIMXdLUqLKOLMt7YvfKkLn3nHAAAAAUIrqz8A")
SUDO_USERS = list(map(int, getenv("1793699293").split()))
