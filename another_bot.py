import telebot
import requests
import lxml.html
from lxml import etree
from bs4 import BeautifulSoup

TOKEN = "5729962240:AAFTb3-VWfZQfm58UMx9S-WH09fVcE7zZmk"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_star(message):
    bot.send_message(message.chat.id, f"Приветствую, {message.chat.username}, этот бот достает самый свежий вопрос "
                                      f"с сайта stackoverflow. Пока доступна только две команды /questions"
                                      f"и /py_questions.")


user_qs = {}
user_py_qs = {}


@bot.message_handler(commands=["py_questions"])
def py_questions(massage):
    bot.send_message(massage.chat.id, "https://ru.stackoverflow.com/questions/tagged/python")
    # base = "https://ru.stackoverflow.com/questions/tagged/python"
    # html = requests.get(base).content
    # soup = BeautifulSoup(html, "lxml")
    # div = soup.find("div", id="questions")

    # a = div.find_all('a', class_='s-link')                                     # здесь нужно доработать
    # for _ in a[:2]:                                                            # не может найти страницу при парсинге
    #     txt = base + _.get('href')                                             # поэтому пока просто ссылка
    #     if massage.chat.username not in user_py_qs:
    #         bot.send_message(massage.chat.id, txt)
    #         user_py_qs[massage.chat.username] = txt
    #     else:
    #         if user_py_qs[massage.chat.username] == txt:
    #             bot.send_message(massage.chat.id, "Вы уже видели эту сатью")
    #         else:
    #             bot.send_message(massage.chat.id, txt)
    #             user_py_qs[massage.chat.username] = txt


@bot.message_handler(commands=['questions'])
def handle_quest(massage):
    base = "https://ru.stackoverflow.com"
    html = requests.get(base).content
    soup = BeautifulSoup(html, "lxml")
    div = soup.find("div", id="question-mini-list")

    a = div.find_all('a', class_='s-link')
    for _ in a[:1]:
        txt = base + _.get('href')
        if massage.chat.username not in user_qs:
            bot.send_message(massage.chat.id, txt)
            user_qs[massage.chat.username] = txt
        else:
            if user_qs[massage.chat.username] == txt:
                bot.send_message(massage.chat.id, "Вы уже видели эту сатью")
            else:
                bot.send_message(massage.chat.id, txt)
                user_qs[massage.chat.username] = txt


bot.polling(none_stop=True)