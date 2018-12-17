import urllib2
import json
import time
from sense_hat import SenseHat

WRITE_API_KEY='1LG9Y1ADWFC5U1MX'

baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

sense = SenseHat()

humidifier = 0
dehumidifier = 0

red = (255,0,0)
green = (0,255,0)

def humidifier_on():
  global humidifier 
  sense.clear(red)
  time.sleep(1)
  if humidifier != 1:
    message = "Humidity Low, Turning On Humdiifer"
    sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])
    humidifier = 1
  else:
    message = "Humdiifer On"
    sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])

def dehumidifier_on():
  global dehumidifier 
  sense.clear(red)
  time.sleep(1)
  if dehumidifier != 1:
    message = "Humidity High, Turning On Dehumidifier"
    sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])
    dehumidifier = 1
  else:
    message = "Dehumdiifer On"
    sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])

def hum_equip_off():
  global humidifier
  global dehumidifier
  sense.clear(green)
  time.sleep(1)
  message = "Humidity Good, Turning Off Equipemnt if On"
  sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])
  
  if humidifier != 0:
    humidifier = 0
  
  if dehumidifier != 0:
    dehumidifier = 0

def writeData(temp)):
	  #sending data to thingspeak in query string
	  conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s&field3=%s&field4=%s' % (temp, hum, humidifier, dehumidifier))
	  print(conn.read())
	  #closing connection
	  conn.close()

while True:
	  global humidifier
          global dehumidifer
          temp=round(sense.get_temperature(),2)
	  hum=round(sense.get_humidity(),2)
	
	  if hum < 94:
	  	humidifier_on()
  	  elif hum > 96:
  		dehumidifier_on()
  	  else:
  		hum_equip_off()
		
 	  writeData(temp,hum,humidifier,dehumidifier)
          time.sleep(60)
