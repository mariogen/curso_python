import paho.mqtt.client as paho

broker="broker.hivemq.com"
#broker="iot.eclipse.org"

#define callback
def on_message(client, userdata, message):
    print("received message =",message.payload)

client= paho.Client() 
######Bind function to callback
client.on_message=on_message

#####
print("connecting to broker ",broker)
client.connect(broker)#connect
print("subscribing ")
client.subscribe("house/bulb1")#subscribe
print("looping forever ")
client.loop_forever() #stop loop