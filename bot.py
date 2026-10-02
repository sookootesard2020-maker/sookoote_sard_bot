import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = "@sookoote_sard"
SLOT = os.environ.get("POST_SLOT", "night")

posts = {
    "morning": """🌅 صبح بخیر

قرار نیست هر روز همه‌چیز عالی باشد.
گاهی فقط کافیست ادامه بدهی و به خودت یادآوری کنی:
این روز هم می‌گذرد.

امروز را با امید شروع کن.
خدا هنوز حواسش به تو هست. 🤍

@ sookoote_sard""",

    "afternoon": """🌿

اگر امروز خسته‌ای،
اگر دلت گرفته،
اگر احساس می‌کنی دیگر توان ادامه دادن نداری...

چند لحظه آرام بگیر.
نفس عمیق بکش.
همه‌چیز قرار نیست همین امروز حل شود.

خدا را به دل بسپار...
گاهی آرامش درست از جایی می‌آید
که انتظارش را نداری. 🤍

@ sookoote_sard""",

    "night": """🌙

گاهی باید چند لحظه سکوت کنی،
نفس عمیق بکشی
و همه نگرانی‌هایت را به خدا بسپاری.

قرار نیست همه‌چیز همین امشب درست شود.

خدا هنوز هست؛
و همین یعنی هنوز امید هست. ❤️

شبت آرام،
دلت گرم به حضور خدا.

@ sookoote_sard"""
}

message = posts.get(SLOT, posts["night"])

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHANNEL,
        "text": message.replace("@ sookoote_sard", "@sookoote_sard")
    },
    timeout=30
)

print(response.text)
