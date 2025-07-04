from utils import send_discord_alert
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

KEYWORDS = [
    "Bug Egg", "Mythical Egg", "Paradise Egg", "Master Sprinkler",
    "Tanning Mirror", "Sugar Apple", "Pitcher Plant", "Basic Sprinkler", "Carrot"
]

def run_scraper():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)

        ### 🥇 PRIMARY SITE
        driver.get("https://www.gamersberg.com/grow-a-garden/stock?webpush=true")
        time.sleep(5)  # wait for site to load

        all_text = driver.page_source

        for keyword in KEYWORDS:
            if keyword.lower() in all_text.lower():
                print(f"🟡 Found: {keyword}")
                send_discord_alert(f"🟡 `{keyword}` is in stock on Gamersberg!")

        ### 🥈 BACKUP SITE
        driver.get("https://arcaiuz.com/grow-a-garden-stock")
        time.sleep(5)
        try:
            refresh_button = driver.find_element("xpath", "//button[contains(., 'Refresh')]")
            refresh_button.click()
            time.sleep(3)
        except Exception as e:
            print("⚠️ Couldn't click refresh on Arcaiuz")

        all_text = driver.page_source
        for keyword in KEYWORDS:
            if keyword.lower() in all_text.lower():
                print(f"🟢 Found (backup): {keyword}")
                send_discord_alert(f"🟢 `{keyword}` is in stock on Arcaiuz!")

        driver.quit()

    except Exception as e:
        print(f"❌ Scraper Error: {e}")
