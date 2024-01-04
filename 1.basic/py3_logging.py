import logging


def logout():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s  %(levelname)s : %(message)s',
        datefmt='%Y/%m/%d %H:%M:%S')
    logging.debug("debug log")
    logging.warning("warnning log")
    logging.info("info log")
    logging.error("error log")
    logging.critical("critical log")


def loggerTest():
    logger = logging.getLogger("test")
    logger.debug("logger debug")


logout()
loggerTest()
