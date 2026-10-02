import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = os.environ.get("CHANNEL_USERNAME", "@sookoote_sard")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

message = """🌙
گاهی فقط باید چند لحظه سکوت کنی...

نفس عمیق بکش.
همه‌چیز قرار نیست همین امروز درست شود.
خدا هنوز هست؛
و همین یعنی هنوز امید هست. 🤍

— سکوت سرد"""

response = requests.post(
    url,
    data={
        "chat_id": CHANNEL,
        "text": message
    },
    timeout=30
)

print(response.text)
