from datetime import datetime, timedelta, date
import subprocess
import urllib.request
import threading
import requests
import schedule
import logging
import sys
import time
from config import URL, LOGGER, DATETIME_FMT


def config_logging():
    formatter = logging.Formatter('%(asctime)s - [%(levelname)s]: %(message)s')

    LOGGER.setLevel(logging.INFO)
    api_log = logging.FileHandler('ifconfig.log')
    api_log.setFormatter(formatter)
    LOGGER.addHandler(api_log)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    LOGGER.addHandler(console_handler)

def job_thread(job):
    thread = threading.Thread(target=job)
    thread.start()

def parse_timestamps(time):
    try:
        return datetime.strptime(time, DATETIME_FMT)
    
    except Exception as e:
        LOGGER.error(f"Invalid time format: {time}")
        return

def timestamp_data():
    if len(sys.argv) != 2:
        print("Error: Please enter timestamps")
        sys.exit(1)

    timestamp_list = [t.strip() for t in sys.argv[1].split(",")]
    return timestamp_list

def fetch_data():
    # response = urllib.request.urlopen(URL)
    # print(response.read().decode())
    try:
        headers = {"User-Agent": "curl/8.0.1"}
        response = requests.get(URL, headers=headers)
        print(response.text)
        LOGGER.info("Succesfully called ifconfig.io")
        
    except requests.exceptions.RequestException as e:
        LOGGER.error(e)
        return f"Error: {e}"
    
    except requests.exceptions.HTTPError as e:
        LOGGER.error(e)
        return f"Error: {e}"

    # response = subprocess.run(['curl', URL],
    #                           capture_output=True,
    #                           text=True,
    #                           check=True)
    # print(response.stdout.strip())

def next_call(ptimestamp, pcurrent_time):
    # timestamps_list = timestamp_data()
    today = date.today()

    wait_seconds = (datetime.combine(today, ptimestamp) - datetime.combine(today, pcurrent_time)).total_seconds()
    return wait_seconds
    
def main():
    config_logging()
    timestamps = timestamp_data()
    timestamps.sort()

    data_len = len(timestamps)
    print(data_len)

    for i, tstamps in enumerate(timestamps):
        # schedule.every().day.at(tstamps).do(job_thread, fetch_data)
        now = datetime.now()
        current_time = now.strftime(DATETIME_FMT)

        parsed_current_time = parse_timestamps(current_time).time()
        try:
            parsed_timestamp = parse_timestamps(tstamps).time()
        except:
            continue

        print(i, tstamps)
        print("now", parsed_current_time)

        if i + 1 <= len(timestamps):
            if parsed_current_time <= parsed_timestamp:
                wait_seconds = next_call(parsed_timestamp, parsed_current_time)
                LOGGER.info(f"Next call at {tstamps}, waiting for {wait_seconds:.0f} seconds....")
                time.sleep(wait_seconds)

                job_thread(fetch_data)
            else:
                print("continue", i, parsed_timestamp)
                continue
        
        else:
            LOGGER.info("All timestamps executed for today")
            break

    # for _ in range(data_len):
    #     schedule.run_pending()
    #     time.sleep(1)

if __name__ == '__main__':
    main()
    



