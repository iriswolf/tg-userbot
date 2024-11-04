from pyrogram import Client


async def send_message(client: Client, chat_id: int, message: str) -> None:
    await client.send_message(chat_id, text=message)
