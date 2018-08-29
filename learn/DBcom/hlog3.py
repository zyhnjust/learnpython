#this is not finished.

import logging

logger = logging.getLogger("simpletest")
logger.setLevel(logging.DEBUG)

fh=logging.FileHandler("simpletest.log")
fh.setLevel(logging.DEBUG)

ch=logging.StreamHandler()
ch.setLevel(logging.ERROR)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(level)s - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.info('THis is infor level log')
logger.info("This is error level log")

a = Auxiliary
