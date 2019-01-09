# coding=utf-8
# -*- coding: utf-8 -*-
import os
import re
import json

#
o = {'a':'a','b':'b','c':{'d':'d','e':'e'}}

v1 = o['a']
v2 = o['c']
v3 = o['c']['e']
print(v1)
print(v2)
print(v3)

o['a'] = 'aaa'
o['c']['e'] = 'eee'

print(v1)
print(v2)
print(v3)
#


#
# s = '1,2,3,4,{5,6,7,8},x,y,z,{aa,b,{3,4,5},cc,d},e,f,g,h'
#
# # r = r'{.+?,.+?}'
#
# # res = re.sub(r,'hahaha',s)
# # print(res)
#
# def rpComma(ss):
#     print(ss)
#     value = ss.group('value')
#     print(value)
#     return value.replace(',','\,')
#
#
# r = '(?P<value>{.+?,.+?})'
# res = re.sub(r,rpComma,s)
# print(res)
#

#
# o = {'z':'z','y':'y','a':'a','b':3,'c':[1,2,3],'d':False,'e':{'aa':'aa','bb':'bb'}}
# print(o.values())
# x = o.values()
# print(x)
#
# # print(''.join(x))
#
# # l = [1,2,3]
# l = ['a','b','c']
# print(l)
# # print(''.join(l))
# s = ''.join(l)
# print(s)
#
#
# t = (1,2,3)
# print(t)
# # str = '-'.join(t)
# # print(str)
#
#
# o2 = {'z':'z','y':'y','a':'a'}
# s = '-'.join(o2)
# print(s)
# l2 = o2.values()
# print(l2)
# s = '-'.join(l2)
# print(s)
#
# o3 = {'z':'z','y':'y','a':1}
# s = '-'.join(o3)
# print(s)
# l3 = o3.values()
# print(l3)
# # str = '-'.join(l3)
# # print(str)
# s = ','.join(map(str, l3))
# print(s)
#

#
# str1 = 'aaaa/aaabc/aaa/?xxxx=-1'
# str2 = 'aaaa/aaabc/aaa/?xxxx=-2'
# str3 = 'aaaa/aaabc/aaa/?xxxx=1'
# str4 = 'aaaa/aaabc/aaa/?xxxx=4'
#
# def f(str):
#     if str.rfind('-') > 0:
#         return str[len(str)-2:]
#     else:
#         return str[len(str)-1:]
#
# print(f(str1))
# print(f(str2))
# print(f(str3))
# print(f(str4))
#

#
# f = open('t1.txt','a')
#
# f.write('123')
# f.write('456')
# f.write('456')
#
# f.close()
#

#
# o = {'a':'a','b':3,'c':[1,2,3],'d':False,'e':{'aa':'aa','bb':'bb'}}
# print(json.dumps(o))
# print(o)
#

#
# o = {'a':'a','b':3,'c':[1,2,3],'d':False,'e':{'aa':'aa','bb':'bb'}}
# print(o)
#

#
# print('a','b',3,'c')
# print('a'+'b')
# print('a'+str(3))
#

#
# print(len('123'))
#

#
# def exChangeTime(str):
#     # reg = r'赛前(\d+)小时(\d+)分'
#     reg = r'\D*(\d+)\D+(\d+)\D+'
#     return re.sub(reg,r'\1:\2',str)
#
# print(exChangeTime('赛前187小时26分'))
# print(exChangeTime('赛前0小时15分'))
#