from transliterate import to_latin,to_cyrillic
import  telebot
TOKEN='5713095119:AAHwXk8mODdTWyrLVYkU-u-LvR4tjeiINgI'
bot=telebot.TeleBot(TOKEN,parse_mode=None)
@bot.message_handler(commands=['start','help'])
def start_otvet(message):
    javob="Assalomu alaykum,Xush kelibsiz"
    javob+='\nMatn kiriting'
    bot.reply_to(message,javob)
@bot.message_handler(func=lambda message:True)
def ishchi_qsm(message):
    msg=message.text
    javob=lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message,javob(msg))
bot.polling()




# matn=input('Matn kiriting>>>')
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
#
#


