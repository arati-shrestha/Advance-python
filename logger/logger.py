# import logging
# logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(name)s-%(levelname)s-%(message)s', datefmt = '%m/%d/%Y %H:%M:%S')
# # logging.debug("this is a debug message")
# # logging.info('this is an info message')
# # logging.warning('this is a warning message')
# # logging.error('this is an error message')
# # logging.critical('this is a critical message')

# logger = logging .getLogger(__name__)

# #create handler
# stream_h = logging.StreamHandler()
# file_h = logging.FileHandler('file.log')

# #level and the format 
# stream_h.setLevel(logging.WARNING)
# file_h.setLevel(logging.ERROR)

# formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# stream_h.setFormatter(formatter)
# file_h.setFormatter(formatter)

# logger.addHandler(stream_h)
# logger.addHandler(file_h)

# logger.warning('this is a warnig')
# logger.error('this is an error')

# import logging.config
# logging.config.fileConfig('logging.conf')
# logger = logging.getLogger('simpleExample')
# logger.debug('this is a debug message')
# import traceback
# try:
#     a = [1,2,3]
#     val = a[4]
# except :
#     logging.error('the error is %s', traceback.format_exc())

# import logging
# from logging.handlers import RotatingFileHandler

# logger  = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)

# handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount = 5)
# logger.addHandler(handler)

# for _ in range(10000):
#     logger.info("hello world")
    
#Using timed rotating file handler : use when your application is running for a long time

import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger  = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler("timed_test.log", when = 's',interval=5, backupCount = 5)
logger.addHandler(handler)

for _ in range(6):
    logger.info("hello world")
    time.sleep(5)
    
    





