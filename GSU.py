import telebot

from telebot import types

bot = telebot.TeleBot( '2006519011:AAGckftjRzgvIxdTA0nWwvWsEynR7BqKEeE', parse_mode=None )

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Привет, выбери неделю для которой нужно расписание: ",reply_markup = markup )

#keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton( 'Верхняя' )
button2 = types.KeyboardButton( "Нижняя" )

markup.add(button1, button2)

@bot.message_handler(content_types=['text'])
def Days(message):
    if message.chat.type == 'private':
        if message.text == 'Верхняя':
            bot.send_message(message.chat.id, "Выбери день недели: ",reply_markup = make)
        elif message.text == 'Понедельник':
            bot.send_message(message.chat.id, 'Прога(2 подгруппа) (3-11)\nДискретка (3-16)\nАГиЛА(лк) (3-11)\nИн.яз (3-11)\nПрога(1 подгруппа) (3-11)', reply_markup = markup)
        elif message.text == 'Вторник':
            bot.send_message(message.chat.id, 'Механика(пр) (3-11)\nМат.анализ(лк) (3-11)\nМат.анализ(пр) (3-11)\nПрога(2 подгруппа) (3-11)', reply_markup = markup)
        elif message.text == 'Среда':
            bot.send_message(message.chat.id, 'Прога(лк) (3-11)\nМеханика(лк) (3-16)\nАГиЛА (3-11)', reply_markup = markup)
        elif message.text == 'Четверг':
            bot.send_message(message.chat.id, 'Физ-ра\nМат.анализ(пр) (3-11)\nМат.анализ(пр) (3-11)', reply_markup = markup)
        elif message.text == 'Пятница':
            bot.send_message(message.chat.id, 'Ин.яз (3-11)\nДискретка (3-11)\nПрога(1 подгруппа) (3-11)', reply_markup = markup)
        elif message.text == 'Суббота':
            bot.send_message(message.chat.id, 'Физ-ра\nИстория Беларуси (2-25)', reply_markup = markup)
        elif message.text == 'Нижняя':
            bot.send_message(message.chat.id, 'Выбери день',reply_markup = keyday)
        elif message.text == 'Понeдельниk':
            bot.send_message(message.chat.id, 'Прога(2 подгруппа) (3-11)\nДискретка (3-16)\nАГиЛА(лк) (3-11)\nИн.яз (3-11)\nПрога(1 подгруппа) (3-11)', reply_markup = markup)
        elif message.text == 'Bтopник':
                bot.send_message(message.chat.id, 'Механика(пр) (3-11)\nМат.анализ(лк) (3-11)\nМеханика(лк) (3-16)\nПрога(2 подгруппа) (3-11)', reply_markup = markup)
        elif message.text == 'Cpeда':
                bot.send_message(message.chat.id, 'Прога(лк) (3-11)\nМеханика(лк) (3-16)\nАГиЛА (3-11)\nИстория Беларуси', reply_markup = markup)
        elif message.text == 'Чeтвepг':
                bot.send_message(message.chat.id, 'Физ-ра\nМат.анализ(пр) (3-11)\nМеханика(лаб.) (5-19)', reply_markup = markup)
        elif message.text == 'Пятницa':
                bot.send_message(message.chat.id, 'Ин.яз (3-11)\nДискретка (3-11)\nПрога(1 подгруппа) (3-11)', reply_markup = markup)
        elif message.text == 'Cyббoтa':
                bot.send_message(message.chat.id, 'Физ-ра', reply_markup = markup)
        else:
            bot.send_message(message.chat.id, ' Данные введены неверно - учись читать =) ')


make = types.ReplyKeyboardMarkup(resize_keyboard=True)
button3 = types.KeyboardButton( 'Понедельник' )
button4 = types.KeyboardButton( 'Вторник' )
button5 = types.KeyboardButton( 'Среда' )
button6 = types.KeyboardButton( 'Четверг' )
button7 = types.KeyboardButton( 'Пятница' )
button8 = types.KeyboardButton( 'Суббота' )

make.add(button3, button4, button5, button6, button7, button8)
    
#Здесь исппользованы символы русского и анйглийского алфавита, т.к. я не придумал еще другого способа

keyday = types.ReplyKeyboardMarkup(resize_keyboard=True)
button9 = types.KeyboardButton( 'Понeдельниk')
button10 = types.KeyboardButton( 'Bтopник' )
button11 = types.KeyboardButton( 'Cpeда' )
button12 = types.KeyboardButton( 'Чeтвepг' )
button13 = types.KeyboardButton( 'Пятницa' )
button14 = types.KeyboardButton( 'Cyббoтa' )


keyday.add(button9, button10, button11, button12, button13, button14)









bot.polling(none_stop=True)