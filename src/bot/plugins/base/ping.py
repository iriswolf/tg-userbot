from typing import Any

from pyrogram import Client, filters
from pyrogram.types import Message

prefixes = ['.', '/', '!']

@Client.on_message(
    filters.user(['me'])
    & filters.command(
        commands=[
            'ping',
        ],
        prefixes=prefixes
    )
)
async def ping_cmd(client: Client, message: Message) -> Any:
    await message.reply('PONG')
