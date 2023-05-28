import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 18577871
API_HASH = '3a8a750fe99471542ce566266eb3a914'
BOT_TOKEN = '6132476790:AAFLozanobHYmHZs1azdEbthnu1s5whl1AY'
USERBOT_STRING_SESSION = 'BACr8zc1jFFg9Igv636IZbHTGWWWQvLqmVVNRwUNIXuiDsb7vm9TkqEevMeOkZgxQCj4RQ2C0sa8rwJ0obtjriN_cDRwvMyshGdU4eTKFEFhBkSj50wYpE5gM8eRLvx8AJWnfHhUw9mih994SiZ85UVyygUPdF4PVdkfnCJGf5BxyE5II4F709zMN3wfCvHcbFjKKieNjHHfrLJjtwtVTmj3XXZ5RCwjbx4awIK5MIBHqhbGaZjRxIZEuak26yM4wd0r3KBuBDnPk7_rhkCrGghGwpf6vd87rdvsUI4iTILvvXXHGLbwjRouIFtbfGdG2WaBFkBfmgVyqZ1uLEhK37U-TA7xdwA'

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
LOG_CHANNEL= -1001945680190

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
