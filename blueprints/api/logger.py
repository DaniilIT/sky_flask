import logging


FORMATTER = logging.Formatter('%(asctime)s [%(levelname)s]Запрос %(message)s', datefmt='%Y-%m-%d %H:%M:%S')


class Logger:
    def __init__(self, log_name: str):
        handler = logging.FileHandler(log_name, mode='a')
        handler.setFormatter(FORMATTER)

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)

        self.logger = logger

    def record_info(self, message: str):
        """ Записать сообщение в log
        """
        self.logger.info(message)
