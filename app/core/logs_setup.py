import logging
import sys
from config import settings

def logging_setup():
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, settings.loglevel, logging.INFO))

    console_handler = logging.StreamHandler(sys.stdout)
    # file_handler = logging.FileHandler("logs.log", mode="a", encoding="UTF-8")

    '''formatting'''
    formatter = logging.Formatter(
        "[{asctime}] {levelname}, {filename}:{lineno} - {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M"
    )

    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # file_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)

    return logger