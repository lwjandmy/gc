import tkinter as tk

# @description: Summarybox的辅助函数
def add_summarybox(master, text, on_change):
	label = tk.Label(master)
	label["text"] = text
	label.pack()
	return label

class Summarybox:
	def __init__(self, on_change, tk_master, json_data):
		self.on_change = on_change  # 改变时的回调函数
		self.tk_master = tk_master  # 此textbox属于的root窗口
		self.json_data = json_data # 保存json配置数据, dict类型
		self.label = add_summarybox(self.tk_master, json_data['description'], on_change)

	def __str__(self):
		return ''
		# return self.json_data['description']

def create_summarybox(on_change, tk_master, json_data):
	return Summarybox(on_change, tk_master, json_data)




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
