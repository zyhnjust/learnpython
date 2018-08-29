import logging
import sys
'''
logger=logging.getLogger()
logger.info("this is infor level log")
logger.warn("this is warn level log")
logger.error("this is error level log")
'''
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("test")
logger.setLevel(logging.DEBUG)

logger.info("This is info message. ")

