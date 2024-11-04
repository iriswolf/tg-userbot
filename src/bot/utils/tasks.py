import asyncio
from typing import Callable, Optional


async def create_interval_task(
        callback: Callable,
        args: Optional[list] = None,
        kwargs: Optional[dict] = None,
        seconds: int = 0
) -> None:
    args = args or []
    kwargs = kwargs or {}

    while True:
        await callback(*args, **kwargs)
        await asyncio.sleep(seconds)


async def create_counted_interval_task(
        callback: Callable,
        args: Optional[list] = None,
        kwargs: Optional[dict] = None,
        count: int = 1,
        seconds: int = 0
) -> None:
    args = args or []
    kwargs = kwargs or {}

    for i in range(count):
        await callback(*args, **kwargs)
        await asyncio.sleep(seconds)
