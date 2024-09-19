import telebot
from telebot import types
from g4f.client import Client
token='7055961728:AAG2lleK7CgR29Y5gdjB0Tqtk8Nlhw49yV0'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id,'Привет, я бот созданный с использованием доработанной модели gpt, от Paranormal Games, отправьте мне любой интересующий вас вопрос')
@bot.message_handler(commands=["geo"])
def geo(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
    keyboard.add(button_geo)
    bot.send_message(
        message.chat.id, "Нажмите на кнопку, чтобы передать свое местоположение боту.",
        reply_markup=keyboard)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
	zapros=message.text
	client = Client()
	response = client.chat.completions.create(
	model="gpt-4",
	messages=[{"role": "user", "content": zapros}]
	)
	otvet = response.choices[0].message.content
	print(otvet)
	if 'Привет' in otvet:
		otvet = 'Привет'
	if 'Open' in otvet:
		otvet = 'я бот созданный с использованием доработанной модели gpt, от Paranormal Games, отправьте мне любой интересующий вас вопрос'
	#if 'Не могу' or 'Прошу' or 'Remember' in otvet:
		#otvet = 'Базар фильтру'
	print(otvet)
	bot.reply_to(message, otvet)
bot.polling(none_stop = True)
