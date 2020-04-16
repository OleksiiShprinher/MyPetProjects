import telebot
import pyowm

owm = pyowm.OWM('670a355f137b53cd44c861a633ecfaa2')

bot = telebot.TeleBot("1193399427:AAGtR_BlibKtIeUBYcnyuIVJU4RotXvRFrA")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	place_to_check = message.text

	try:
		observation = owm.weather_at_place(place_to_check)
	except BaseException:
		answer = "I don`t know this place!"
		bot.send_message(message.chat.id, answer)
	else:		
		w = observation.get_weather()

		answer = 'In ' + place_to_check + ' now is ' + w.get_detailed_status() + "\n"
		answer += 'The temperature is ' + str(w.get_temperature('celsius')['temp']) + ' there'"\n\n"

		bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True)