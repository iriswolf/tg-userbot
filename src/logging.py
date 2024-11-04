import logging
import sys
from typing import TYPE_CHECKING

from loguru import logger

from src.consts import LOG_FILE_PATH

if TYPE_CHECKING:
    from src.types import LogLevel


class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def setup(log_level: 'LogLevel') -> None:
    logging.basicConfig(
        handlers=[InterceptHandler()],
        level=log_level,
        force=True
    )

    logger.add(
        LOG_FILE_PATH,
        rotation='00:00',
        compression='zip',
        retention='7 days',
        level=log_level,
        colorize=False
    )
