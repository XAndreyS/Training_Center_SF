import telebot
from config import keys, TOKEN
from utils import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start (message: telebot.types.Message):
    text = 'Вас приветствует Бот-Конвертер Валют!\nЧтобы начать работу введите команду в следующем формате:\n<название валюты> <в какую валюту перевести> <количество>' \
           '\n- Показать список доступных валют /values\n- напомнить о работе бота /help'
    bot.reply_to(message, text)

@bot.message_handler(commands=['help'])
def help (message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты>\
    <в какую валюту перевести>\
    <количество перевадимой валюты>\nНапрмер:\nдоллар рубль 2\nУвидеть список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.lower().split(' ')
        if len(values) != 3:
            raise ConvertionException('Введите команду или 3 параметра!\nДля помощи воспользуйтесь командой /help')  #
        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()

