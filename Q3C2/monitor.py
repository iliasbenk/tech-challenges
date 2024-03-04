import requests
import time
import logging

logger = logging.getLogger('Q3C2')
logger.setLevel(logging.INFO)

handler = logging.FileHandler('alert.txt')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

interval = 60
prev_status = None
while True:
    try:
        response = requests.get('http://localhost:5000/health', timeout=5)

        if response.status_code == 200:
            logger.info('Success')
            prev_status = response.status_code
        else:
            if prev_status != 200:
                logger.error('Web app or DB is down')
            else:
                logger.warning('Web app or DB is down. (x1)')
            prev_status = response.status_code

    except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
        logger.error(f'Web app or DB is down')  #: {e}
        prev_status = 500

    time.sleep(interval)
