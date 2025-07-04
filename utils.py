import requests
import os

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1390607631097532436/We8AWWa25yeYlVmq-IGlCAQgPEontbksgwBvf-Otf8rXNpZ8Bkrxo4B9V5Xuvp9U8jnT"

def send_discord_alert(message):
    payload = {
        "content": f"🚨 Rare Item Alert 🚨\n{message}"
    }
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("✅ Alert sent to Discord")
        else:
            print(f"❌ Discord error: {response.status_code}")
    except Exception as e:
        print(f"❌ Discord Exception: {e}")
