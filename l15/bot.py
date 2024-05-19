import telebot
from telebot import types
from datetime import date
import json
import io
import random

API_TOKEN = '6973472905:AAEL75ssZbRYcPmi_casdsadasWIRamTXGfMIsqabVw'

bot = telebot.TeleBot(API_TOKEN)


def is_day_name(day_name):
    days = ["понедельник", "среда", "четверг", "пятница", "вторник"]

    return day_name.lower() in days

def is_even_week():
    today = date.today()
    week_number = today.isocalendar()[1]
    return week_number % 2 == 0

def get_schedule(day_name, is_even):
    schedule = []

    with io.open("calendar.json", encoding='utf-8') as f:
        file_content = f.read()
        calendar = json.loads(file_content)

        schedule = calendar["even" if is_even else "odd"][day_name.lower()]

    return schedule

def get_format_schedule(day_name, is_even):
    schedule = get_schedule(day_name, is_even)

    formattedString = "📅 *{day_name}*\n\n".format(day_name=day_name.capitalize())

    for item in schedule:
        formattedString += "🕤 {item}\n".format(item=item)

    return formattedString


def get_curweek_schedule():
    days = ["понедельник", "среда", "четверг", "пятница", "вторник"]
    even = is_even_week()

    s = "Расписание на эту неделю\n\n"

    for day in days:
        s += get_format_schedule(day, even) + "\n"
    
    return s

def get_nextweek_schedule():
    days = ["понедельник", "среда", "четверг", "пятница", "вторник"]
    even = not is_even_week()

    s = "Расписание на следующую неделю\n\n"

    for day in days:
        s += get_format_schedule(day, even) + "\n"
    
    return s

week_keyboard = (
    types.ReplyKeyboardMarkup(resize_keyboard=True)
    .add(types.KeyboardButton("Понедельник"))
    .add(types.KeyboardButton("Вторник"))
    .add(types.KeyboardButton("Среда"))
    .add(types.KeyboardButton("Четверг"))
    .add(types.KeyboardButton("Пятница"))
    .add(types.KeyboardButton("Расписание на текущую неделю"))
    .add(types.KeyboardButton("Распиание на следующую неделю"))
)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Чем могу вам помочь? Используйте /help если у вас возникли вопросы", reply_markup=week_keyboard)


@bot.message_handler(commands=['help'])
def handle_help(message):
    help_message = """
🤖 Привет! Я бот для удобного просмотра расписания в институте.

Я создан в рамках курса по разработке пользовательского интерфейса студентом группы 4311-22 Петровым Андреем.
Вот что я могу:

/start - начать взаимодействие с ботом
/help - получить справку о боте и доступных командах
/week - узнать, четная ли текущая неделя
/kstu - получить ссылку на официальный сайт КНИТУ
/vk - получить ссылку на официальную группа вконтакте КНИТУ
/location - получить адреса всех учебных корпусов
    """

    bot.send_message(message.chat.id, help_message)


@bot.message_handler(commands=['location'])
def handle_location(message):
    locations = """
    Местонахождение учебных корпусов:

    Корпус «А» - г. Казань, ул. К. Маркса, 68
    Корпус «Б», «В», «О» - г. Казань, ул. К. Маркса, 72
    Корпус «Д», «Е», «Л», «М» - г. Казань, ул. Сибирский тракт, 12
    Корпус «К» - г. Казань, ул. Толстого, 8/31
    Корпус «Г» - г. Казань, ул. Попова, 10
    Корпус «И» - г. Казань, ул. Сибирский тракт, 41
    Корпус «Т» - г. Казань, ул. Толстого, 6 корпус 1
    """

    bot.send_message(message.chat.id, locations)


@bot.message_handler(commands=['vk'])
def handle_vk_group(message):
    bot.send_message(message.chat.id, "Группа Казанского национального технического университета (КазНИТУ) во ВКонтакте: https://vk.com/knitu")


@bot.message_handler(commands=['kstu'])
def kstu_handler(message):
    bot.send_message(message.chat.id, 'https://www.kstu.ru/')


@bot.message_handler(commands=['week'])
def handle_week(message):
    bot.send_message(message.chat.id, "Текущая неделя: {week_type}".format(week_type="нечетная" if is_even_week() else "четная"))


@bot.message_handler(func=lambda message: message.text.lower() == "куда идти")
def handle_wheretogo(message):
    bot.send_message(message.chat.id, "Для получения адресов корпусов воспользуйтесь командной /location")


@bot.message_handler(func=lambda message: message.text.lower() == "когда стипендия")
def handle_scholarship(message):
    bot.send_message(message.chat.id, "Стипендия приходит в 20-х числях месяца")


@bot.message_handler(func=lambda message: message.text.lower() == "придумай оправдание")
def handle_scholarship(message):
    l = [
        "Я не пришел, потому что у меня внезапно возникли проблемы с транспортом, и я не смог добраться до университета вовремя.",
        "Я не пришел, потому что сегодня у меня важное семейное событие, в котором участвуют все члены моей семьи.",
        "Я не пришел, потому что у меня непредвиденная ситуация с здоровьем, и мне потребовался неотложный визит к врачу.",
        "Я не пришел, потому что мне нужно было помочь другу/подруге в сложной ситуации, и я не мог его/её бросить.",
        "Я не пришел, потому что у меня сегодня важное интервью/мероприятие, которое невозможно было перенести, и я был вынужден пропустить занятие."
    ]

    bot.send_message(message.chat.id, "Если вам не хочется идти на пару вы можете сказать следующее\n\n🗣: " + random.choice(l))


@bot.message_handler(func=lambda message: True)
def handle_day(message):
    text = message.text.lower()

    if is_day_name(text):
        schedule = get_format_schedule(text, is_even_week())
        bot.send_message(message.chat.id, schedule)

    elif text == "расписание на текущую неделю":
        schedule = get_curweek_schedule()
        bot.send_message(message.chat.id, schedule)

    elif text == "распиание на следующую неделю":
        schedule = get_curweek_schedule()
        bot.send_message(message.chat.id, schedule)

    else:
        bot.send_message(message.chat.id, "Извините, я вас не понял")




bot.infinity_polling()
