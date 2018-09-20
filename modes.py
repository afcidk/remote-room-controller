from telegram import InlineKeyboardButton, InlineKeyboardMarkup 

def genMarkup(data):
    keyboard = []
    for k,v in data.items():
        keyboard.append([InlineKeyboardButton(k, callback_data=v)])
    print(keyboard)
    return InlineKeyboardMarkup(keyboard)

def aircon_mode(query):
    data = {'溫度': 'air_temp', '自動風向': 'wind_dir', '風量': 'wind_str', '返回': 'menu'}
    query.edit_message_reply_markup(reply_markup=genMarkup(data))

def temp_mode(query):
    data = {k:'temp_'+str(k) for k in range(23,27)}
    data.update({'返回': 'aircon'})
    query.edit_message_reply_markup(reply_markup=genMarkup(data))

def wind_str_mode(query):
    tl = ['靜', '弱', '中', '強']
    data = {tl[i]:'wind_str_'+str(i) for i in range(len(tl))}
    data.update({'返回': 'aircon'})
    query.edit_message_reply_markup(reply_markup=genMarkup(data))

def start(bot, update):
    data = {'電燈':'light', '冷氣':'aircon'}
    bot.send_message(chat_id=update.message.chat_id, text='Welcome!', reply_markup=genMarkup(data))

def menu(query):
    data = {'電燈':'light', '冷氣':'aircon'}
    query.edit_message_reply_markup(reply_markup=genMarkup(data))

