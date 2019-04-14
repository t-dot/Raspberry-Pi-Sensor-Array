import time
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 4

print('Press Ctrl-C to quit...')
while True:
	value = adc.read_adc_difference(0, gain=GAIN)
	value1 = adc.read_adc_difference(3, gain=GAIN)
	value2 = abs((value) - (value1))
	total = value2/750
	print('Channel 0 minus 1: {0}'.format(value))
	print('Channel 2 minus 3: {0}'.format(value1))
	print('DeltaV: {0}'.format(value2))
	print('Total: {0} ppb'.format(total))
	time.sleep(2)
