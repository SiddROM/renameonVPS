from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://jairename:jairename@cluster0.a1rlm9j.mongodb.net/?retryWrites=true&w=majority"]
        API_HASH = [str, "752a1fb86785c5bd35eb7b1e42071786"]
        API_ID = [int, 25341724]
        BOT_TOKEN = [str, "6129167866:AAGIEh5O1Zgt_9GLRc3pmaUq6VYeVvTca5o"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 15]
        SLEEP_SECS = [int, 0]
        IS_MONGO = [bool, False]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[5860097723]]
        OWNER_ID = [int, 5976553781]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,""]
        FORCEJOIN_ID = [int,-100123465978]

        TRACE_CHANNEL = [int, 0]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
