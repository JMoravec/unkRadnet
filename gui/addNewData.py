import sys
from tkinter import *

def exit(win,ent):
	print(ent.get())
	win.destroy()

def addNewData():
	win = Toplevel()

	Label(win,text='Filter #').grid(row=0,column=1)
	entFilterNum = Entry(win,width=7)
	entFilterNum.grid(row=0,column=2)

	Label(win,text='Start Date').grid(row=0,column=3)
	entStartDate = Entry(win)
	entStartDate.insert(0, 'YYYY-MM-DD')
	entStartDate.grid(row=0,column=4)

	Label(win,text='End Date').grid(row=1,column=3)
	entEndDate = Entry(win)
	entEndDate.insert(0, 'YYYY-MM-DD')
	entEndDate.grid(row=1,column=4)
	
	Label(win, text='Sample Time (hours)').grid(row=0,column=5)
	entSampleTime = Entry(win)
	entSampleTime.grid(row=0,column=6)

	Label(win, text='Sample Volume (m^3)').grid(row=0,column=7)
	entSampleVol = Entry(win)
	entSampleVol.grid(row=0,column=8)

	Label(win, text='t_stop').grid(row=2,column=1)
	entTStop = Entry(win)
	entTStop.insert(0, 'HHMMSS')
	entTStop.grid(row=2,column=2)

	Label(win, text='Alpha Calibration Number').grid(row=2,column=3)
	entAlphaCal = Entry(win)
	entAlphaCal.grid(row=2,column=4)
	
	Label(win, text='Beta Calibration Number').grid(row=2,column=5)
	entBetaCal = Entry(win)
	entBetaCal.grid(row=2,column=6)


	Button(win, text='ok', command=lambda: exit(win,entFilterNum)).grid(row=6,column=2)
	win.focus_set()
	win.grab_set()
	win.wait_window()


if __name__ == '__main__':
	root = Tk()
	Button(root, text='bla', command=addNewData).pack()
	Button(root, text='quit', command=sys.exit).pack()
	root.mainloop()
