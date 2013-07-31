import sys
from tkinter import *
from tkinter.messagebox import *
from makeMenu import *
from addNewData import *

def notDone():
	showerror('Not implemented', 'Not yet available')

def makeStartPage(win):
	win.configure(background='white')
	Label(win,bg='white', text="RadNet").pack(side=TOP,pady=10)
	Button(win,bg='white', text="Add New Data", command=addNewData, width=30).pack(padx=10, pady=10)
	Button(win, bg='white',text='View Raw Data', command=sys.exit, width=30).pack(padx=10, pady=10)
	Button(win,bg='white', text='Make Graphs', command=sys.exit, width=30).pack(padx=10, pady=10)
	win.title('Radnet')

if __name__ == '__main__':
	root = Tk()
	makeStartPage(root)
	root.mainloop()
