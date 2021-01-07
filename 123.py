from keras.engine.saving import model_from_json
from bj_env import PokerAgent
from audioOutput import speak

import time
import RPi.GPIO as GPIO
import numpy as np
import json

env=PokerAgent()
with open('model_in_json.json','r') as f:
    model_json=json.load(f)
model=model_from_json(model_json)
model.load_weights('bj_model_500K.fdh5')

BUTTON_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

card_value=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def suggest(action):
    speech=''
    if action==0:
        speech='stand'
    elif action==1:
        speech='hit'
    else:
        speech='double'
    speak(speech)


print("start")
stage=0
while True:
    if GPIO.input(BUTTON_PIN)==GPIO.LOW and stage==0:
        print("new game")
        print("scan dealer's card")
        card_file=open('card.txt','r')
        cards=card_file.read().split()
        card_file.close()
        while not cards:
            card_file=open('card.txt','r')
            cards=card_file.read().split()
            card_file.close()
        env.reset()
        env.dealer.append(card_value[int(cards[0])])
        stage=1
        print(env.dealer,"\nscan player's card")
        time.sleep(0.25)
    elif stage==1:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            print("end game")
            stage=0
            time.sleep(0.5)
            continue
        env.player=[]
        card_file=open('card.txt','r')
        cards=card_file.read().split()
        card_file.close()
        while len(cards) < 2:
            card_file=open('card.txt','r')
            cards=card_file.read().split()
            card_file.close()
        for i in cards:
            env.player.append(card_value[int(i)])
        cur_state=env.get_obs()
        print(cur_state)
        action=np.argmax(model.predict(np.array(cur_state).reshape(-1,*np.array(cur_state).shape))[0])
        suggest(action)