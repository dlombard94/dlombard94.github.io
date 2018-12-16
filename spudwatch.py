import urllib2
import json
import time
from sense_hat import SenseHat

WRITE_API_KEY='1LG9Y1ADWFC5U1MX'

baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY

sense = SenseHat()

def writeData(temp)):
	  #sending data to thingspeak in query string
	  conn = urllib2.urlopen(baseURL + '&field1=$s' % (hu(temp)))
	  print(conn.read())
	  #closing connection
	  conn.close()

while True:
	  hum=round(sense.get_humidity(),2)
 	  writeData(temp)
    sense.show_message(str(temp))
    time.sleep(60)
