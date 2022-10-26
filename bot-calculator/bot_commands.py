from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler

import datetime
from spy import *


def start(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(\
        f'Что бы провести математическую'
        f'\n операцию, введите:\n/sum X Y для X + Y '
        f'\n/mult X Y для X * Y \n/divis X Y для X / Y  '
        f'\n/sub X Y для X - Y \n/help для вызова справки')


def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(\
        f'Что бы провести математическую'
        f'\n операцию, введите:\n/sum X Y для X + Y '
        f'\n/mult X Y для X * Y \n/divis X Y для X / Y  '
        f'\n/sub X Y для X - Y')


def mat_operations_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    fun = items[0]
    if fun == '/sum':
        x = int(items[1])
        y = int(items[2])
        update.message.reply_text(f'{x} + {y} = {x + y}')
    elif fun == '/mult':
        x = float(items[1])
        y = float(items[2])
        update.message.reply_text(f'{x} * {y} = {x * y}')
    elif fun == '/divis':
        x = float(items[1])
        y = float(items[2])
        update.message.reply_text(f'{x} / {y} = {x / y}')
    elif fun == '/sub':
        x = float(items[1])
        y = float(items[2])
        update.message.reply_text(f'{x} - {y} = {x - y}')

    print(msg)
