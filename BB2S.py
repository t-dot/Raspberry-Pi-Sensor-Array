#rpi serial connections
#Python app to run a K-30 Sensor
import serial
import time
import dothat.lcd as lcd
import Adafruit_DHT
from dothat import backlight

ser = serial.Serial("/dev/ttyAMA0",baudrate =9600,timeout = .5)
print "  AN-137: Raspberry Pi3 to K-30 Via UART\n"
ser.flushInput()
time.sleep(.1)
sensor = Adafruit_DHT.DHT22
pin = 5	

while 1:   
		ser.flushInput()
		ser.write("\xFE\x44\x00\x08\x02\x9F\x25")
		time.sleep(.1)
		resp = ser.read(7)
		high = ord(resp[3])
		low = ord(resp[4])
		co2 = (high*256) + low
		print_co2= 'CO2= %0.2f ppm' % (co2)
		
		humidity, temperature = Adafruit_DHT.read(sensor, pin)
		#temp = 'Temp= {0:0.1f}*C'.format(temperature)
		#hum = 'Humidity= {0:0.1f}%'.format(humidity)
		#print temp
		#print hum
		print print_co2
		lcd.clear()
		backlight.rgb(255, 255, 255)
		#lcd.set_cursor_position(0,0)
		#lcd.write(temp)
		#lcd.set_cursor_position(0,1)
		#lcd.write(hum)
		lcd.set_cursor_position(0,2)
		lcd.write(print_co2)
time.sleep(.1)

#if humidity is not None and temperature is not None:
	#temp_humidity = ('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
	#print temp_humidity

#humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#if humidity is not None and temperature is not None:
    #temp_humidity = ('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    #print temp_humidity
#else:
    #print('Failed to get reading. Try again!')
