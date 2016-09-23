import os
import time
from datetime import datetime
import time
import subprocess
import sys

print ("Current date and time is: ") 

currentDateTime = (str(datetime.now())[:-7]).replace("-"," ")
print(currentDateTime)
i = str(raw_input('Enter a start date (year month day hour:minute:second):\n'))
try:
    startDate = datetime.strptime(i, '%Y %m %d %H:%M:%S')
except ValueError:
    print "Incorrect format"

i = str(raw_input('Enter an end date (year month day hour:minute:second):\n'))
try:
    endDate = datetime.strptime(i, '%Y %m %d %H:%M:%S')
except ValueError:
    print "Incorrect format"
startTime = time.mktime(datetime.timetuple(startDate))
endTime = time.mktime(datetime.timetuple(endDate))

start = False
while(1):
	last = start
	time.sleep(1)	
	if(time.time()>= startTime and time.time() <= endTime):
		start = True
		print("Seconds until stream ends: "+ str(endTime - time.time())+"\r"),
		sys.stdout.flush()
	else:
		start = False
		print("Seconds until stream starts: "+ str(startTime - time.time())+"\r"),
		sys.stdout.flush()
	if(last != start):
		if(start == True):
			print("Starting Stream...")
			os.spawnlp(os.P_NOWAIT,"/home/pi/PIHomeSecurity/start-stream","start-stream")
		if(start == False):
			print("Ending Stream...")
			os.system("pkill ffmpeg")
			os.system("pkill raspivid")
			break;
