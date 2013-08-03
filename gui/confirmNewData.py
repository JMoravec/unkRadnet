from Tkinter import *
import sqlite3
from datetime import datetime 
from decimal import Decimal

TWOPLACES = Decimal(10) ** -2

def confirmData(filterID):
	win = Toplevel()
	conn = sqlite3.connect("../sql/test.db")
	cur = conn.cursor()

	cur.execute("""SELECT * FROM Filter WHERE FilterId = ?""", (filterID,))
	sqlStuff = cur.fetchone()
	filterNum = 	sqlStuff[1]
	startDate = 	sqlStuff[2]
	endDate = 		sqlStuff[3]
	sampleTime = 	sqlStuff[4]
	sampleVol = 	sqlStuff[5]
	timeStart = 	sqlStuff[6]
	alphaCoeffID = 	sqlStuff[7]
	betaCoeffID = 	sqlStuff[8]

	startDate = datetime.strptime(str(startDate), "%Y%m%d")
	endDate = datetime.strptime(str(endDate), "%Y%m%d")

	cur.execute("""SELECT Coefficient FROM AlphaEfficiency WHERE AlphaCoeffID = ?""", (alphaCoeffID,))
	alphaCoeff = cur.fetchone()[0]

	cur.execute("""SELECT Coefficient FROM BetaEfficiency WHERE BetaCoeffID = ?""", (betaCoeffID,))
	betaCoeff = cur.fetchone()[0]

	Label(win, text='Filter #:').grid(row=0, column=2)
	Label(win, text=filterNum).grid(row=0, column=3)

	Label(win, text='Start Date:').grid(row=0, column=4)
	Label(win, text=startDate.strftime("%Y-%m-%d")).grid(row=0,column=5)

	Label(win, text='End Date:').grid(row=1, column=4)
	Label(win, text=endDate.strftime("%Y-%m-%d")).grid(row=1, column=5)

	Label(win, text='Sample Time:').grid(row=0,column=6)
	Label(win, text=sampleTime).grid(row=0,column=7)

	Label(win, text='Sample Volume:').grid(row=0,column=8)
	Label(win, text=sampleVol).grid(row=0,column=9)

	Label(win, text='t_stop (decimal form):').grid(row=2,column=2)
	Label(win, text=Decimal(str(timeStart)).quantize(TWOPLACES)).grid(row=2,column=3)
	#Decimal('3.214').quantize(TWOPLACES)

	Label(win, text='Alpha Calibration #:').grid(row=2, column=5)
	Label(win, text=alphaCoeff).grid(row=2,column=6)

	Label(win, text='Beta Calibration #:').grid(row=2,column=7)
	Label(win, text=betaCoeff).grid(row=2,column=8)

	Button(win, text='OK', command=win.destroy).grid(row=0,column=1)
	Button(win, text='Cancel', command=win.destroy).grid(row=1,column=1)

	Label(win, text='t (in hours)').grid(row=3, column=2)
	Label(win, text='DET 2 (a, B)').grid(row=3, column=3)
	Label(win, text='DET 2 (CFC)').grid(row=3, column=4)
	Label(win, text='NET (a, B)').grid(row=3, column=5)
	Label(win, text='DET (a)').grid(row=3, column=6)
	Label(win, text='NET (B)').grid(row=3, column=7)
	Label(win, text='a Act in pCi').grid(row=3, column=8)
	Label(win, text='B Act in pCi').grid(row=3, column=9)
	Label(win, text='t - t_stop').grid(row=3, column=10)

	cur.execute("""SELECT * FROM RawData JOIN Activity ON (Rawdata.RawdataID = Activity.RawdataID) WHERE Rawdata.FilterID = ? ORDER BY RawDataID ASC""", (filterID,))
	sqlStuff = cur.fetchall()

	for row in sqlStuff:
		time = row[2]
		alphaReading = row[3]
		betaReading = row[4]
		cfc = row[5]
		deltaT = row[9]
		alphaAct = row[10]
		betaAct = row[11]
		netBetaAlpha = betaReading - cfc
		netBeta = netBetaAlpha - alphaReading

		currentColumn, currentRow = win.grid_size()

		Label(win, text=(Decimal(str(time)).quantize(TWOPLACES))).grid(row=currentRow, column=2)
		Label(win, text=betaReading).grid(row=currentRow, column=3)
		Label(win, text=cfc).grid(row=currentRow, column=4)
		Label(win, text=netBetaAlpha).grid(row=currentRow, column=5)
		Label(win, text=alphaReading).grid(row=currentRow, column=6)
		Label(win, text=netBeta).grid(row=currentRow, column=7)
		Label(win, text=(Decimal(str(alphaAct)).quantize(TWOPLACES))).grid(row=currentRow, column=8)
		Label(win, text=(Decimal(str(betaAct)).quantize(TWOPLACES))).grid(row=currentRow, column=9)
		Label(win, text=(Decimal(str(deltaT)).quantize(TWOPLACES))).grid(row=currentRow, column=10)




if __name__ == '__main__':
	root = Tk()
	Button(root, text='bla', command=lambda: confirmData(1)).pack()
	Button(root, text='quit', command=sys.exit).pack()
	root.mainloop()
