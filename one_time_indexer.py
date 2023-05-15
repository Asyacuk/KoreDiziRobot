import logging
import logging.config

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.WARNING)

import asyncio
from pyrogram import Client
from utils import save_file

SESSION = 'Media_search'
API_ID = 18577871
API_HASH = '3a8a750fe99471542ce566266eb3a914'
BOT_TOKEN = '6132476790:AAGB-1tK_FHEwS12_vkT_4Q2jOXQ1l6nn50'
USERBOT_STRING_SESSION = 'BAEbec8Ao3yYa6Uc-jGyCVl5Uo-b_GpljRFrrqv2W5Gv9cXaxncWmliUW-o2Us6VheKJga1zmRFguCyPCcMVPmR0KMeAdKPByvrRWXRf8j1FfMEzvEOgTg-QU0-C794PPhgCOpRq3sSS0pXH3IiLWjxBHxEq2s46jfVxrnuEhEpbFh_U-zNaKo-vN1w5L1e-rkvm-9tLkYjNLhQGMeySbleWFUz1I7VFFh1ow1p33bpC_aAHC5_UjbyWJ-qH_dtetQ3K4Sv1V0TkmU3zTIT72IGCRoIKhTQY0Mcwb4SmYY2T-zBFRxzwfYft572OyOarQp7fwcqHTQdnQj0lJ9gW9Q2bdy73kQAAAABMDvF3AA'
CHANNELS = [-1001869462968]



async def main():
    """Save old files in database with the help of user bot"""

    user_bot = Client('User-bot', API_ID, API_HASH, session_string=USERBOT_STRING_SESSION, in_memory=True)
    bot = Client(SESSION, API_ID, API_HASH, bot_token=BOT_TOKEN)

    await user_bot.start()
    await bot.start()

    try:
        for channel in CHANNELS:
            async for user_message in user_bot.get_chat_history(channel):
                message = await bot.get_messages(channel, user_message.id, replies=0)
                for file_type in ("document", "video", "audio"):
                    media = getattr(message, file_type, None)
                    if media is not None:
                        break
                else:
                    continue
                media.file_type = file_type
                media.caption = message.caption
                await save_file(media)
    finally:
        await user_bot.stop()
        await bot.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
