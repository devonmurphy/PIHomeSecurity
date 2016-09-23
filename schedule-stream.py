import os
import time
from datetime import datetime
import time
import subprocess
import sys

#Print the date and time
print ("Current date and time is: ") 
currentDateTime = (str(datetime.now())[:-7]).replace("-"," ")
print(currentDateTime)

#Take in a start date as input
i = str(raw_input('Enter a start date (year month day hour:minute:second):\n'))
try:
    startDate = datetime.strptime(i, '%Y %m %d %H:%M:%S')
except ValueError:
    print "Incorrect format"

#Take in a end date as input
i = str(raw_input('Enter an end date (year month day hour:minute:second):\n'))
try:
    endDate = datetime.strptime(i, '%Y %m %d %H:%M:%S')
except ValueError:
    print "Incorrect format"

#Convert datetime to seconds since Unix Epoch
startTime = time.mktime(datetime.timetuple(startDate))
endTime = time.mktime(datetime.timetuple(endDate))

#Initialize start
start = False

while(1):

	#Sleep for one second so the process doesn't take up much cpu
	time.sleep(1)

	#Set last equal to start to keep track if start has changed
	last = start

	#Check if the current time is greater than the start time and less than the end time
	#If it is, then set start to True
	if(time.time()>= startTime and time.time() <= endTime):
		start = True
		print("Seconds until stream ends: "+ str(endTime - time.time())+"\r"),
		sys.stdout.flush()

	#If the current time is outside of our scheduled time then set start to false
	else:
		start = False
		print("Seconds until stream starts: "+ str(startTime - time.time())+"\r"),
		sys.stdout.flush()

	#If the value of start has changed then start/stop the stream
	if(last != start):

		if(start == True):
			print("Starting Stream...")
			os.spawnlp(os.P_NOWAIT,"/home/pi/PIHomeSecurity/utils/python-start-stream","python-start-stream")

		if(start == False):
			print("Ending Stream...")
			os.system("pkill ffmpeg")
			os.system("pkill raspivid")
			break;
