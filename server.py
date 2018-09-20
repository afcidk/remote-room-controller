from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup 
from send import send_mes
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def genMarkup(data):
    keyboard = []
    for k,v in data.items():
        keyboard.append([InlineKeyboardButton(k, callback_data=v)])
    print(keyboard)
    return InlineKeyboardMarkup(keyboard)

def aircon_mode(query, chat_data):
    data = {'溫度': 'air_temp', '自動風向': 'wind_dir', '風量': 'wind_str', '返回': 'menu'}
    query.edit_message_reply_markup(reply_markup=genMarkup(data))

def temp_mode(query, chat_data):
    data = {k:'temp_'+str(k) for k in range(23,27)}
    data.update({'返回': 'aircon'})
    query.edit_message_reply_markup(reply_markup=genMarkup(data))

def wind_str_mode(query, chat_data):
    tl = ['靜', '弱', '中', '強']
    data = {tl[i]:'wind_str_'+str(i) for i in range(len(tl))}
    data.update({'返回': 'aircon'})
    query.edit_message_reply_markup(reply_markup=genMarkup(data))

def start(bot, update):
    data = {'電燈':'light', '冷氣':'aircon'}
    bot.send_message(chat_id=update.message.chat_id, text='Welcome!', reply_markup=genMarkup(data))

def menu(query, chat_data):
    data = {'電燈':'light', '冷氣':'aircon'}
    query.edit_message_reply_markup(reply_markup=genMarkup(data))

def callbackHandler(bot, update, chat_data):
    query = update.callback_query
    if query.data == 'light':
        send_mes('light')
        pass
        # TODO: send signal to toggle light
    elif query.data == 'aircon':
        aircon_mode(query, chat_data)
    elif query.data == 'menu':
        menu(query, chat_data)
    elif query.data == 'air_temp':
        temp_mode(query, chat_data)
    elif query.data == 'wind_dir':
        send_mes('wind_dir')
        pass
        # TODO: send signal to toggle auto wind direction
    elif query.data == 'wind_str':
        wind_str_mode(query, chat_data)
    elif query.data[:5] == 'temp_':
        pass
        send_mes(query.data)
        # TODO: send signal to modify temperature
    elif query.data[:9] == 'wind_str_':
        pass
        send_mes(query.data)
        # TODO: send signal to modify wind strength


if __name__ == "__main__":

    updater = Updater(token='672339448:AAH1plTouL32azoeaAxsJsxAlXzbWoLVfTs')
    dispatcher = updater.dispatcher
    command_list = ['start', 'menu']

    for c in command_list:
        handler = CommandHandler(c, globals()[c])
        dispatcher.add_handler(handler)
    dispatcher.add_handler(CallbackQueryHandler(callbackHandler, pass_chat_data=True))

    print("hi")
    updater.start_polling()
