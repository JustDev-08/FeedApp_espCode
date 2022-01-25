

# This file is executed on every boot (including wake-boot from deepsleep)

# import esp

# esp.osdebug(None)

import time
from machine import Pin, PWM
from  lib_mqtt import MQTTClient
import network
import gc

import os


# import webrepl

# webrepl.start()

gc.collect()


# Main


# สัมการ


# import iib
# ssid

ssid = "Netnapawan_2.4GHz"
sspass = "12102503"

# server
mqttserver = "broker.hivemq.com"

# password
mypass = "15463"
topica = "/feed/board/pass/" + mypass

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, sspass)

while not station.isconnected():
    print(".", end="")
    time.sleep(1)

print("Connected To " + ssid)

client = MQTTClient(mypass, mqttserver)

client.connect()
print("Connected with ", mypass)
# about servo and machine gear

servo1 = PWM(Pin(4), freq=50, duty=100)
servo2 = PWM(Pin(0), freq=50, duty=20)

def math_feed(ml) :
    return float(ml)

def use_servo(time_feed):
    
    servo2.duty(100)
    servo1.duty(50)
    for i in range(time_feed) :
        print(i)
        servo2.duty(120)
        time.sleep(0.5)
        servo2.duty(60)
        time.sleep(0.5)
    servo2.duty(20)
    servo1.duty(100)



def sub_suc(topic_in, mess):
    print('Send message To', topic_in)
    client.publish(topic_in + "/callback", 'Feeded')
    ml = mess.decode('utf-8').split('/')
    
    use_servo(math_feed(ml[1]))

    print('sucessfuly')


client.set_callback(sub_suc)
while True:
    client.subscribe(topica)
