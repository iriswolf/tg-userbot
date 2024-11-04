from pathlib import Path

from pyrogram import Client, idle

from src.bot.utils.user_storage import UserMemoryStorage

__all__ = ['setup']

async def _client_run(client: Client):
    await client.start()
    await idle()
    await client.stop()


async def setup(
        session_name: str,
        api_id: str,
        api_hash: str,
        app_version: str,
        workdir: Path,
        plugins: str,
        include: list[str],
        exclude: list[str]
) -> None:
    client = Client(
        session_name,
        api_id,
        api_hash,
        app_version,
        lang_code='ru',
        workdir=str(workdir),
        plugins={
            'root': str(plugins),
            'include': include,
            'exclude': exclude
        }
    )

    UserMemoryStorage()

    await _client_run(client)
