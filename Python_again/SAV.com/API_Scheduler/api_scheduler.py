import threading
import logging
import requests
import schedule
import sys
import time
from datetime import datetime
from config import URL, DATETIME_FMT, TIME_FMT, LOG_FMT, LOG_FILE

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
lock = threading.Lock()
executed_jobs = 0
run = True
total_jobs = 0

def setup_logging_config():
    formatter = logging.Formatter(LOG_FMT)

    api_log = logging.FileHandler(LOG_FILE)
    api_log.setFormatter(formatter)
    api_log.setLevel(logging.INFO)
    logger.addHandler(api_log)

    console_log = logging.StreamHandler()
    console_log.setFormatter(formatter)
    console_log.setLevel(logging.INFO)
    logger.addHandler(console_log)


def job_thread(job):
    thread = threading.Thread(target=job)
    thread.start()


def parse_timestamp(timestamp: str)->list:
    now = datetime.now()
    try:
        return datetime.strptime(timestamp, TIME_FMT).replace(
            year=now.year, month=now.month, day=now.day
        )
    
    except:
        logger.error(f"Invalid timestamp {timestamp}")


def timestamps_data():
    if len(sys.argv) != 2:
        print("Error: Enter timestamps in the format %H:%M:%S....")
        sys.exit(1)

    return [parse_timestamp(tstamps.strip()) for tstamps in sys.argv[1].split(",") if parse_timestamp(tstamps.strip())]


def executable_timestamps():
    now = datetime.now()

    timestamps_list = timestamps_data()

    return [current_tstamps for current_tstamps in timestamps_list if current_tstamps >= now]


def fetch_data():

    curl_header = {"User-Agent": "curl/8.0.1"}
    try:
        response = requests.get(URL, headers=curl_header, timeout=5)
        response.raise_for_status()
        logger.info("Successfully called API at ifconfig.co")

        global executed_jobs, run

        with lock:
            executed_jobs += 1

            if executed_jobs == total_jobs:
                run = False

        return response.text
    
    except requests.HTTPError as e:
        executed_jobs += 1

        if executed_jobs == total_jobs:
            run = False

        logger.error(f"HTTP Error")
    
    except requests.ConnectionError as c:
        executed_jobs += 1

        if executed_jobs == total_jobs:
            run = False
            
        logger.error(f"Failed to connect '{URL}'")


def schedule_timestamps():
    global total_jobs
    timestamps = executable_timestamps()
    
    total_jobs = len(timestamps)
    
    if timestamps:
        for tstamps in timestamps:
            schedule.every().day.at(datetime.strftime(tstamps, TIME_FMT)).do(job_thread, fetch_data)
            logger.info(f"Scheduled API call at {tstamps}")
        return True
    
    else:
        logger.warning("No timestamps to schedule")
        return False


def run_schedule():
    exec_tstamps = executable_timestamps()

    while run:
        schedule.run_pending()
        time.sleep(1)

        print("jobs = ", executed_jobs)
        print("tstamps len = ", len(exec_tstamps))

    

def main():
    setup_logging_config()

    if schedule_timestamps():
        run_schedule()

    logger.info("All timestamps executed for today")

if __name__ == '__main__':
    main()