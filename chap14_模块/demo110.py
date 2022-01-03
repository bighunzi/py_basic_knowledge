"""
作者：Big_hunzi
日期：2021年11月12日   12:15

主题：第三方模块的安装与使用
"""
import schedule
import time

def job():
    print('哈哈--------')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)