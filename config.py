"""Config fill properly"""
import os

API_ID = int(os.environ.get("API_ID", "20729355"))
API_HASH = os.environ.get("API_HASH", "3559855a79208a95323343c56b142220")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6096307685:AAFQ_96C21XeW0bU3PBwN8oai8n56JF8OqQ")
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://Aamirjemadar01:aamir01@cluster0.uyclyiz.mongodb.net/?retryWrites=true&w=majority")
DB_URI = os.environ.get("ELEPHANT_SQL", "postgres://jcnfgwip:R2Y9NPWvALAp90UHd1kwPbt6f2TsSzOd@babar.db.elephantsql.com/jcnfgwip")
OWNER_ID = int(os.environ.get("OWNER_ID", "5864436910"))
BOT_ID = int(os.environ.get("BOT_ID", "-1001694132088"))
