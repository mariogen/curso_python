import paho.mqtt.client as paho
import time
import random

broker="broker.hivemq.com"
#broker="iot.eclipse.org"


client= paho.Client() 
######Bind function to callback

#####
print("connecting to broker ",broker)
client.connect(broker)#connect

while(True):
    time.sleep(random.random()*10)
    if (random.random()>0.5) :
        client.publish("house/bulb1","on")
    else:
        client.publish("house/bulb1","off")