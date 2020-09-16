import logging
import ephem
from datetime import date
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from lesson2.cities import cities_list
import lesson2.settings as settings
import random

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
user_data = {}


def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def wordcount(bot, update):
    user_text = update.message.text
    clear = []
    for i in user_text.split(' '):
        elem = ''.join(filter(str.isalpha, i))
        if elem != '':
            clear.append(elem)
    del clear[0]
    if len(clear) > 0:
        update.message.reply_text(f'{len(clear)} слова')
    else:
        update.message.reply_text('В строке нет слов')


def planet(bot, update):
    user_text = update.message.text
    if user_text.split()[1] == 'Mercury':
        update.message.reply_text(ephem.constellation(ephem.Mercury(date.today())))
    elif user_text.split()[1] == 'Venus':
        update.message.reply_text(ephem.constellation(ephem.Venus(date.today())))
    elif user_text.split()[1] == 'Mars':
        update.message.reply_text(ephem.constellation(ephem.Mars(date.today())))
    elif user_text.split()[1] == 'Jupiter':
        update.message.reply_text(ephem.constellation(ephem.Jupiter(date.today())))
    elif user_text.split()[1] == 'Saturn':
        update.message.reply_text(ephem.constellation(ephem.Saturn(date.today())))
    elif user_text.split()[1] == 'Uranus':
        update.message.reply_text(ephem.constellation(ephem.Uranus(date.today())))
    elif user_text.split()[1] == 'Neptune':
        update.message.reply_text(ephem.constellation(ephem.Neptune(date.today())))
    elif user_text.split()[1] == 'Pluto':
        update.message.reply_text(ephem.constellation(ephem.Pluto(date.today())))
    else:
        update.message.reply_text('Не знаю такую планету')


def fullmoon(bot, update):
    update.message.reply_text(ephem.next_full_moon(date.today()))


def cities(bot, update):
    user = update.message.from_user.username
    city = update.message.text[8:].lower()
    last_letter = city[-1]
    if city not in cities_list:
        update.message.reply_text('Я не знаю такой город')
    else:
        if last_letter in 'ыъйь':
            last_letter = city[-2]
        if user not in user_data or len(user_data[user]) == 0:
            user_data[user] = []
            user_data[user].append(city)
            bot_city = random.choice([i for i in cities_list if i.startswith(last_letter) and i not in user_data[user]])
            update.message.reply_text(bot_city)
            user_data[user].append(bot_city)
        else:

            if len(cities_list) == len(user_data[user]):
                update.message.reply_text('Известные мне города закончились. Обнуляем список городов.')
                user_data[user] = []
            elif len([i for i in cities_list if i.startswith(last_letter) and i not in user_data[user]]) == 1:
                random.choice([i for i in cities_list if i.startswith(last_letter) and i not in user_data[user]])
                update.message.reply_text('Использовано последнее слово на эту букву, которое я знаю. Начинаем сначала')
                user_data[user] = []
            else:
                start_letter = user_data[user][-1][-1]
                if start_letter in 'ыъйь':
                    start_letter = user_data[user][-1][-2]
                if start_letter != city[0]:
                    update.message.reply_text('Схитрить решил? Отвечай честно!')
                else:
                    if city in user_data[user]:
                        update.message.reply_text('Схитрить решил? Отвечай честно!')
                    else:

                        user_data[user].append(city)
                        bot_city = random.choice(
                            [i for i in cities_list if i.startswith(last_letter) and i not in user_data[user]])
                        update.message.reply_text(bot_city)
                        user_data[user].append(bot_city)


def calc(bot, update):
    try:
        user_text = str(update.message.text)[5:]
        user_text = user_text.replace(' ', '').replace(',', '.')
        print(user_text)
        if user_text.lower() == 'правила':
            update.message.reply_text(
                'Правила работы с калькулятором:\n пример записывается без пробелов с использованием'
                '\n + Суммирует значения слева и справа от оператора \n -Вычитает правый операнд из левого \n * Перемножает операнды \n / Делит левый операнд на правый \n ** возводит левый операнд в степень правого ')
        else:
            update.message.reply_text(
                f"Ответ: {eval(user_text)} \n для вывода правил работы с калькулятором напиши \n /cal правила")

    except:
        update.message.reply_text('бЛА БЛА БАЛА БАЛ БАЛ УЧИ ПРАИВЛА')


def main():
    mybot = Updater(settings.API_KEY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("fullmoon", fullmoon))
    dp.add_handler(CommandHandler("cities", cities))
    dp.add_handler(CommandHandler("cal", calc))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
