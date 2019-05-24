#!/usr/bin/python
import paho.mqtt.client as paho
import requests
import time

oldstate = ""
def on_message(client, userdata, msg):
    global oldstate
    if msg.topic == "openlabs/state/state":
        spacestate = msg.payload
        if oldstate!="" and oldstate!=spacestate:
            r = requests.get("https://api.telegram.org/botXXXXX/sendMessage?chat_id=YYYYY&text=Open Labs is now "+spacestate)
            print spacestate
        oldstate = spacestate

client = client = paho.Client()
client.on_message = on_message
client.connect("37.187.106.16", 1883, 60)
client.subscribe("openlabs/state/state")

x=time.time()
while True:
    client.loop_start()
    time.sleep(0.5)
    if x + 1800 < time.time():
        client.disconnect()
        client.connect("37.187.106.16", 1883, 60)


