import telebot
import tools.config as config
import tools.shedule as shedule

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['monday'])
def send_monday(message):
    bot.send_message(message.chat.id, shedule.MONDAY)

@bot.message_handler(commands=['tuesday'])
def send_tuesday(message):
    bot.send_message(message.chat.id, shedule.TUESDAY)

@bot.message_handler(commands=['wednesday'])
def send_wednesday(message):
    bot.send_message(message.chat.id, shedule.WEDNESDAY)
    
@bot.message_handler(commands=['thursday'])
def send_thursday(message):
    bot.send_message(message.chat.id, shedule.THURSDAY)

@bot.message_handler(commands=['friday'])
def send_friday(message):
    bot.send_message(message.chat.id, shedule.FRIDAY)

if __name__ == '__main__':
     bot.polling(none_stop=True)