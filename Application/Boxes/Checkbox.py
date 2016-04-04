import tkinter as tk


class Checkbox:
	def __init__(self, on_change, tk_master, json_data, on_duplicate, after):
		self.on_change = on_change  # 改变时的回调函数
		self.tk_master = tk_master  # 此checkbox属于的root窗口
		self.json_data = json_data  # json中保存的数据, dict结构
		self.on_duplicate_parent = on_duplicate

		self.frame = tk.Frame(self.tk_master)

		self.var = tk.IntVar()
		cbtn = tk.Checkbutton(self.frame)
		cbtn["text"] = self.json_data['description']
		cbtn["variable"] = self.var
		cbtn["command"] = self.on_change
		cbtn.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)

		self.btn_duplicate = tk.Button(self.frame)
		self.btn_duplicate['text'] = "+"
		self.btn_duplicate['command'] = self.on_duplicate
		self.btn_duplicate.pack(side=tk.LEFT)

		self.frame.pack(expand=tk.YES, fill=tk.X, after=after)

	def __str__(self):
		if self.check():
			return self.json_data['value']
		else:
			return ''

	# check() 获取是否打勾; check(True/False) 设置/去掉钩
	def check(self, b=None):
		if b is not None:
			self.var.set(b)
			self.on_change()
		else:
			return self.var.get() == 1

	def on_duplicate(self):
		self.on_duplicate_parent(self)

# 工厂方法
def create_checkbox(on_change, tk_master, json_data, on_duplicate, after):
	return Checkbox(on_change, tk_master, json_data, on_duplicate, after)


if __name__ == '__main__':
	import json

	json_rtn = json.loads('''
		{
			"type": "toggle",
			"description": "-A  显示全部",
			"value": "-A"
		}
	''')

	import tkinter as tk

	root = tk.Tk()
	frame = tk.Frame(root)

	check_box = create_checkbox(lambda: print('p: ' + str(check_box)), root, json_rtn)

	print(check_box.check())
	check_box.check(True)
	print(check_box.check())
	check_box.check(False)
	print(check_box.check())

	frame.mainloop()
