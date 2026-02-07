import logging
from functools import lru_cache
from logging.handlers import RotatingFileHandler
import sys

LOG_FORMAT = (
    "%(asctime)s | "
    "%(levelname)-8s | "
    "%(name)s | "
    "%(message)s"
)

DATE_FORMAT = "%d-%m-%Y %H:%M:%S %z"

@lru_cache(maxsize=1)
def get_logger(name: str, level: int) -> logging.Logger:

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger
    


    formatter = logging.Formatter(
        fmt=LOG_FORMAT,
        datefmt=DATE_FORMAT
    )

    # Console Handler
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File Handler
    from src import settings

    file_name = settings.LOG_DIR / f"{name}.log"
    file_handler = RotatingFileHandler(
        filename=file_name,
        maxBytes=settings.LOG_MAX_BYTES,
        backupCount=settings.LOG_BACKUP_COUNT,
        encoding="utf-8"
    )
    file_handler.setFormatter(fmt=formatter)
    logger.addHandler(file_handler)

    return logger