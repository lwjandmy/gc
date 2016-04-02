import tkinter as tk
import json
import os
from Application.Boxes.BoxList import create_boxlist


class Application(tk.Frame):
	def __init__(self, command_name, master=None):
		tk.Frame.__init__(self, master)
		self.pack()
		self.command_name = command_name  # 命令的名字, 如ps, cat等
		json_rtn = json.loads(open(self.command_name + '.json').read())
		self.boxlist = create_boxlist(self.on_change, self, json_rtn)

		# 输出生成的命令
		self.text_output = tk.Text(self)
		self.text_output['height'] = 1
		self.text_output.pack()

		self.btn_execute = tk.Button(self)
		self.btn_execute['text'] = 'Execute'
		self.btn_execute['command'] = self.on_execute
		self.btn_execute.pack()

		self.btn_quit = tk.Button(
				self, text="QUIT", fg="red",
				command=master.destroy)
		self.btn_quit.pack()

	def __str__(self):
		return self.command_name + ' ' + str(self.boxlist)

	def output(self, str):
		self.text_output.delete(1.0, tk.END)
		self.text_output.insert(tk.END, str)


	def on_execute(self):
		print(str(self))
		self.on_change()
		os.system(str(self))
		self.btn_quit.invoke()

	def on_change(self):
		self.output(str(self))


if __name__ == '__main__':
	import tkinter as tk

	root = tk.Tk()
	app = Application('ps', master=root)
	app.mainloop()
