import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = "@sookoote_sard"

posts = {
    "morning": """🌅 صبح بخیر

امروز قرار نیست همه‌چیز را یک‌دفعه درست کنی.
فقط یک قدم بردار...
همین یک قدم می‌تواند شروع یک اتفاق خوب باشد.

به خدا توکل کن؛
شاید امروز همان روزی باشد که منتظرش بودی. 🤍

@sookoote_sard""",

    "noon": """☀️

وسط شلوغی‌های روز،
گاهی چند لحظه مکث کن...

نفس عمیق بکش،
دلت را آرام کن
و یادت باشد:
همه چیز قرار نیست با عجله حل شود.

خدا آرام‌تر از چیزی که فکر می‌کنی
جوابت را می‌دهد. 🌿

@sookoote_sard""",

    "afternoon": """🌿

اگر امروز خسته‌ای،
اگر چیزی ذهنت را درگیر کرده،
خودت را سرزنش نکن.

تو تا همین‌جا هم خیلی چیزها را پشت سر گذاشتی.

کمی آرام بگیر...
خدا هنوز کنار توست. 🤍

@sookoote_sard""",

    "evening": """🌆

گاهی یک غروب آرام،
یک موسیقی خوب
و چند دقیقه سکوت
می‌تواند حال آدم را عوض کند.

امروز هرچقدر هم سخت گذشته،
بگذار تمام شود.

فردا می‌تواند شروع تازه‌ای باشد. ❤️

@sookoote_sard""",

    "night": """🌙

قبل از خواب
همه نگرانی‌هایت را برای چند دقیقه کنار بگذار.

چشم‌هایت را ببند و بگو:

خدایا...
آنچه از توان من خارج است
به تو می‌سپارم.

دلم را آرام کن
و فردایم را بهتر از امروزم قرار بده. 🤍

شبت آرام.

@sookoote_sard"""
}

# انتخاب متن بر اساس زمان اجرای GitHub Actions
hour = int(os.environ.get("POST_HOUR", "23"))

if hour == 8:
    message = posts["morning"]
elif hour == 12:
    message = posts["noon"]
elif hour == 17:
    message = posts["afternoon"]
elif hour == 20:
    message = posts["evening"]
else:
    message = posts["night"]

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
