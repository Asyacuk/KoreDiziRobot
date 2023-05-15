import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 18577871
API_HASH = '3a8a750fe99471542ce566266eb3a914'
BOT_TOKEN = '6132476790:AAGB-1tK_FHEwS12_vkT_4Q2jOXQ1l6nn50'
USERBOT_STRING_SESSION = 'BAEbec8Ao3yYa6Uc-jGyCVl5Uo-b_GpljRFrrqv2W5Gv9cXaxncWmliUW-o2Us6VheKJga1zmRFguCyPCcMVPmR0KMeAdKPByvrRWXRf8j1FfMEzvEOgTg-QU0-C794PPhgCOpRq3sSS0pXH3IiLWjxBHxEq2s46jfVxrnuEhEpbFh_U-zNaKo-vN1w5L1e-rkvm-9tLkYjNLhQGMeySbleWFUz1I7VFFh1ow1p33bpC_aAHC5_UjbyWJ-qH_dtetQ3K4Sv1V0TkmU3zTIT72IGCRoIKhTQY0Mcwb4SmYY2T-zBFRxzwfYft572OyOarQp7fwcqHTQdnQj0lJ9gW9Q2bdy73kQAAAABMDvF3AA'

# Bot settings
CACHE_TIME =  300
USE_CAPTION_FILTER =  False

# Admins, Channels & Users
ADMINS = 5787717617
CHANNELS = -1001869462968
auth_users = 'AUTH_USERS'
AUTH_USERS = ''
auth_channel = 'AUTH_CHANNEL'
AUTH_CHANNEL = '1001849374845'

# MongoDB information
DATABASE_URI = 'mongodb+srv://Asyacuk:Ahmed.0012@clusters.vyb9dcc.mongodb.net/?retryWrites=true&w=majority'
DATABASE_NAME = 'korediziizle'
COLLECTION_NAME = 'Telegram_files'

# Messages
default_start_msg = """
**Merhaba, ben kore dizilerini daha kolay izletebilmek için yapılmış bir botum.**

Burada dosyaları satır içi modda arayabilirsiniz. Sadece aşağıdaki düğmelere basın ve aramaya başlayın.

<i>Ör: Taxi driver 2. sezon veya the uncanny counter....</i>
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Kore Dizilerini daha kolay izleyebilmek için {username} kullanın'
INVITE_MSG = environ.get('INVITE_MSG', """
Bu botu kullanmak için lütfen @koredizileriguncelleme kanalına katılın.

<i>Kanalda yüklenen dizi ve filmlerin haberini vereceğiz.</i>
""")