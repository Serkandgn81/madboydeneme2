import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "29938341"))
API_HASH = getenv("API_HASH", "234eeead61912d630aaacbad924b0789")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "6757500151:AAFJxbQZEB7CUYNUphUmgQj4XfrLfDHInNc")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://madpanel:madboy11@atlascluster.gprqayn.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")


DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 960))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002182187594"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "5901320319"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://t.me/DostTicaret",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/GeceExpress")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/GeceExpress")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "None")

# Time after which you're assistant account will leave chats automatically.

AUTO_LEAVE_ASSISTANT_TIME = int(

    getenv("ASSISTANT_LEAVE_TIME", "3400")

)  # Remember to give value in Seconds

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2041df9cbcd142cba804578a2cf85939")

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "80ffd296320e49299830e80b11e3bf73")

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAHI0qUAMqBynuMk9OtaBWNLNohPYSz-AV-2zolE6C3v35BrqA2EYDA47TrFgG2wVP6CBTvXr7MhybhMlHXD18NtSA3G863UKDj9ndKY1cdZVhav4IUKVe0g5MnVv0WOFLT9Ep5o1jQJuujqJBZ1XgwZQjFuf_4dGFQNw1f0jaHCyHC7DzTqjypuev2HOSLsWH6KK0W9MwK4k7yyfVk5ceklZ5EIXSW3raHI9pQEvRNaZP2BQnuzWCTTUwyFtmdOGLCM5ywD7dz5LZt5mGKcw1k1zgseVsVkD4to6us3YlYPon-ufT1SKZPV9tRm9JWotPYfFosziV9nv4hz_YkMzoLq8Cx7AAAAAAG0r2kqAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbo2pvt1D14-cp4ChdEBSukZC55OCmhv8KIsKH8DtDvg-o2aB76ON7CN6_&s=10"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbo2pvt1D14-cp4ChdEBSukZC55OCmhv8KIsKH8DtDvg-o2aB76ON7CN6_&s=10"
)
PLAYLIST_IMG_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbo2pvt1D14-cp4ChdEBSukZC55OCmhv8KIsKH8DtDvg-o2aB76ON7CN6_&s=10"
STATS_IMG_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbo2pvt1D14-cp4ChdEBSukZC55OCmhv8KIsKH8DtDvg-o2aB76ON7CN6_&s=10"
TELEGRAM_AUDIO_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbo2pvt1D14-cp4ChdEBSukZC55OCmhv8KIsKH8DtDvg-o2aB76ON7CN6_&s=10"
TELEGRAM_VIDEO_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbo2pvt1D14-cp4ChdEBSukZC55OCmhv8KIsKH8DtDvg-o2aB76ON7CN6_&s=10"
STREAM_IMG_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbo2pvt1D14-cp4ChdEBSukZC55OCmhv8KIsKH8DtDvg-o2aB76ON7CN6_&s=10"
SOUNCLOUD_IMG_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbo2pvt1D14-cp4ChdEBSukZC55OCmhv8KIsKH8DtDvg-o2aB76ON7CN6_&s=10"
YOUTUBE_IMG_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbo2pvt1D14-cp4ChdEBSukZC55OCmhv8KIsKH8DtDvg-o2aB76ON7CN6_&s=10"
SPOTIFY_ARTIST_IMG_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbo2pvt1D14-cp4ChdEBSukZC55OCmhv8KIsKH8DtDvg-o2aB76ON7CN6_&s=10"
SPOTIFY_ALBUM_IMG_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbo2pvt1D14-cp4ChdEBSukZC55OCmhv8KIsKH8DtDvg-o2aB76ON7CN6_&s=10"
SPOTIFY_PLAYLIST_IMG_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbo2pvt1D14-cp4ChdEBSukZC55OCmhv8KIsKH8DtDvg-o2aB76ON7CN6_&s=10"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
