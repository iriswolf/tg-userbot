from pathlib import Path


CWD = Path.cwd()

# src
SRC_FOLDER_PATH = CWD.joinpath('src')

# bot
BOT_FOLDER_PATH = SRC_FOLDER_PATH.joinpath('bot')

# plugins
PLUGINS_MODULE_PATH = 'src.bot.plugins'
PLUGINS_RESOURCES_MODULE_PATH = 'resources'
PLUGINS_INCLUDE_MODULE_PATHS = [
]
PLUGINS_EXCLUDE_MODULE_PATHS = [
]

# logs
LOGS_FOLDER_PATH = CWD.joinpath('logs')
LOG_FILE_PATH = LOGS_FOLDER_PATH.joinpath('log_{time}.log')

# APS
APS_REPEAT_TASK_ID = 'repeat_task'
