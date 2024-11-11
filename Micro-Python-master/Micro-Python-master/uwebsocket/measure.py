import uwebsockets.client
import sys,time
import network
from machine import Pin
from time import sleep
import _thread
import upip
import dht 
import machine, time
import ujson
from machine import Timer

TIMEOUT_MS = 5000 #soft-reset will happen around 5 sec
sensor = dht.DHT22(Pin(14))
def timeout_callback(t):
    try:
        #sleep(20)
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        temp_f = temp * (9/5) + 32.0
        print('Temperature: %3.1f C' %temp)
        print('Temperature: %3.1f F' %temp_f)
        print('Humidity: %3.1f %%' %hum)
        #print("I am in Call back")
        dict={}
        dict["action"]="onMessage"
        dict["message"]=str(temp)
        websocket.send(ujson.dumps(dict))
        #websocket.send(str(temp))
        #websocket.send("Ws send \r")
    finally:
        print("")
       

def wlan_connect(ssid,pwd):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid,pwd)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    #upip.install("")
    
    
wlan_connect('KMIT-Colleage', 'A1B2C3D4E5')
uri = "wss://s8xnksme9e.execute-api.ap-northeast-1.amazonaws.com/dev"
websocket = uwebsockets.client.connect(uri)
while True:
    #print("Enter Command:\r")
    #mesg=input()
    #websocket.send(mesg + "\r")
    timer = Timer(0)
    timer.init(period=TIMEOUT_MS, callback=timeout_callback)
    resp = websocket.recv()
    #print(resp)
    print(ujson.dumps(resp))