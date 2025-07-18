import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMINS = list(map(int, os.getenv("ADMINS", "").split(",")))
DEV_USERNAME = os.getenv("DEV_USERNAME")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")

channel_id = os.getenv("CHANNEL_ID")
if channel_id is None:
    raise ValueError("CHANNEL_ID environment variable is not set.")
CHANNEL_ID = int(channel_id)
