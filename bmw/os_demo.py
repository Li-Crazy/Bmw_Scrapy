'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/6/8 17:08
@Software: PyCharm
@File    : os_demo.py
'''
import os
print(os.path.join(os.path.dirname(os.path.dirname(__file__)),'images'))
images_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
if not os.path.exists(images_path):
    print("文件夹不存在")
    os.mkdir(images_path)
else:
    print("文件夹存在")