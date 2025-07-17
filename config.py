import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
ADMINS = list(map(int, os.getenv("ADMINS", "").split(",")))
DEV_USERNAME = os.getenv("DEV_USERNAME")
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME")
