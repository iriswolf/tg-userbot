import asyncio
import re
from asyncio import Task
from typing import Any
from venv import logger

from pyrogram import Client, filters
from pyrogram.types import Message

from src.bot.utils.user_storage import UserMemoryStorage
from src.bot.utils.tasks import create_interval_task, create_counted_interval_task
from src.bot.utils.send_message import send_message

prefixes = ['.', '/', '!']

@Client.on_message(
    filters.user(['me'])
    & filters.command(
        commands=[
            'repeat',
            'повтори',
            'п'
        ],
        prefixes=prefixes
    )
)
async def repeat_cmd(client: Client, message: Message) -> Any:
    reg = re.match(r'\S+ (\d+) (\d+)\s(.*)', message.text, re.IGNORECASE | re.MULTILINE)

    repeat_count = reg.group(1)
    repeat_interval = reg.group(2)
    repeat_text = reg.group(3)

    user_storage = UserMemoryStorage()

    logger.info(123)

    kwargs = {
        'client': client,
        'chat_id': message.chat.id,
        'message': repeat_text
    }

    if user_storage.get('repeat_task'):
        return await message.edit('Не возможно запустить задачу, уже есть одна запущенная задача')

    el = asyncio.get_running_loop()
    task = None

    if repeat_count == 0:
        task = el.create_task(
            create_interval_task(
                send_message,
                kwargs=kwargs,
                seconds=int(repeat_interval)
            )
        )
    else:
        task = el.create_task(
            create_counted_interval_task(
                send_message,
                kwargs=kwargs,
                seconds=int(repeat_interval),
                count=int(repeat_count)
            )
        )

    logger.info('Создана задача на повтор')
    logger.info(task)
    logger.info(task.cancelled())

    user_storage.set('repeat_task', task)

    await task
    await message.delete()


@Client.on_message(
    filters.user(['me'])
    & filters.command(
        commands=[
            'уп'
        ],
        prefixes=prefixes
    )
)
async def del_repeat_cmd(client: Client, message: Message) -> Any:
    user_storage = UserMemoryStorage()

    if user_storage.get('repeat_task') is None:
        return await message.reply('Задачи на повтор и так нет')

    task: Task = user_storage.get('repeat_task')

    if not task.cancelled():
        task.cancel()

    user_storage.set('repeat_task', None)

    logger.info('Удалена задача на повтор')
    logger.info(task)
    logger.info(task.cancelled())

    return await message.reply('Задача удалена')
