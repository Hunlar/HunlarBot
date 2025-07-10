import asyncio
from telethon import TelegramClient, events

# Telegram API bilgileri (my.telegram.org'dan al)
api_id = int("TELEGRAM_API_ID")
api_hash = "TELEGRAM_API_HASH"
bot_token = "TELEGRAM_BOT_TOKEN"

# Grup ve Kanal Ayarları
source_channel = "HunlarBirligi"
target_group = "HunBirligichat"

client = TelegramClient('bot_session', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(chats=source_channel))
async def forward_to_group(event):
    await client.send_message(target_group, event.message)

@client.on(events.NewMessage(pattern="/start"))
async def start_handler(event):
    await event.respond(
        "Hun İmparatorluğu Federasyonuna Bağlı Ülkeler için yapılacak ortak çalışmalar için botun her gruba dahil olması gerekmektedir.\n"
        "Ülkelerin İsimleri: Özbekistan, Pakistan, Arabistan, Suriye, Almanya, Kıbrıs, Türkmenistan, BAE, Kırgızistan.\n"
        "Bu bot İmparatorluk adına tüm ticari anlaşmalar çerçevesinde gerekli parayı kripto yolu ile aktarım için yapılmıştır."
    )

@client.on(events.NewMessage(pattern="/help"))
async def help_handler(event):
    await event.respond(
        "Gerekli kişiye yardım için bilgi verilmiştir. İmparatorluk size desteklerini sağlayacaktır."
    )

print("Bot çalışıyor...")
client.run_until_disconnected()
