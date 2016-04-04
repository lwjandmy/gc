import tkinter as tk
import json
import os
import os.path
from Application.Boxes.BoxList import create_boxlist


class Application():
	def __init__(self, command_name, tk_master):
		self.command_name = command_name  # 命令的名字, 如ps, cat等
		self.tk_master = tk_master

		filepath = os.path.join(os.path.dirname(__file__), '../plugins', self.command_name + '.json')
		json_rtn = json.loads(open(filepath).read())
		self.boxlist = create_boxlist(self.on_change, self.tk_master, json_rtn)

		# 输出生成的命令
		self.text_output = tk.Text(self.tk_master)
		self.text_output['height'] = 1
		self.text_output.pack(expand=tk.YES, fill=tk.X)

		self.frame_bottom = tk.Frame(self.tk_master)

		self.btn_execute = tk.Button(self.frame_bottom)
		self.btn_execute['text'] = 'Execute'
		self.btn_execute['command'] = self.on_execute
		self.btn_execute.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)

		self.btn_quit = tk.Button(self.frame_bottom)
		self.btn_quit['text'] = 'Quit'
		self.btn_quit['fg'] = 'red'
		self.btn_quit['command'] = self.tk_master.destroy
		self.btn_quit.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)

		self.frame_bottom.pack()

		self.on_change()

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
	app = Application('ps', root)
	tk.mainloop()
