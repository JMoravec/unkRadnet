from tkinter import *
from tkinter.messagebox import *

def notDone():
	showerrror('Not implemented', 'Not yet available')

def makeMenu(win):
	top = Menu(win)
	win.config(menu=top)
	file = Menu(top, tearoff=False)
	file.add_command(label='Quit', command=win.quit, underline=0)
	top.add_cascade(label='File', menu=file, underline=0)

if __name__ == '__main__':
	root = Tk()
	root.title('menu_win')
	makeMenu(root)
	msg = Label(root, text='Menu Test')
	msg.pack(expand=YES, fill=BOTH)
	msg.config(relief=SUNKEN, width=40, height=7, bg='beige')
	root.mainloop()
