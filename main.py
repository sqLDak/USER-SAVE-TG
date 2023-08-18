import asyncio
import logging

from telethon import TelegramClient, events

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

api_id = '16890749'
api_hash = 'd5439aaa3ff4ef30696decf6389341ff'

session_name = 'DownL'  # Укажите желаемое имя сессии

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start()
    await client.run_until_disconnected()

@client.on(events.NewMessage(func=lambda e: e.is_private and (e.photo or e.video) and e.media_unread))
async def downloader(event):
    result = await event.download_media()
    await client.send_file("me", result, caption="Downloaded by @sqLDak")

asyncio.run(main())