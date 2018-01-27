#!/usr/bin/python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt # Klient importieren
import time

import sys
import Adafruit_DHT

broker ="172.22.72.xxx"

# Parameter von der Method read_retry sind: DHT-Typ und Port
feuchtigkeit, temp = Adafruit_DHT.read_retry(11,4)

thema_t = "MQTT/DeviceID123/temperatur" #thema für Temperatur
thema_h = "MQTT/DeviceID123/feuchtigkeit" #thema für Luftfeuchtigkeit

print(" Eine neue Klienteninstanz erzeugen")
client = mqtt.Client("a-a3wbxy-s0hi3rf1z4",transport="tcp")
print("Verbindung mit dem Broker erstellt")
print("Anmeldung zum Thema:", thema_t)
print("Anmeldung zum Thema:", thema_h)

while True:
    try:                            
        
        
        time.sleep(5)              # Jitter
        client.subscribe(thema_t)
        print("Botschaft zu dem Thema ",thema_t," veröffentlicht")
        client.publish(topic = thema_t,payload = str("Temperatur: ")+str(temp)+str(" °C\n"), retain = False)

        client.subscribe(thema_h)
        print("Botschaft zu dem Thema ",thema_h," veröffentlicht")
        client.publish(topic = thema_h,payload = str("Feutigkeit: ")+str(feutigkeit)+str("%"), retain = False)

        client.connect(broker) # connect to broker
    except(EOFError, SystemExit, KeyboardInterrupt, UnicodeError):
        client.disconnect()
        print("Ende des Themas: ",thema_t)
        print("Ende des Themas: ",thema_h)
        sys.exit()
