import tkinter as tk


class Setbox:
	def __init__(self, on_change, tk_master, json_data, on_duplicate, after):
		self.on_change_parent = on_change  # 改变时的回调函数
		self.tk_master = tk_master  # 此setbox(checkbox + text)属于的root窗口
		self.json_data = json_data  # 保存json配置数据, dict类型
		self.on_duplicate_parent = on_duplicate

		self.frame = tk.Frame(self.tk_master)

		self.var = tk.IntVar()
		cbtn = tk.Checkbutton(self.frame)
		cbtn["text"] = self.json_data['description']
		cbtn["variable"] = self.var
		cbtn["command"] = self.on_change
		cbtn.pack(side=tk.LEFT)

		self.txt = tk.Text(self.frame)
		self.txt["height"] = 1
		self.txt["state"] = "disabled"  # "normal", "disabled"
		self.txt.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)

		self.btn_duplicate = tk.Button(self.frame)
		self.btn_duplicate['text'] = "+"
		self.btn_duplicate['command'] = self.on_duplicate
		self.btn_duplicate.pack(side=tk.LEFT)

		self.frame.pack(expand=tk.YES, fill=tk.X, after=after)

	def __str__(self):
		if self.check():
			return self.json_data['value'] + ' ' + self.text()
		else:
			return ''

	def on_change(self):
		self.txt["state"] = "normal" if self.check() else "disabled"
		self.on_change_parent()

	# 直接通过self.var.set修改后, 不会执行tk.Button()['command']回调!!! 只能手动执行了
	def check(self, b=None):
		if b is not None:
			self.var.set(b)
			self.on_change()
		else:
			return self.var.get() == 1

	def text(self, str=None):
		if str is not None:
			self.txt.delete(1.0, tk.END)
			self.txt.insert(tk.END, str)
			self.on_change()
		else:
			return self.txt.get(1.0, tk.END)[:-1]

	def on_duplicate(self):
		self.on_duplicate_parent(self)


def create_setbox(on_change, tk_master, json_data, on_duplicate, after):
	return Setbox(on_change, tk_master, json_data, on_duplicate, after)


if __name__ == '__main__':
	import json

	json_rtn = json.loads('''
		{
			"type": "set",
			"description": "--append string  加入一些字符串",
			"value": "--append"
		}
	''')

	import tkinter as tk

	root = tk.Tk()
	frame = tk.Frame(root)

	set_box = create_setbox(lambda: print('p: ' + str(set_box)), root, json_rtn)

	print(set_box.check())
	set_box.check(True)
	print(set_box.check())
	set_box.check(False)

	set_box.text('Hello!!')
	print(set_box.text())


	frame.mainloop()
