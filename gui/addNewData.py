import sys
from Tkinter import *
import sqlite3
import datetime
import time

def exit(win):
	win.destroy()

def addRow(win, lineEnts):
	currentColumn, currentRow = win.grid_size()
	
	entTime = Entry(win,width=7)
	entTime.grid(row=(currentRow), column=3)

	entDet2 = Entry(win,width=10)
	entDet2.grid(row=(currentRow), column=5)

	entCfc = Entry(win,width=10)
	entCfc.grid(row=(currentRow), column=7)

	entDet1 = Entry(win,width=10)
	entDet1.grid(row=(currentRow), column=9)

	lineEnts.append([entTime, entDet2, entCfc, entDet1])

def calculate(win, lineEnts, headerEnts):
	timeStart = headerEnts[5].get()
	if not isTimeFormat(timeStart):
		print 'That string is no good'

def addNewData():
	win = Toplevel()

	headerEnts = []
	lineEnts = []

	Label(win,text='Filter #').grid(row=0,column=2)
	entFilterNum = Entry(win,width=7)
	entFilterNum.grid(row=0,column=3)
	headerEnts.append(entFilterNum)

	Label(win,text='Start Date (YYYY-MM-DD)').grid(row=0,column=4)
	entStartDate = Entry(win,width=10)
	entStartDate.grid(row=0,column=5)
	headerEnts.append(entStartDate)

	Label(win,text='End Date (YYYY-MM-DD)').grid(row=1,column=4)
	entEndDate = Entry(win,width=10)
	entEndDate.grid(row=1,column=5)
	headerEnts.append(entEndDate)
	
	Label(win, text='Sample Time (hours)').grid(row=0,column=6)
	entSampleTime = Entry(win,width=10)
	entSampleTime.grid(row=0,column=7)
	headerEnts.append(entSampleTime)

	Label(win, text='Sample Volume (m^3)').grid(row=0,column=8)
	entSampleVol = Entry(win,width=10)
	entSampleVol.grid(row=0,column=9)
	headerEnts.append(entSampleVol)

	Label(win, text='t_stop (HHMMSS)').grid(row=2,column=2)
	entTStop = Entry(win,width=7)
	entTStop.grid(row=2,column=3)
	headerEnts.append(entTStop)

	Label(win, text='Alpha Calibration Number').grid(row=2,column=4)
	entAlphaCal = Entry(win,width=10)
	entAlphaCal.grid(row=2,column=5)
	headerEnts.append(entAlphaCal)
	
	Label(win, text='Beta Calibration Number').grid(row=2,column=6)
	entBetaCal = Entry(win,width=10)
	entBetaCal.grid(row=2,column=7)
	headerEnts.append(entBetaCal)
	

	Label(win, text='Time Measured (HHMMSS)').grid(row=3,column=2)
	entTime1 = Entry(win,width=7)
	entTime1.grid(row=3,column=3)

	Label(win,text='Det 2 (Beta + Alpha)').grid(row=3, column=4)
	entdet21 = Entry(win,width=10)
	entdet21.grid(row=3, column=5)

	Label(win, text='Clean Filter Count').grid(row=3, column=6)
	entCfc1 = Entry(win,width=10)
	entCfc1.grid(row=3, column=7)

	Label(win, text='Det 1 (Alpha)').grid(row=3, column=8)
	entDet11 = Entry(win,width=10)
	entDet11.grid(row=3, column=9)

	lineEnts.append([entTime1, entdet21, entCfc1, entDet11])

	butCancel = Button(win, text='Cancel', command=lambda: exit(win))
	butCancel.grid(row=0,column=1)

	butAddNew = Button(win, text='Add new row', command=lambda: addRow(win, lineEnts))
	butAddNew.grid(row=1,column=1)

	butCalc = Button(win, text='Calculate',command=lambda: calculate(win, lineEnts, headerEnts))
	butCalc.grid(row=2,column=1)

	win.focus_set()
	win.grab_set()
	win.wait_window()

def timeToHours(timeString):
	"""This function converts a string with the format HHMMSS to a decimal hour representation. This makes it easier to find the time difference in hours between two time"""
	time = float(timeString[0:2]) + float(timeString[2:4])/60.0 + float(timeString[4:6])/3600
	return time

def isTimeFormat(input):
	try:
		time.strptime(input, '%H%M%S')
		return True
	except ValueError:
		return False

if __name__ == '__main__':
	root = Tk()
	Button(root, text='bla', command=addNewData).pack()
	Button(root, text='quit', command=sys.exit).pack()
	root.mainloop()
