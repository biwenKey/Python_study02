#!/usr/bin/env python
# -*- coding:utf-8 -*-

#有如下值集合 [11,22,33,44,55,66,77,88,99,90...]，将所有大于 66 的值保存至字典的第一个key中，将小于 66 的值保存至第二个key的值中。
# 即： {'k1': 大于66的所有值, 'k2': 小于66的所有值}
dic = {"k1":[],"k2":[]}

list = [11,22,33,44,55,66,77,88,99]
for i in list:
    if i < 66:
        dic["k1"].append(i)
    else:
        if i > 66:

            dic["k2"].append(i)

print(dic)
print(dic["k1"])
print(dic["k2"])


