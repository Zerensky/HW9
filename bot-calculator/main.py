from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

TOKEN = 'TOKEN'
updater = Updater(token="тут мой токен")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', mat_operations_command))
updater.dispatcher.add_handler(CommandHandler('mult', mat_operations_command ))
updater.dispatcher.add_handler(CommandHandler('divis', mat_operations_command ))
updater.dispatcher.add_handler(CommandHandler('sub', mat_operations_command ))

print('server start')
updater.start_polling()
updater.idle()
