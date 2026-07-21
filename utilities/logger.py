import logging
import os


class Logger:

    @staticmethod
    def get_logger(name):
        logger = logging.getLogger(name)

        if not logger.handlers:
            logger.setLevel(logging.INFO)
            os.makedirs("logs", exist_ok=True)
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )
            file_handler = logging.FileHandler(
                "logs/automation.log",
                encoding="utf-8"
            )
            file_handler.setLevel(logging.INFO)
            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
            logger.propagate = False

        return logger