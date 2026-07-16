import logging

import os


class Logger:

    @staticmethod
    def get_logger(name):

        logger = logging.getLogger(name)

        logger.setLevel(logging.INFO)

        if logger.hasHandlers():
            return logger

        os.makedirs("logs", exist_ok=True)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler("logs/automation.log")

        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.addHandler(console_handler)

        return logger