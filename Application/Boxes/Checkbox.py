import tkinter as tk


# @description: Checkbox的辅助函数
# @return: IntVar()
def add_checkbox(master, text, on_change):
	var = tk.IntVar()
	cbtn = tk.Checkbutton(master)
	cbtn["text"] = text
	cbtn["variable"] = var
	cbtn["command"] = on_change
	cbtn.pack()
	return var


class Checkbox:
	def __init__(self, on_change, tk_master, json_data):
		self.on_change = on_change  # 改变时的回调函数
		self.tk_master = tk_master  # 此checkbox属于的root窗口
		self.json_data = json_data  # json中保存的数据, dict结构
		self.var = add_checkbox(self.tk_master, self.json_data['description'],
				self.on_change)  # IntVar(), 可获取checkbox是否打勾

	def __str__(self):
		if (self.check()):
			return self.json_data['value']
		else:
			return ''

	# check() 获取是否打勾; check(True/False) 设置/去掉钩
	def check(self, b=None):
		if b != None:
			self.var.set(b)
			self.on_change()
		else:
			return self.var.get() == 1



# 工厂方法
def create_checkbox(on_change, tk_master, json_data):
	return Checkbox(on_change, tk_master, json_data)


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
