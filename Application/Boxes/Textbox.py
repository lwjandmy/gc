import tkinter as tk



class Textbox:
	def __init__(self, on_change, tk_master, json_data, on_duplicate, after):
		self.on_change = on_change  # 改变时的回调函数
		self.tk_master = tk_master  # 此textbox属于的root窗口
		self.json_data = json_data # 保存json配置数据, dict类型
		self.on_duplicate_parent = on_duplicate

		self.frame = tk.Frame(self.tk_master)

		self.label = tk.Label(self.frame)
		self.label["text"] = self.json_data['description']
		self.label.pack(side=tk.LEFT)

		self.txt = tk.Text(self.frame)
		self.txt["height"] = 1
		# txt["state"] = "normal"  # "disabled"
		self.txt.tag_bind(tk.SEL, "Enter>", on_change)
		self.txt.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)

		self.btn_duplicate = tk.Button(self.frame)
		self.btn_duplicate['text'] = "+"
		self.btn_duplicate['command'] = self.on_duplicate
		self.btn_duplicate.pack(side=tk.LEFT)

		self.frame.pack(expand=tk.YES, fill=tk.X, after=after)

	def __str__(self):
		return self.text()

	def text(self, str=None):
		if str is not None:
			self.txt.delete(1.0, tk.END)
			self.txt.insert(tk.END, str)
		else:
			return self.txt.get(1.0, tk.END)[:-1]


	def on_duplicate(self):
		self.on_duplicate_parent(self)

def create_textbox(on_change, tk_master, json_data, on_duplicate, after):
	return Textbox(on_change, tk_master, json_data, on_duplicate, after)



if __name__ == '__main__':
	import json

	json_rtn = json.loads('''
		{
			"type": "text",
			"description": "string  加入一些字符串"
		}
	''')

	import tkinter as tk

	root = tk.Tk()
	frame = tk.Frame(root)
	frame.pack()

	text_box = create_textbox(lambda: 'p: ' + print(str(text_box)), frame, json_rtn)
	print(text_box.text())
	text_box.text("hello, world")
	print('print: ' + text_box.text())
	text_box.text("")
	print('print: ' + str(text_box))


	frame.mainloop()
