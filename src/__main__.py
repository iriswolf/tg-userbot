import asyncio

from src import bot, logging, consts
from src.settings import settings


async def main() -> None:
    await bot.setup(
        settings.session_filename,
        settings.api_id,
        settings.api_hash,
        settings.app_version,
        consts.CWD,
        consts.PLUGINS_MODULE_PATH,
        consts.PLUGINS_INCLUDE_MODULE_PATHS,
        consts.PLUGINS_EXCLUDE_MODULE_PATHS
    )




if __name__ == '__main__':
    from src.container import container

    logging.setup('DEBUG' if settings.debug else 'INFO')

    container.apscheduler.start()

    asyncio.run(main())