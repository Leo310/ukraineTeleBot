import logging


def setupLogger(name="root"):
    # setup logger
    # creates Logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # formatter to format ouput
    formatter = logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # handler to specify output streams (file, etc)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def getLogger(name="root"):
    return logging.getLogger(name)
