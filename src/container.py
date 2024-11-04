from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.pattern import Singleton


class Container(metaclass=Singleton):

    apscheduler = AsyncIOScheduler()

container = Container()
