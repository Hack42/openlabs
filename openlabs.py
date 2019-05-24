#KADOOTJE VAN HACK42
import ugfx
import badge
import easywifi
import time
import machine
import gc
import time
from umqtt.simple import MQTTClient

state="CLOSED"
oldstate=state
oldtest=-1
pin=machine.Pin(33,machine.Pin.IN,machine.Pin.PULL_UP)

def test():
    return pin.value()

X=MQTTClient("openlabs42","test.mosquitto.org")
while True:
    thetest = test()
    if oldtest != thetest:
        easywifi.enable()
        X.connect()
        oldtest = thetest
        state = "CLOSED" if thetest == 1 else "OPEN"
        X.publish("openlabs/state/state",state,1)
        ugfx.clear(ugfx.WHITE if state=="OPEN" else ugfx.BLACK)
        ugfx.string_box(0,45,296,38, state, "PermanentMarker36", ugfx.BLACK if state=="OPEN" else ugfx.WHITE, ugfx.justifyCenter)
        ugfx.flush(ugfx.LUT_FULL)
        X.disconnect()
        easywifi.disable()
    time.sleep(1)
