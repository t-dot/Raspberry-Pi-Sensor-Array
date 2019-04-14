import gps
import time
 
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
 
while True:
    	report = session.next()
		# Wait for a 'TPV' report and display the current time
		# To see all report data, uncomment the line below
		# print report
	if report['class'] == 'TPV':
			if hasattr(report, 'lat'):
				
			if hasattr(report, 'lon'):
				
			if hasattr(report, 'alt'):
				
			if hasattr(report, 'speed'):
				
			#if hasattr(report, 'climb'):
				
			#if hasattr(report, 'track'):
				
			print "Latitude= {0:}".format(report.lat)
			print "Longitude= {0:}".format(report.lon)
			print "Speed= {0:} knots".format(report.speed)
			print "Altitude= {0:} meters".format(report.alt)
			#print "Climb= {0:} m/s".format(report.climb)
			#print "Track= {0:} Degrees from true north \n".format(report.track)
			
			
			
			time.sleep(2)
			
				
    #except KeyError:
		#pass
    #except KeyboardInterrupt:
		#quit()
   # except StopIteration:
		#session = None
		#print "GPSD has terminated"
		
		
		

#lon
#lat
#alt
#speed
#time
#climb
#track
#/usr/lib/python2.7/dist-packages/gps
