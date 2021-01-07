import time
import RPi.GPIO as GPIO
 
BUTTON_PIN = 18
 
def my_callback(channel):
    print('按下按鈕')

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 
try:
    print('按下 Ctrl-C 可停止程式')
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            my_callback(BUTTON_PIN)
        time.sleep(0.25)
except KeyboardInterrupt:
    print('關閉程式')
finally:
    GPIO.cleanup()