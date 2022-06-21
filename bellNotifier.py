import time
import requests
import RPi.GPIO as GPIO

TOKEN = "TOKEN"
CHAT_ID = "CHATID"
SEND_URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

#RELAY READ PIN     15
#POWER PIN 3.3V     17
PIN = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.IN)
GPIO.setup(PIN, GPIO.LOW)

print("Running....")

while True:
    try:
        #state high = 1  low = 0
        state = GPIO.input(PIN)
        if state:
            requests.post(SEND_URL, json={'chat_id': CHAT_ID, 'text': "Door bell!!!"})
            # "ringing time" (so that the message comes only once)
            time.sleep(2)
        # So raspberry can do other things than monitor one pin :-)
        time.sleep(0.2)
    except KeyboardInterrupt:
        print('\nProgram interrupted')
        GPIO.cleanup()
        exit()
    except:
        print('Other error or exception occured!')
        GPIO.cleanup()
