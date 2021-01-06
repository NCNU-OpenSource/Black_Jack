# import telepot
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


# Welcome users
def hello(update, context):
    update.message.reply_text(f'hello, {update.message.from_user.first_name}')


# New Game
def start(update, context):
    update.message.reply_text('New Round!')
    os.system('python3 audioOutput.py')


# Commands
def help(update, context):
    update.message.reply_text(
        'Blackjack的指令集~~~\n /help 指令集\n /dealer 莊家的牌\n /me 玩家的牌')


# Repeat what user say
def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(
        f'{update.message.from_user.first_name} 說: {update.message.text}')


# Bluetooth setting
def bluetooth():
    pass


# Add commend
def add_command(name, function):
    global command
    command.append({'name': name, 'function': function})


command = []


def main():

    # 執行這個程式，注意 'YOUR TOKEN HERE' 的地方請填入前面得到的 Token
    myFile = open('token.txt')
    token = myFile.read().strip()
    updater = Updater(token, use_context=True)

    # bot = telepot.Bot(token)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    add_command('start', start)
    add_command('hello', hello)
    add_command('help', help)
    add_command('echo', echo)

    for i in command:
        updater.dispatcher.add_handler(
            CommandHandler(i['name'], i['function']))

    # updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
