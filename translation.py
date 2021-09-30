class Translation(object):

    START_TEXT = """👋Salom,

 Bu Telegram URL manzilini yuklash boti!

 <b> Iltimos, menga to'g'ridan -to'g'ri yuklab olish URL manzilini yuboring, men Telegramga Fayl/Video sifatida yuklay olaman </b>

 /help batafsil ma'lumot uchun..

"""

    HELP_USER = """👋Salom, men URL yuklovchi botiman..
    
1️⃣. URL manzilini yuboring.
2️⃣. Eskiz yuboring.
3️⃣. Tugmani tanlang.
   SVideo - Faylni video shaklida screenshotlar bilan yuboradi
   DFile  - Faylni screenshotlar bilan yuboradi
   Video  - Faylni video shaklida yuboradi
   File  - Faylni yuboradi
"""

    FORMAT_SELECTION = """🛎️Formatni tanlang: <a href='{}'>fayl hajmi tahminiy bõlishi mumkin</a>
    
Xoxlasangiz eskiz yuboring.
/deletethumbnail eskizni õchirish uchun."""
    
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""


    UPGRADE_TEXT = "<b>👉 Create own Clone Bot.. </b>  \n\n<a href='https://github.com/prgofficial/URLuploader-With-Hotstar'>Click here, Fork and deploy!!</a>"
    
    DOWNLOAD_START = "📥Yuklab olish..."
    
    UPLOAD_START = "📤Yuborish.."
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "📥Yuklab olindi {} sekundda. \n\n📤Yuborildi {} sekundda."

    RCHD_TG_API_LIMIT = "📥Yuklab olindi {} sekundda.\n📁Fayl hajmi: {}\nKechirasiz. Fayl hajmi 2 GB dan yuqori bõlganligi uchun, faylni Telegramga yuklashning iloji yõq❌."

    SAVED_CUSTOM_THUMB_NAIL = "Custom thumbnail saved. This will be permanent.\n\nUse /deletethumbnail to clear it."

    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom thumbnail cleared succesfully."

    CUSTOM_CAPTION_UL_FILE = " "

    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    
    SHOW_THUMB = "🗑️Eskizni õchirish uchun /deletethumbnail buyrugidan foydalaning."
    
    NO_THUMB = "Eskiz topilmadi!!\n\nAvval rasm yuboring."    
