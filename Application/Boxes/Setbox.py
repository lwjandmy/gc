import tkinter as tk


# @description: Setbox的辅助函数
# @return: IntVar() Text()
def add_setbox(master, text, on_change):

	var = tk.IntVar()
	cbtn = tk.Checkbutton(master)
	cbtn["text"] = text
	cbtn["variable"] = var
	cbtn["command"] = on_change
	cbtn.pack()

	txt = tk.Text(master)
	txt["height"] = 1
	# txt["state"] = "disabled"  # "normal", "disabled"
	txt.pack()

	return var, txt


class Setbox:
	def __init__(self, on_change, tk_master, json_data):
		self.on_change_parent = on_change  # 改变时的回调函数
		self.tk_master = tk_master  # 此setbox(checkbox + text)属于的root窗口
		self.json_data = json_data  # 保存json配置数据, dict类型
		self.var, self.txt = add_setbox(tk_master, self.json_data['description'],
				self.on_change)  # IntVar(), 可获取checkbox是否打勾; txt.get(1.0, tk.END)可获取text文本

	def __str__(self):
		if (self.check()):
			return self.json_data['value'] + ' ' + self.text()
		else:
			return ''

	def on_change(self):
		self.txt["state"] = "normal" if self.check() else "disabled"
		self.on_change_parent()

	# 直接通过self.var.set修改后, 不会执行tk.Button()['command']回调!!! 只能手动执行了
	def check(self, b=None):
		if b != None:
			self.var.set(b)
			self.on_change()
		else:
			return self.var.get() == 1

	def text(self, str=None):
		if str != None:
			self.txt.delete(1.0, tk.END)
			self.txt.insert(tk.END, str)
			self.on_change()
		else:
			return self.txt.get(1.0, tk.END)[:-1]



def create_setbox(on_change, tk_master, json_data):
	return Setbox(on_change, tk_master, json_data)


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
