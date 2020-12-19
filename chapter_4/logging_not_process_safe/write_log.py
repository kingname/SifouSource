import time
import logging
import datetime
from multiprocessing import Pool
from logging.handlers import TimedRotatingFileHandler


def write_log(logger_name):
    logger = logging.Logger(logger_name)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    steam_handler = logging.StreamHandler()

    rotate_time = datetime.datetime(2020, 10, 7, 19, 19,)
    file_handler = TimedRotatingFileHandler(filename='example.log',
                                            when='midnight',
                                            atTime=rotate_time)

    file_handler.setFormatter(formatter)
    steam_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(steam_handler)

    i = 0
    while True:
        i += 1
        logger.info(f'这是第{i}条信息')
        time.sleep(0.1)


with Pool(3) as pool:
    pool.map(write_log, ['进程1', '进程2', '进程3'])
