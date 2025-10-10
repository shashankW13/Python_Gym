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

def duplicate_timestamps():
    duplicate_tstamps = {}
    timestamps_list = timestamp_data()

    for tstamps in timestamps_list:
        count = timestamps_list.count(tstamps)
        
        if count > 1:
            dups = [tstamps for _ in range(count)]
            duplicate_tstamps[tstamps] = dups
                
        else:
            continue

    return duplicate_tstamps



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

def wait_time():
    pass
    
def main():
    print("Duplicate", duplicate_timestamps())
    config_logging()
    timestamps = timestamp_data()
    timestamps.sort()

    LOGGER.info(f"Scheduling {len(timestamps)} timestamps...")

    now = datetime.now()
    future_timestamps = []

    for t in timestamps:
        try:
            t_dt = parse_timestamps(t).replace(
                year=now.year, month=now.month, day=now.day
            )
            if t_dt >= now:
                future_timestamps.append(t)
        except:
            print(f"Invalid timestamp {t}")
            continue

    job_len = len(future_timestamps)
    executed_jobs = 0
    print(job_len)

    for tstamps in future_timestamps:
        schedule.every().day.at(tstamps).do(job_thread, fetch_data)
        LOGGER.info(f"Scheduled call at {tstamps}")

    LOGGER.info("All jobs scheduled. Waiting for execution...")

    while executed_jobs < job_len:
        now = datetime.now()
        next_run = schedule.next_run()
        if not next_run:
            break
        
        wait_time = (next_run - now).total_seconds()
        if wait_time > 0:
            LOGGER.info(f"Next job at {next_run.time()}, waiting {wait_time:.1f} seconds...")
            time.sleep(wait_time)

        executed_jobs += 1

        schedule.run_pending()

        
    LOGGER.info("All timestamps executed successfully.")


            

    # for i, tstamps in enumerate(timestamps):
    #     # schedule.every().day.at(tstamps).do(job_thread, fetch_data)
    #     now = datetime.now()
    #     current_time = now.strftime(DATETIME_FMT)

    #     parsed_current_time = parse_timestamps(current_time).time()
    #     try:
    #         parsed_timestamp = parse_timestamps(tstamps).time()
    #     except:
    #         continue

    #     print(i, tstamps)
    #     print("now", parsed_current_time)

    #     if i + 1 <= len(timestamps):
    #         if parsed_current_time <= parsed_timestamp:
    #             wait_seconds = next_call(parsed_timestamp, parsed_current_time)
    #             LOGGER.info(f"Next call at {tstamps}, waiting for {wait_seconds:.0f} seconds....")
    #             time.sleep(wait_seconds)

    #             job_thread(fetch_data)
    #         else:
    #             print("continue", i, parsed_timestamp)
    #             continue
        
        # else:
        #     LOGGER.info("All timestamps executed for today")
        #     break

    # for _ in range(data_len):
    #     schedule.run_pending()
    #     time.sleep(1)

if __name__ == '__main__':
    main()
    



