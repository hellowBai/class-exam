# !/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *  # 导入 Tkinter 库

root = Tk()
language = ['C', 'python', 'php', 'html', 'SQL', 'java']
listb = Listbox(root)  # 创建两个列表组件
for item in language:  # 第一个小部件插入数据
    listb.insert(0, item)
listb.pack()  # 将小部件放置到主窗口中

root.mainloop()  # 进入消息循环
