import tkinter as tk


class Summarybox:
	def __init__(self, on_change, tk_master, json_data, on_duplicate, after):
		self.on_change = on_change  # 改变时的回调函数
		self.tk_master = tk_master  # 此textbox属于的root窗口
		self.json_data = json_data # 保存json配置数据, dict类型
		self.on_duplicate_parent = on_duplicate

		self.frame = tk.Frame(self.tk_master)

		self.label = tk.Label(self.frame)
		self.label["text"] = json_data['description']
		self.label.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)

		self.btn_duplicate = tk.Button(self.frame)
		self.btn_duplicate['text'] = "+"
		self.btn_duplicate['command'] = self.on_duplicate
		self.btn_duplicate.pack(side=tk.LEFT)

		self.frame.pack(expand=tk.YES, fill=tk.X, after=after)

	def __str__(self):
		return ''
		# return self.json_data['description']

	def on_duplicate(self):
		self.on_duplicate_parent(self)

def create_summarybox(on_change, tk_master, json_data, on_duplicate, after):
	return Summarybox(on_change, tk_master, json_data, on_duplicate, after)




if __name__ == '__main__':
	import json

	json_rtn = json.loads('''
		{
			"type": "summary",
			"description": "ps 显示进程"
		}
	''')

	import tkinter as tk

	root = tk.Tk()
	frame = tk.Frame(root)
	frame.pack()

	summary_box = create_summarybox(
		lambda: print(str(summary_box)),
		frame,
		json_rtn
	)


	frame.mainloop()
