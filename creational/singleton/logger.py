import logging


class Logger:
    logger_instance = None

    def __init__(self):
        raise Exception("Can not create an instance, please use get_instance()")

    @staticmethod
    def get_instance():
        if Logger.logger_instance is None:
            Logger.logger_instance = Logger.__create_logger()
        return Logger.logger_instance

    @staticmethod
    def __create_logger():
        logger = logging.getLogger("Logger")
        logger.handlers = []
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(threadName)s - %(name)s - %(message)s")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
        logger.propagate = False
        return logging.getLogger("Logger")
