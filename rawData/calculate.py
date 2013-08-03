"""This module allows the user to convert a file to a SQLite3 database (../sql/radnet.db) It will also calculate the activity from the alpha/beta calibration numbers as well as insert that data into the database"""
import sys
import sqlite3
import datetime


def timeToHours(timeString):
	"""This function converts a string with the format HHMMSS to a decimal hour representation. This makes it easier to find the time difference in hours between two times"""
	time = float(timeString[0:2]) + float(timeString[2:4])/60.0 + float(timeString[4:6])/3600
	return time


# set calibration numbers if not in the data table
ALPHACALIBRATION = 1.63
BETACALIBRATION = 1.15


def calculate(filename):
	"""
	This method calculates the rest of the columns for the radnet data (format for the first few lines):
	#Filter
	#Start Date
	#End Date
	# Sample time
	# sample volumen
	"""
	#open connection to database file
	conn = sqlite3.connect("../sql/radnet.db")
	cur = conn.cursor()
	with open(filename,'r') as f:
		#get initial values
		filterNum = f.readline().rstrip()
		startDate = f.readline().rstrip()
		endDate = f.readline().rstrip()
		sampleTime = f.readline().rstrip()
		sampleVol = f.readline().rstrip()
		
		for line in f:
			#check if no line if len(line) != 0:
				#check for comment lines
				if line[0] != '#':
					#Check if it's the initial value for time and set it
					#this part is for the legacy typed data which didn't have the calibration numbers in the data textfile
					if ',' not in line:
						timeStart = timeToHours(line)
						alphaCal = ALPHACALIBRATION
						betaCal = BETACALIBRATION
					elif len(line.split(',')) == 3:
						timeStart,alphaCal,betaCal = line.rstrip().split(',')
						timeStart = timeToHours(timeStart)
						alphaCal = float(alphaCal)
						betaCal = float(betaCal)


					if ',' not in line or len(line.split(',')) == 3:
						#check database to see if alphaCal is in already
						cur.execute("""SELECT * FROM AlphaEfficiency WHERE coefficient = ?""", (alphaCal,))
						check = cur.fetchall()
						if check == []:
							cur.execute("""INSERT INTO AlphaEfficiency (Coefficient) VALUES (?)""", (alphaCal,))
							conn.commit()

						#get alphaCalID
						cur.execute("""SELECT AlphaCoeffID from AlphaEfficiency WHERE Coefficient = ?""", (alphaCal,))
						check = cur.fetchone()
						alphaCalID = check[0]

						#check database to see if betaCal is in already
						cur.execute("""SELECT * FROM BetaEfficiency WHERE coefficient = ?""", (betaCal,))
						check = cur.fetchall()
						if check == []:
							cur.execute("""INSERT INTO BetaEfficiency (Coefficient) VALUES (?)""", (betaCal,))
							conn.commit()

						#get betaCalID
						cur.execute("""SELECT BetaCoeffID from BetaEfficiency WHERE Coefficient = ?""",(betaCal,))
						check = cur.fetchone()
						betaCalID = check[0]


						
						#INSERT new filter row if no previous filter was there
						cur.execute("""SELECT * FROM Filter WHERE filterNum = ?""", (filterNum,))
						if cur.fetchall() == []:
							for i in [(filterNum,startDate,endDate,sampleTime,sampleVol,timeStart,alphaCalID,betaCalID)]:
								cur.execute("""INSERT INTO Filter (FilterNum, StartDate, EndDate, SampleTime, SampleVolume,TimeStart,AlphaCoeffID,BetaCoeffID) VALUES (?,?,?,?,?,?,?,?)""",i)
							conn.commit()
						else:
							print "No filter entry was created for " + startDate + "-" + endDate

						#get filterID
						cur.execute("""SELECT FilterID FROM Filter WHERE filterNum = ?""", (filterNum,))
						filterID = cur.fetchone()
						filterID = filterID[0]

						stuff = '# Date: ' + sys.argv[1] + '\n# t_stop = ' + str(timeStart) + '\n# Alpha Calibration: ' + str(alphaCal) + '\n# Beta Calibration: ' + str(betaCal) + '\n'
						print stuff

					else:
						#Set the values for each line
						#det2 is beta+Alpha reading
						#det1 is alpha reading
						#cfc is clean filter count
						time,det2,cfc,det1 = line.rstrip().split(',')
						time = timeToHours(time)
						det2 = int(det2)
						cfc = int(cfc)
						det1 = int(det1)

						#write this line into the database
						for i in [(filterID, time)]:
							cur.execute("""SELECT * FROM RawData WHERE FilterID = ? AND Time = ?""", i)
						if cur.fetchall() == []:
							for i in [(filterID, time, det1, det2, cfc)]:
								cur.execute("""INSERT INTO RawData (FilterID, Time, AlphaReading, BetaReading, CleanFilterCount) VALUES (?,?,?,?,?)""", i)
							conn.commit()

						#get rawDataID
						for i in [(filterID, time)]:
							cur.execute("""SELECT RawDataID FROM RawData WHERE FilterID = ? AND Time = ?""", i)
						rawDataID = cur.fetchone()
						rawDataID = rawDataID[0]



						#Calculate the other variables for each reading
						netAB = det2 - cfc
						netBeta = netAB - det1
						alphaActivity = det1 * alphaCal
						betaActivity = netBeta * betaCal

						#This is incase the readings were taken on the next day after the initial stop time (eg. if timeStart is 23:00:00 and the reading is 00:25:00)
						if time < timeStart:
							time += 24.0

						timeDiff = time - timeStart

						#write to database
						for i in [(filterID, rawDataID)]:
							cur.execute("""SELECT * FROM Activity WHERE FilterID = ? AND RawDataID = ?""", i)
						if cur.fetchall() == []:
							for i in [(filterID, rawDataID, timeDiff, alphaActivity, betaActivity)]:
								cur.execute("""INSERT INTO Activity(FilterID, RawDataID, DeltaT, AlphaAct, BetaAct) VALUES (?,?,?,?,?)""",i)
								conn.commit()
								printStuff = str(alphaActivity) + ' , ' + str(betaActivity) + ' , ' + str(timeDiff)
								print printStuff
						else:
							print 'blrrrrrg'


		print "File processed succesfully"
		conn.close()


if __name__ == "__main__":
	calculate(sys.argv[1])
