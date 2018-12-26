# spudwatch.github.io
IoT Application used to monitor storage conditions on a farm - utilizing RPi and SenseHat

Uses HTTP to transfer data from the RPi Sensehat to the thingspeak platform.
Have 6 fields in thing speak
1. Temperature
2. Heater Status - On/Off
3. Cooler Status - On/Off
4. Humidity 
5. Humidifier Status - On/Off
6. Dehumidifer Status - On/Off

Also use thingtweet platform to tweet when temp or humidity go outside the desired range
