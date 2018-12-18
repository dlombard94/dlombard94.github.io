import urllib2
import json
import time
from sense_hat import SenseHat
import logging

#creates log file for monitoring purposes
logging.basicConfig(filename='spudwatch2.log',level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info('Starting SpudWatch')

WRITE_API_KEY='1LG9Y1ADWFC5U1MX'

baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

sense = SenseHat()

#declaring variables for the equipment (0 = off, 1 = on)
humidifier = 0
dehumidifier = 0
cooler = 0
heater = 0

#using rgb to define colors to be shown on Sensehat in certain situations
red = (255,0,0)
green = (0,255,0)

#function to turn on humidifer if not on already
def humidifier_on():
  global humidifier
  #sensehat flashes red
  sense.clear(red)
  time.sleep(1)
  #if humidifier not on, it is turned on and message is shown on the sensehat	
  if humidifier != 1:
    message = "Humidity Low, Turning On Humdiifer"
    sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])
    humidifier = 1
  else:
    #if already on, a message is shown to say this
    message = "Humdiifer On"
    sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])

#function to turn on dehumidifier if not on already
def dehumidifier_on():
  global dehumidifier 
  sense.clear(red)
  time.sleep(1)
  #if dehumidifier is off, it is turned on and message is shown on the sensehat
  if dehumidifier != 1:
    message = "Humidity High, Turning On Dehumidifier"
    sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])
    dehumidifier = 1
  else:
    #if already on, a message is shown to say this
    message = "Dehumdiifer On"
    sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])

#function to turn off all humidity equipment
def hum_equip_off():
  global humidifier
  global dehumidifier
  #sensehat flashes green
  sense.clear(green)
  time.sleep(1)
  message = "Humidity Good, Turning Off Equipemnt if On"
  sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])
  
  #if humidifier is on it is turned off
  if humidifier != 0:
    humidifier = 0

  #if dehumidifer is on it is turned off
  if dehumidifier != 0:
    dehumidifier = 0

#function to turn heater on if not on already
def heater_on():
  global heater 
  sense.clear(red)
  time.sleep(1)
  #if heater is off, it is turned on and message shown on the sensehat
  if heater != 1:
    message = "Temp Low, Turning On Heater"
    sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])
    heater = 1
  else:
    #if on already, a message is shown on th esensehat to state this
    message = "Heater On"
    sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])

#function to turn on the cooler if not on already
def cooler_on():
  global cooler 
  sense.clear(red)
  time.sleep(1)
  #if cooler is off, it is turned on and message shown on the sensehat
  if cooler != 1:
    message = "Temp High, Turning On Cooler"
    sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])
    cooler = 1
  else:
    #if cooler is on, a message is shown on the sensehat to state this
    message = "Cooler On"
    sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])

#function to turn off temperature equipment if on
def temp_equip_off():
  global cooler
  global heater
  sense.clear(green)
  time.sleep(1)
  message = "Temp Good, Turning Off Equipemnt if On"
  sense.show_message(message, scroll_speed=(0.05),text_colour=[0,255,0])
  
  #if cooler is turned on, it is turned off
  if cooler != 0:
    cooler = 0
  
  #if heater is turned on, it is turned off
  if heater != 0:
    heater = 0

def writeData(temp,hum,humidifier,dehumidifier,cooler,heater):
	  #sending data to thingspeak in query string
          #includes temperature and assoicated equipment and humidit and its assoiciated equipment
	  conn = urllib2.urlopen(baseURL + '&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s&field6=%s' % (temp, hum, humidifier, dehumidifier,cooler,heater))
	  print(conn.read())
	  #closing connection
	  conn.close()

while True:
	try:
	  global humidifier
          global dehumidifer
	  global cooler
          global heater
	  #getting temperature and humidity from the sense hat
          temp=round(sense.get_temperature(),2)
	  hum=round(sense.get_humidity(),2)
	
          #check if the humidity is within range or not 
	  #if ok - equipment is turned off
	  #if low - humidifier is turned on
	  #if high - the dehumidifier is turned on
	  if hum < 94:
	  	humidifier_on()
  	  elif hum > 96:
  		dehumidifier_on()
  	  else:
  		hum_equip_off()
	  
	
	  #check if the temperature is within range or not 
	  #if ok - equipment is turned off
	  #if low -  heater is turned on
	  #if high - cooler is turned on
	  if temp < 3.5:
                heater_on()
          elif temp > 5.5:
                cooler_on()
          else:
                temp_equip_off()
	
          #uses defined fucntion above to push all necessay variables up to thingspeak	
 	  writeData(temp,hum,humidifier,dehumidifier,cooler,heater)
	  
	  #repeats every 30 seconds
          time.sleep(30)
	except Exception as e:
          logging.error(e)

