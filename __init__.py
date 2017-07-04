#coding: utf-8
# __init__.py
from spider import spider_robot

__all__ = ['os', 'sys', 're', 'urllib']


page_num = str(raw_input(u'Please input the page number：\n'))
spider_robot.timer(page_num)

