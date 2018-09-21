from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from send import create_connection_thread
import modes
import config
import logging
'''
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                    '''

def callbackHandler(bot, update):
    query = update.callback_query
    if query.data == 'light':
        sock.send_mes('light')
    elif query.data == 'aircon':
        modes.aircon_mode(query)
    elif query.data == 'menu':
        modes.menu(query)
    elif query.data == 'air_temp':
        modes.temp_mode(query)
    elif query.data == 'wind_dir':
        sock.send_mes('wind_dir')
    elif query.data == 'wind_str':
        modes.wind_str_mode(query)
    elif query.data[:5] == 'temp_':
        sock.send_mes(query.data)
    elif query.data[:9] == 'wind_str_':
        sock.send_mes(query.data)


if __name__ == "__main__":

    updater = Updater(token=config.token)
    dispatcher = updater.dispatcher
    command_list = ['start', 'menu']

    for c in command_list:
        handler = CommandHandler(c, getattr(modes, c))
        dispatcher.add_handler(handler)
    dispatcher.add_handler(CallbackQueryHandler(callbackHandler))
    
    sock = create_connection_thread()
    sock.start()

    updater.start_polling()
    print("[+] Bot server started")
