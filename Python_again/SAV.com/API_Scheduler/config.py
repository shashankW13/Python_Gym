import logging
import os

URL = 'https://ifconfig.c'

LOG_FILE = 'ifconfig.log'

TIME_FMT = "%H:%M:%S"

DATETIME_FMT = "%Y-%m-%d"

current_dir = os.path.dirname(__file__)
LOG_FILE = os.path.join(current_dir, 'ifconfig.log')

LOG_FMT = '%(asctime)s - [%(levelname)s]: %(message)s'