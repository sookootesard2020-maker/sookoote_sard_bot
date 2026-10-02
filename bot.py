import os
import requests

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = "@sookoote_sard"
SLOT = os.environ.get("POST_SLOT", "night")

posts = {
    "morning": """☀️
    صبح که شروع می‌شود،
    لازم نیست همه‌ی جواب‌ها را بدانی.

    فقط یک قدم بردار،
    یک نفس عمیق بکش
    و به خدا اعتماد کن.

    شاید امروز همان روزی باشد
    که منتظرش بودی. 🤍

    @ sookoote_sard""",

        "noon": """🌿
        اگر امروز دلت خسته است،
        کمی آرام‌تر زندگی کن...

        قرار نیست همیشه قوی باشی.
        گاهی فقط باید بنشینی،
        نفس بکشی
        و بگذاری خدا کمی از بار دلت را بردارد.

        تو تنها نیستی. 🤍

        @ sookoote_sard""",

            "afternoon": """🕊️
            بعضی اتفاق‌ها دیر می‌رسند،
            اما وقتی می‌رسند می‌فهمی
            خدا چرا تو را این‌همه منتظر گذاشته بود.

            صبور باش...
            هنوز پایان قصه‌ات نرسیده. 🌱

            @ sookoote_sard""",

                "evening": """🌅
                هرچقدر امروز سخت گذشت،
                دیگر تمام شد.

                اشتباه‌هایت را زمین بگذار،
                دلخوری‌ها را رها کن
                و امشب را با خیال خدا آرام کن.

                فردا دوباره شروع می‌شود. 🤍

                @ sookoote_sard""",

                    "night": """🌙
                    گاهی فقط باید چند لحظه سکوت کنی...

                    نفس عمیق بکش.
                    همه‌چیز قرار نیست همین امروز درست شود.

                    خدا هنوز هست؛
                    و همین یعنی هنوز امید هست. 🤍

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