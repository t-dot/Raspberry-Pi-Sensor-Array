#This is CO2/Temp/Rh

from Adafruit_BME280 import *
import curses
import serial
import time
import Adafruit_DHT

ser = serial.Serial("/dev/ttyAMA0")
print "We are sensing."
ser.flushInput()
time.sleep(.01)
pin = 5
def main(stdscr):
	sensor = Adafruit_DHT.DHT22()
	
	stdscr.nodelay(1)
	tstart = time.time()
	while (stdscr.getch() == -1) :
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
		#humidity = Adafruit_DHT.read(sensor, pin)
        #temperature = Adafruit_DHT.read(sensor, pin)
		
	while True:
		ser.write("\xFE\x44\x00\x08\x02\x9F\x25")
    	time.sleep(0.01)
    	resp = ser.read(7)
    	high = ord(resp[3])
    	low = ord(resp[4])
    	co2 = (high*256) + low
    	
        stdscr.addstr(0, 0, 'Timestamp = %0.3f sec' % (time.time() - tstart))
        stdscr.addstr(1, 0, 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        stdscr.addstr(2, 0, 'Humidity  = %0.2f %%' % humidity)
        stdscr.addstr(3, 0, 'Carbon Dioxide = %0.2f ppm' % co2)
        stdscr.addstr(4, 0, 'Press any key to exit...')
	stdscr.refresh()

        time.sleep(.5)

        stdscr.erase()
        
curses.wrapper(main)       

