import logging

logger = logging.getLogger('pyrogram_logger')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')
file_handler = logging.FileHandler('telegram-bot.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)
logger.addHandler(file_handler)

