import time
import telepot
from telepot.namedtuple import InlineKeyboardButton, InlineKeyboardMarkup


TOKEN = '1336543686:AAHOpcZBbwmOOLA5zG_HgIW-fjRKWTyUQj8'
bot = telepot.Bot(TOKEN)

def handle_start(msg):
    chat_id = msg['chat']['id']
    bot.sendMessage(chat_id, "Hello, please send Google Play Store link to download APK file.")

def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        if msg['text'] == '/start':
            handle_start(msg)

        elif 'https://play.google.com/store/apps/details?id=' in msg['text']:
            package_name = msg['text'].split('id=')[1].split('&')[0]
            apkpure =f'https://d.apkpure.com/b/APK/{package_name}?version=latest'
            time.sleep(1)
            hazirlaniyor = bot.sendMessage(chat_id, "Preparing download link...")
            for i in range(4):

                bot.editMessageText((chat_id, hazirlaniyor['message_id']), f"\u23F1 Preparing download link{'.' * i}")
                time.sleep(0.2)
            time.sleep(2)
            bot.editMessageText((chat_id, hazirlaniyor['message_id']), "\U0001F973 Download link is ready!")
            bot.sendChatAction(chat_id,'upload_document')
            time.sleep(3)
            bot.deleteMessage((chat_id, hazirlaniyor['message_id']))
            button_text = '⬇️ Download ⬇️'
            button_url = apkpure
            button = InlineKeyboardButton(text=button_text, url=button_url)

            # Butonları bir araya getirerek bir klavye oluşturun
            keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])

            # Mesajınızı gönderirken butonlu klavyeyi de ekleyin
            bot.sendMessage(chat_id, text='When you go to the link in the button, the APK file will automatically start downloading.', reply_markup=keyboard)


        else:
            bot.sendMessage(chat_id, "Please send Google Play Store link.")

bot.message_loop(handle_message)

while True:
    pass
