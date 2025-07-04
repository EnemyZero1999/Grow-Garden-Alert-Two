from website_bot import run_scraper
import time
from datetime import datetime

def is_active_time():
    now = datetime.now().hour
    return 7 <= now < 24

while True:
    if is_active_time():
        print("🌞 Checking stock...")
        run_scraper()
    else:
        print("🌙 Sleeping (midnight to 7AM)")
    time.sleep(300)  # 5 minutes
