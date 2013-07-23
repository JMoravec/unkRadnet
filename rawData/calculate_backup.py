import sys

#this function converts a string with the format HHMMSS to a decimal hour representation. This makes it easier to find the time difference in hours between two times
def timeToHours(timeString):
	time = float(timeString[0:2]) + float(timeString[2:4])/60.0 + float(timeString[4:6])/3600
	return time


# set calibration numbers if not in the data table!!
ALPHACALIBRATION = 1.63
BETACALIBRATION = 1.15


def calculate(filename):
#open file from system arguments
	with open(filename,'r') as f:
		with open(filename + 'Activity','w') as w:
			for line in f:
				if len(line) != 0:
					#check for commented lines
					if line[0] != '#':
						#Check if it's the initital value for time and set it
						#this part is for the legacy typed data which didn't have the calibration numbers in the data textfile
						if ',' not in line:
							timeStart = timeToHours(line)
							alphaCal = ALPHACALIBRATION
							betaCal = BETACALIBRATION
							stuff = '# Date: ' + sys.argv[1] + '\n# t_stop = ' + line + '# Alpha Calibration: ' + str(alphaCal) + '\n# Beta Calibration: ' + str(betaCal) + '\n'
							w.write(stuff)
							print stuff
						elif len(line.split(',')) == 3:
							timeStart,alphaCal,betaCal = line.split(',') 
							stuff = '# Date: ' + sys.argv[1] + '\n# t_stop = ' + timeStart + '\n# Alpha Calibration: ' + str(alphaCal) + '\n# Beta Calibration: ' + str(float(betaCal)) + '\n'
							timeStart = timeToHours(timeStart)
							alphaCal = float(alphaCal)
							betaCal = float(betaCal)
							w.write(stuff)
							print stuff
						else:
							#Set the values for each line.
							time,det2,cfc,det1 = line.split(',')
							time = timeToHours(time)
							det2 = int(det2)
							cfc = int(cfc)
							det1 = int(det1)

							#Calculate the other variables for each reading
							netAB = det2 - cfc
							netBeta = netAB - det1
							alphaActivity = det1 * alphaCal
							betaActivity = netBeta * betaCal

							#This is incase the readings were taken on the next day after the initial stop time (eg. if timeStart is 23:00:00 and the reading is 00:25:00)
							if time < timeStart:
								time += 24.0

							timeDiff = time - timeStart
							#set the string for print to file and screen
							stuff = str(timeDiff) + ',' + str(alphaActivity) + ',' + str(timeDiff) + ',' + str(betaActivity) 
							printStuf = str(alphaActivity) + ' , ' + str(betaActivity) + ' , ' + str(timeDiff)
							print(printStuf)
							stuff += '\n'
							w.write(stuff)



			w.close()
		f.close()

if __name__ == "__main__":
	calculate(sys.argv[1])
