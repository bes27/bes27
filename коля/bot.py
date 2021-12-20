import telebot
from telebot import types

bot = telebot.TeleBot('5030946634:AAEAU1_Q0_9VWW7k_2TIH2FQtNBX3woNrvo');


@bot.message_handler(commands = ['get_info', 'info'])
def get_user_info(message):
	markup_inline = types.InlineKeyboardMarkup()
	item_yes = types.InlineKeyboardButton(text ='Да', callback_data = 'yes')
	item_no = types.InlineKeyboardButton(text ='Нет', callback_data = 'no')

	markup_inline.add(item_yes, item_no)
	bot.send_message(message.chat.id, 'инфу о себе будешь?(потом в чате нажми id or name)',
		reply_markup = markup_inline
	)

@bot.callback_query_handler(func= lambda call: True)
def answer(call):
	if call.data == 'yes':
		markup_replay = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item_id = types.KeyboardButton('My ID')
		item_name = types.KeyboardButton('My Name')

		markup_replay.add(item_id, item_name)
		bot.send_message(call.message.chat.id,'choose',
			reply_markup = markup_replay
			)

	elif call.data == 'no':
		pass

@bot.message_handler(content_types =['text'])
def text_info(message):
	if message.text ==  'My ID':
		bot.send_message(message.chat.id, f'Ur ID: {message.from_user.id}')
	elif message.text == 'My Name':
		bot.send_message(message.chat.id, f'Ur Name: {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(content_types = ['text'])
def get_help(message):
	if message.text == 'Привет':
		bot.send_message(message.chat.id, 'Привет (список команд /help)')
	elif message.text == '/help':
		bot.send_message(message.chat.id, '/info')
		bot.register_next_step_handler(message, get_user_info);
	else:
		bot.send_message(message.chat.id, 'Не понимаю о чем ты(/help)')
	


bot.polling(none_stop = True, interval = 0)