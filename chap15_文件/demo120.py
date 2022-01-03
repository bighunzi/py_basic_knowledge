"""
作者：Big_hunzi
日期：2021年11月13日   20:56

主题：os.path模块的常用方法
"""
import os.path
print(os.path.abspath('demo113.py'))#用于获取文件或目录的绝对路径
print(os.path.exists('demo113.py'),os.path.exists('demo11111.py'))#用于判断文件或目录是否存在
print(os.path.join('D:\\pythonProject','demo113.py'))#将目录与目录或者文件名拼接起来
print(os.path.split('D:\\pythonProject\\vippython\\chap15_文件\\demo113.py'))#将目录与文件拆分
print(os.path.splitext('demo113.py'))#分离文件名和扩展名
print(os.path.basename('D:\\pythonProject\\vippython\\chap15_文件\\demo113.py'))#提取文件名
print(os.path.dirname('D:\\pythonProject\\vippython\\chap15_文件\\demo113.py'))#提取目录名
print(os.path.isdir('D:\\pythonProject\\vippython\\chap15_文件'))#判断是否是路径