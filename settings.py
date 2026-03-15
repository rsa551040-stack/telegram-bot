import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
MODERATION_ENABLED = os.getenv("MODERATION_ENABLED", "true").lower() == "true"
BLOCK_LINKS = os.getenv("BLOCK_LINKS", "true").lower() == "true"
BLOCK_PHONE_NUMBERS = os.getenv("BLOCK_PHONE_NUMBERS", "true").lower() == "true"
SEND_ALERT_MESSAGES = os.getenv("SEND_ALERT_MESSAGES", "true").lower() == "true"
ALERT_MESSAGE_AUTO_DELETE_SECONDS = int(os.getenv("ALERT_MESSAGE_AUTO_DELETE_SECONDS", "8"))
ABUSE_BAN_THRESHOLD = int(os.getenv("ABUSE_BAN_THRESHOLD", "0"))

# أنماط تعتبر وسيلة تواصل/رابط ويؤدي وجودها إلى حذف الرسالة وحظر المرسل.
USERNAME_LINK_PATTERNS = [
    "http://",
    "https://",
    "www.",
    "t.me/",
    "telegram.me/",
    "wa.me/",
    "chat.whatsapp.com/",
    "bit.ly/",
    "tinyurl.com/",
    "goo.gl/",
]

# عبارات إعلانية طلبتَ حظرها.
BANNED_AD_PHRASES = [
    "♨️حل واجبات او بحوث او عروض ومشاريع وحتى حلول الكويزات والاختبارات",
    "حل واجبات او بحوث او عروض ومشاريع وحتى حلول الكويزات والاختبارات",
    "حل واجبات",
    "حل بحوث",
    "حلولهم ثقة ومضمونة ولديهم تجارب العديد من الطلاب والطالبات",
    "للتواصل واتساب",
    "تعال خاص",
    "للتواصل",
    "خصم",
    "خدمات طلابية",
    "سكليف",
    "مساعدة",
    "خش خاص",
    "خاص",
]

# أضف هنا الكلمات المسيئة التي تريد حذفها. افتراضيًا القائمة فارغة لتجنب الحظر الخاطئ.
CUSTOM_BANNED_ABUSE_TERMS = [
    # مثال: "كلمة مسيئة",
]


def _normalized_unique(items: list[str]) -> list[str]:
    seen = set()
    cleaned = []
    for item in items:
        value = " ".join(item.split()).strip().lower()
        if value and value not in seen:
            cleaned.append(value)
            seen.add(value)
    return cleaned



def build_banned_ad_phrases() -> list[str]:
    return _normalized_unique(BANNED_AD_PHRASES)



def build_banned_abuse_terms() -> list[str]:
    return _normalized_unique(CUSTOM_BANNED_ABUSE_TERMS)
