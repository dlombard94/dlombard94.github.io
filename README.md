# spudwatch.github.io
IoT Application used to monitor storage conditions on a farm - utilizing RPi and SenseHat

Uses HTTP to transfer data from the RPi Sensehat to the thingspeak platform.
Have a spudwatch2.py python program which when run monitors the temp and humidity.
Using crontab, I have this program automatically running when the RPi is turned on.
If outside the desired range the program will either turn on/off certain equipment

Have 6 fields in thing speak
1. Temperature
2. Heater Status - On/Off
3. Cooler Status - On/Off
4. Humidity 
5. Humidifier Status - On/Off
6. Dehumidifer Status - On/Off

These fields are being uploaded every 30 seconds
Also use thingtweet platform to tweet when temp or humidity go outside the desired range
