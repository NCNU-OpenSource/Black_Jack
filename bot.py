import os
import time
import json
import telepot
import numpy as np
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# import main
import audioOutput
from bj_env import PokerAgent
from keras.engine.saving import model_from_json

# Welcome users


def hello(update, context):
    update.message.reply_text(f'hello, {update.message.from_user.first_name}')


# New Game
def start(update, context):
    start_new_round('start')
    update.message.reply_text('New Round!\n\nShow me the dealer\'s card.')


# My turn
def mine(update, context):
    print('new')
    start_new_round('mine')
    update.message.reply_text('Scaning your cards plz.')


# Speak what you want


def speak(update, context):
    audioOutput.speak(
        f'{update.message.from_user.first_name} 說: {update.message.text[6:]}')


# Show Commands
def help(update, context):
    update.message.reply_text(
        'Blackjack的指令集~~~\n /help 指令集\n /start 開始新的一輪')

    # update.message.reply_text(
    #     'Blackjack的指令集~~~\n /help 指令集\n /dealer 莊家的牌\n /me 玩家的牌')


# Repeat what user say
def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(
        f'{update.message.from_user.first_name} 說: {update.message.text[5:]}')


# Bluetooth setting
def bluetooth():
    pass


# Add commend
def add_command(name, function):
    global command
    command.append({'name': name, 'function': function})


def start_new_round(method):
    ambiguous()
    global env
    card_file = open('card.txt', 'r')
    cards = card_file.read().split()
    card_file.close()
    if method == 'start':
        while not cards[0]:
            card_file = open('card.txt', 'r')
            cards = card_file.read().split()
            card_file.close()
        env.reset()
        env.dealer.append(card_value[int(cards[0])])
    if method == 'mine':
        while len(cards) < 2:
            card_file = open('card.txt', 'r')
            cards = card_file.read().split()
            card_file.close()
        for i in cards:
            env.player.append(card_value[int(i)])
        cur_state = env.get_obs()
        action = np.argmax(model.predict(
            np.array(cur_state).reshape(-1, *np.array(cur_state).shape))[0])
        suggest(action)


# Change suggestion to the speech
def suggest(action):
    speech = ''
    if action == 0:
        speech = 'stand'
    elif action == 1:
        speech = 'hit'
    else:
        speech = 'double'
    speak(speech)


status = 1
command = []
card_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Load the reinforcement learning
env = PokerAgent()

with open('model_in_json.json', 'r') as f:
    model_json = json.load(f)
model = model_from_json(model_json)
model.load_weights('bj_model_500K.fdh5')


def main():

    myFile = open('token.txt')
    token = myFile.read().strip()
    updater = Updater(token, use_context=True)
    bot = telepot.Bot(token)
    # dispatcher = updater.dispatcher
    # dispatcher.add_handler(CommandHandler("start", start))
    # updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

    add_command('hello', hello)
    add_command('new', start)
    add_command('me', mine)
    add_command('help', help)
    add_command('echo', echo)
    add_command('speak', speak)

    for i in command:
        updater.dispatcher.add_handler(
            CommandHandler(i['name'], i['function']))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
    # mine()
