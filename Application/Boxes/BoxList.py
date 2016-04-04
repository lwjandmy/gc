from Application.Boxes.Checkbox import create_checkbox
from Application.Boxes.Setbox import create_setbox
from Application.Boxes.Textbox import create_textbox
from Application.Boxes.Summarybox import create_summarybox
import copy


# 工厂方法
def create_box(type, on_change, tk_master, json_data, on_duplicate, after=None):
	if type == 'toggle':
		return create_checkbox(on_change, tk_master, json_data, on_duplicate, after)
	elif type == 'set':
		return create_setbox(on_change, tk_master, json_data, on_duplicate, after)
	elif type == 'text':
		return create_textbox(on_change, tk_master, json_data, on_duplicate, after)
	elif type == 'summary':
		return create_summarybox(on_change, tk_master, json_data, on_duplicate, after)
	else:
		pass


class BoxList:
	def __init__(self, on_change, tk_master, json_data):
		self.on_change = on_change  # 各box被更改时, 会调用的回调函数
		self.tk_master = tk_master  # 所有box的父窗口, tk的root窗口
		self.json_data = json_data  # json配置文件保存的内容, dict格式
		self.box_list = []  # 记录各种box的列表
		self.parse_config(json_data)  # 读取配置文件信息

	def parse_config(self, json_data):
		for json_box_data in json_data:
			self.box_list.append(create_box(json_box_data['type'], self.on_change, self.tk_master, json_box_data, self.on_duplicate))

	def __str__(self):
		strlist = []
		for box in self.box_list:
			str_box = str(box)
			if str_box != '':
				strlist.append(str(box))
				strlist.append(' ')
		return ''.join(strlist)

	def on_duplicate(self, child):
		# 注意这里after=child.frame
		self.box_list.append(create_box(child.json_data['type'], child.on_change, child.tk_master, child.json_data, self.on_duplicate, after=child.frame))


def create_boxlist(on_change, tk_master, json_data):
	return BoxList(on_change, tk_master, json_data)


if __name__ == '__main__':
	import json

	json_rtn = json.loads('''
		[
			{
				"type": "summary",
				"description": "ps 显示进程"
			},
			{
				"type": "toggle",
				"description": "-A  显示全部",
				"value": "-A"
			},
			{
				"type": "set",
				"description": "--append string  加入一些字符串",
				"value": "--append"
			},
			{
				"type": "text",
				"description": "string  加入一些字符串"
			}
		]
	''')

	import tkinter as tk

	root = tk.Tk()
	frame = tk.Frame(root)

	box_list = create_boxlist(lambda: print(str(box_list)), root, json_rtn)

	frame.mainloop()
