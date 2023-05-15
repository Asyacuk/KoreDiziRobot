import os
import logging

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from utils import Media, __init__

START_MSG= """
**Merhaba, ben kore dizilerini daha kolay izletebilmek için yapılmış bir botum.**

Burada dosyaları satır içi modda arayabilirsiniz. Sadece aşağıdaki düğmelere basın ve aramaya başlayın.

<i>Ör: Taxi driver 2. sezon veya the uncanny counter....</i>
"""
CHANNELS= -1001869462968
INVITE_MSG= """
Bu botu kullanmak için lütfen @koredizileriguncelleme kanalına katılın.

<i>Kanalda yüklenen dizi ve filmlerin haberini vereceğiz.</i>
"""
ADMINS = 5787717617


logger = logging.getLogger(__name__)


@Client.on_message(filters.command('start'))
async def start(bot, message):
    """Start command handler"""
    if len(message.command) > 1 and message.command[1] == 'subscribe':
        await message.reply(INVITE_MSG)
    else:
        buttons = [[
            InlineKeyboardButton('Arama Yap', switch_inline_query_current_chat=''),
            InlineKeyboardButton('Grupta Ara', switch_inline_query=''),
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(START_MSG, reply_markup=reply_markup)


@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
    """Kanalın temel bilgilerini gönderme"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Beklenmeyen KANAL türü")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):
    """Veritabanındaki toplam dosyaları göster"""
    msg = await message.reply("İşleniyor...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Kaydedilen dosyalar: {total}')
    except Exception as e:
        logger.exception('Toplam dosyalar kontrol edilemedi')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(ADMINS))
async def log_file(bot, message):
    """Log dosyası gönder"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Dosyayı veritabanından silme"""
    reply = message.reply_to_message
    if not (reply and reply.media):
        await message.reply('Silmek istediğiniz dosyaya /delete ile yanıt verin', quote=True)
        return

    msg = await message.reply("İşleniyor...⏳", quote=True)

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media:
            media.file_type = file_type
            break
    else:
        await msg.edit('Bu desteklenmeyen dosya biçimi')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'file_type': media.file_type,
        'mime_type': media.mime_type
    })

    if result.deleted_count:
        await msg.edit('Dosya veritabanından başarıyla silindi')
    else:
        await msg.edit('Dosya veritabanında bulunamadı')
