#Drone without gps/NO

import serial
import time
from Adafruit_BME280 import *
import datetime
import smbus



bus = smbus.SMBus(1)

ser = serial.Serial("/dev/ttyAMA0")
ser.flushInput()

sensor = BME280(p_mode=BME280_OSAMPLE_8, t_mode=BME280_OSAMPLE_2, h_mode=BME280_OSAMPLE_1, filter=BME280_FILTER_16)
print "Serial Connected!"
time.sleep(1)

with open("Outside5Test.csv", "a") as log:
	while True:
			
			ser.write("\xFE\x44\x00\x08\x02\x9F\x25")
			resp = ser.read(7)
			high = ord(resp[3])
			low = ord(resp[4])
			co2 = (high*256) + low
			
			#Sets variables from BME280
			celsius = sensor.read_temperature()
			farenheight = celsius * 1.8 + 32
			pascals = sensor.read_pressure()
			torr = pascals * 0.00750062
			#hectopascals = pascals / 100
			humidity = sensor.read_humidity()
			#To get pressure in inches of Hg
			inches = pascals * 0.0002953
			#To get Altitude from pressure
			sealevel_pa = 101325 ##Enter Sea Level Pressure for that Day##
			altitude = 44330.0 * (1.0 - pow(pascals / sealevel_pa, (1.0/5.255)))
			
			bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
			bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)
			data = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)
			data1 = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)
			ch0 = data[1] * 256 + data[0]
			ch1 = data1[1] * 256 + data1[0]
			
			print (time.strftime("%H:%M:%S %m/%d/%Y"))
			print ("Temp= {0:f} *C".format(celsius))
			print ("Humidity= {0:f} %".format(humidity))
			print ("Pressure= {0:f} torr".format(torr))
			#print ("Altitude= {0:f} meters".format(altitude))
			print ("Full Spectrum(IR + Visible)= %d lux" %ch0)
			print ("Infrared Value= %d lux" %ch1)
			print ("Visible Value= %d lux" %(ch0 - ch1))
			print ("CO2= {0:f} ppm \n".format(co2))
			
				
			log.write(time.strftime("%H:%M:%S %m/%d/%Y \n"))
			log.write("Temp= {0:f} ;*C \n".format(celsius))
			log.write("Humidity= {0:f} ;% \n".format(humidity))
			log.write("Pressure= {0:f} ;torr \n".format(torr))
			#log.write("Altitude= {0:f} ;meters \n".format(altitude))
			log.write("Full Spectrum(IR + Visible)= %d ;lux \n" %ch0)
			log.write("Infrared Value= %d ;lux \n" %ch1)
			log.write("Visible Value= %d ;lux \n" %(ch0 - ch1))
			log.write("CO2= {0:f} ;ppm \n \n".format(co2))
			log.flush()
			
			time.sleep(1)
			
	
