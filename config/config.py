import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 😌 -----------------------

API_ID = int(getenv("API_ID", "11360899"))
API_HASH = getenv("API_HASH", "b3a49413dfcaf0a16bd6d15e49772d70")
BOT_TOKEN = getenv("BOT_TOKEN", "5586184860:AAGs2JhgY62py6rJSNQhf4fO0owE9dJzRv4")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "AQCM5QJLq0JljEwD09d0chpThQlH_R38HoQBnrTB18YfNjWydUECmLMlJj9P_QawAhGH9wg1yPNx8s5VReLmLAQIx3B3aflLHU2FdJiNVjwfedJLsrVO-7EqCNqbRH2p4Ln8o5ejByyXiSsYptDJmg5Ab2oyVtJ0wN_CChyn153KnlOp3Mi_tZzwvK7K4286Jb5z5xJBGOZe2_0D-hFLlVo2jjwCWy4ujyBYgO3k4YQ2AtpJ1bxeqTEv7nQFO5fda6rGcjcQcxIKIWFqarhai5jvHTDKBCRl4XDmrMrMCj8bsdF3A_lkHntBCo5t1gMywuvIBUa4ANNx2R3JqmNmmuhQAAAAAT2xSecA")
BOT_USERNAME = getenv("BOT_USERNAME", "gxgfgffybot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5329996263").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5329996263").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001956961601")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://R:R@cluster0.t1nml.mongodb.net/?retryWrites=true&w=majority")
#________________________ Updates 🍃 & Music bot name________________
NETWORK = getenv("NETWORK", "Telugucodersupdates")
GROUP = getenv("GROUP", "tgshadow_fighters")
BOT_NAME = getenv("BOT_NAME", "Amala Music")
BANNED_USERS = filters.user()

#************************* Image Stuff 💕 ****************************

IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/d08d6474628be7571f013.png") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/bc5556476395a0c8e109b.jpg")

aiohttpsession = aiohttp.ClientSession()


