# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "22318866")

API_HASH = os.environ.get("API_HASH", "7fcac00bc99a1fb23b7563115fd079a6")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7164061796:AAF_J9VfukIqwH93r2K9VpixfykW3K0xm7k") 

FORCE_SUB = os.environ.get("FORCE_SUB", "SSABOTS") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "SSARENAMER_4GBBOT")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://BOTMAKERS6:/BOTMAKERS6@cluster0.a2dbeeo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/187fd995e71153c88b08a.jpg")
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1170337923').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
