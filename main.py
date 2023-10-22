import requests
import telebot
from datetime import datetime


bot = telebot.TeleBot(token='', parse_mode = 'Markdown')

@bot.message_handler()
def main(message):
    data = requests.get('http://bard.notes:8888/test').text
    if data:
        bot.send_message(chat_id = message , text = f'Гороскоп на {datetime.now().strftime("%d %H:%M")}\n\n{data}')

if __name__ == '__main__':
    main(message='-1001692686575')