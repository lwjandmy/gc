import tkinter as tk
import sys
from Application.Application import Application

if __name__ == '__main__':
	if __debug__:
		root = tk.Tk()
		app = Application('ps', master=root)
		app.mainloop()
		exit()

	if len(sys.argv) != 2:
		print('''
			Usage: gc COMMAND-NAME
			Example: gc ps
		''')
		exit()
	root = tk.Tk()
	app = Application(sys.argv[1], master=root)
	app.mainloop()
