
import inspect
import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename='.\\Logs\\automation.log', format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        logger.setLevel(logging.DEBUG)
        return logger
    # def loggen():
    #     loggername = inspect.stack()[1][3]
    #     logger = logging.getLogger(loggername)
    #     filehandler = logging.FileHandler('.\\Logs\\automation.log')
    #     formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    #     filehandler.setFormatter(formatter)
    #     logger.addHandler(filehandler)
    #     logger.setLevel(logging.DEBUG)
    #     return logger