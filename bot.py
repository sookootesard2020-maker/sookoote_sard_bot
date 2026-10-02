import os
import re
import requests
from datetime import date

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = "@sookoote_sard"
POST_HOUR = int(os.environ.get("POST_HOUR", "23"))

# تاریخ شروع چرخه 1000 روزه
START_DATE = date(2026, 10, 2)

# مشخص کردن نوبت
slots = {
    8: "صبح",
    12: "ظهر",
    17: "عصر",
    20: "غروب",
    23: "شب"
}

slot_name = slots.get(POST_HOUR, "شب")

# شماره روز از شروع برنامه
today = date.today()
day_number = (today - START_DATE).days + 1

# نگه داشتن شماره روز در محدوده 1 تا 1000
day_number = ((day_number - 1) % 1000) + 1

# خواندن بانک 5000 متن
with open("sokoot_sard_1000_days.txt", "r", encoding="utf-8") as f:
    content = f.read()

# پیدا کردن متن مربوط به روز و نوبت
pattern = (
    rf"===== روز {day_number} \| {re.escape(slot_name)} =====\n"
    rf"(.*?)(?=\n===== روز |\Z)"
)

match = re.search(pattern, content, re.DOTALL)

if not match:
    raise Exception(
        f"متن روز {day_number} و نوبت {slot_name} پیدا نشد."
    )

message = match.group(1).strip()

# ارسال به تلگرام
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHANNEL,
        "text": message
    },
    timeout=30
)

print(response.text)

if not response.ok:
    raise Exception("ارسال پیام به تلگرام ناموفق بود.")
