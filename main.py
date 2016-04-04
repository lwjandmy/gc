import tkinter as tk
import sys
# from controllers.application import Application
from Application.Application import Application


if __name__ == '__main__':
	if __debug__:
		root = tk.Tk()
		app = Application('ps', root)
		tk.mainloop()
		exit()

	if len(sys.argv) != 2:
		print('''
			Usage: gc COMMAND-NAME
			Example: gc ps
		''')
		exit()
	root = tk.Tk()
	app = Application(sys.argv[1], root)
	tk.mainloop()
