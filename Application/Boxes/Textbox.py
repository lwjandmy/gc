import tkinter as tk


# @description: Textbox的辅助函数
def add_textbox(master, text, on_change):
	label = tk.Label(master)
	label["text"] = text
	label.pack()

	txt = tk.Text(master)
	txt["height"] = 1
	# txt["state"] = "normal"  # "disabled"
	txt.tag_bind(tk.SEL, "Enter>", on_change)
	txt.pack()

	return txt

class Textbox:
	def __init__(self, on_change, tk_master, json_data):
		self.on_change = on_change  # 改变时的回调函数
		self.tk_master = tk_master  # 此textbox属于的root窗口
		self.json_data = json_data # 保存json配置数据, dict类型
		self.txt = add_textbox(self.tk_master, self.json_data['description'], self.on_change)

	def __str__(self):
		return self.text()

	def text(self, str=None):
		if (str != None):
			self.txt.delete(1.0, tk.END)
			self.txt.insert(tk.END, str)
		else:
			return self.txt.get(1.0, tk.END)[:-1]

def create_textbox(on_change, tk_master, json_data):
	return Textbox(on_change, tk_master, json_data)



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
