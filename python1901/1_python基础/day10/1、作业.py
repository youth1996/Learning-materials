#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
'''
1.设计出一个模块，这个模块包含求和（1+...+n），偶数和，奇数和,
以及任意的倍数之和的功能。
2.获取当前时间，并且返回当前时间的下一秒
3.分别使用递归与循环计算出遍历目录，并且比较两个程序的运算速度。
'''

import day10.qiuhe as qiuhe
import time

time1 = time.time()
tupletime = time.localtime(time1)
strtime = time.strftime("%X",tupletime)
print(strtime)
time1 = time1 + 1
tupletime = time.localtime(time1)
strtime = time.strftime("%X",tupletime)
print(strtime)

# print(qiuhe.func1(100))
# print(qiuhe.jisu(100))
# print(qiuhe.beihe(100,2))