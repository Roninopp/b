from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "7217645"))
API_HASH = getenv("API_HASH", "78ba6352dd5cdc166fdef5aa84ba7c67")

ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN", "2100096282:AAG2c-iWRPsqoxbRFrioHYnFc5hYzKzhkRY")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001754175512"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://DARKAMAN:DARKAMAN@cluster0.snqhn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1793699293").split()))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/12245022cf675d057b79e.jpg")
START_IMG = getenv("START_IMG")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Ronin_fighters_fd")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", " https://t.me/IMPERIAL_AREnA")

STRING_SESSION = getenv("STRING_SESSION", "BQDDH_N6wtFNKnifc6DfYf6DVhpiMu_CsYoH60CmJ147z5irv-J4-jID869dUPvK3BWms3W7UFPq8tcOXmu_JiJjrI2ILNHnQdmRPD07saD6uWsqWwstUmTS7DpginZFRNT9UgmpplK9EHhNogaBkw5OgV2T10wcPxso4huqabL1g0mOIoqBUHMQ2REfmIQ4euuwISK-Yk_yB19snhcAJR65K8toG4ngaTURJT-BHQbNpRd8P1r06VrB1nx_fuDxEKuVFVgM6VxauxGFdiQHwko4ZQ4mkmR8XiAPl6nAPiBQcRZ0zNObv4ehOtRAvZ5sr2AFHD0IJdIa7MjmNuS7efv9AAAAAUIrqz8A")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1793699293").split()))
