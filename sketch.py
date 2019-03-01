#coding:utf-8
import requests
import os
import sys
from lxml import etree
import time
import smtplib  #加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
import random
from util import util
import re
import json

from util.logger import logger
from util.logger import lg

#2019-2-21 16:45:37 非空校验

# d = {"a":"a","b":"b"}
d = {"a":"a","b":"b","d":None}
# d = {"a":"a","b":"b","d":"d"}
print(d)
print(d["a"])
if not d.has_key("d"):
    d["d"] = "e"
if not d["d"]:
    d["d"] = "f"

print(d["d"])


x = None
if x != None:
    print("not x")
else:
    print(x)

#2019-2-21 16:45:37 非空校验

#2019-1-17 10:49:05 for循环
# # for i in range(10):
#     # logger.info(i)

# # for i in range(10,5):
# #     logger.info(i)

# arr = [0,1,2,3,4,5,6,7,8,9]

# # for i in range(len(arr)):
# i = 0
# while i < len(arr):
#     lg(arr[i])

#     if arr[i] % 3 == 0:
#         del(arr[i])
#     else:


#         i=i+1

# lg(arr)
#2019-1-17 10:49:05 for循环

#2019-1-16 10:32:10 测试loadjson
# f = open("thread_analyzed.json")
# j = f.read()

# # logger.info(j)

# p = json.loads(j)

# # logger.info(p)

# for k1,v1 in p.items():
#     # logger.info("k1")
#     # logger.info(k1)
#     # logger.info("v1")
#     # logger.info(v1)

#     for v2 in v1:
#         logger.info(v2["time"])
#         logger.info("threads")
#         for v3 in v2["threads"]:
#             for k4,v4 in v3.items():
#                 logger.info("%s : %s"%(k4,v4))

# f.close()
#2019-1-16 10:32:10 测试loadjson

#2019-01-15-215047 测试对象
# data = {"a":"a","b":[]}
# b = data["b"]

# for i in range(10):
#     # data["b"].append(i)
#     b.append(i)


# logger.info(data)


# b = []

# for i in range(0,5):
#     b.append(i)

# logger.info(data)
# logger.info(b)
#2019-01-15-215047 测试对象




#2019-1-15 21:40:47 测试search
# str1 = "01-09 21:02:24.690 28860-29062/com.tencent.karaoke:service I/leonzhong: test log"

# if "test log" in str1:
#     logger.info("in")
# else:
#     logger.info("not in")

# logger.info(str1[:14])
#2019-1-15 21:40:47 测试search


#2019-1-7 20:55:20  测试正则
# pattern = r'(?<=\/).*(?=\))'
# pattern2 = r'(?<=\: ).*(?=\<)'

# str_ori = 'commit 5a2ae6dade8bfc2da2e93bcc10b030caeb66486a (origin/6.0_bugfix_eddy)'
# str_ori2 = 'Author: eddyyuan <eddyyuan@tencent.com>'

# str_des = re.search(pattern,str_ori,flags=0)
# str_des2 = re.search(pattern2,str_ori2,flags=0).group()

# print(str_des.group())
# print(str_des2)
# # print(str_des[0])
#2019-1-7 20:55:20  测试正则



#2019-1-15 21:59:53 测试正则
# pattern = r'(?<=name = ).*$'
# str_ori = "01-09 21:02:24.699 28860-29062/com.tencent.karaoke:service I/leonzhong: name = ReferenceQueueDaemon"
# str_des = re.search(pattern,str_ori,flags=0)

# logger.info(str_des.group())
#2019-1-15 21:59:53 测试正则


# 测试random
# print(random.randint(0,999999))
# r = random.randint(0,999999)
# print(r)
# print(str(r).zfill(6))

# for i in range(0,10):
#     print(i)
# 测试random


# 测试replace
# str1 = 'src\\a\\bb\\cc'
# str2 = str1.replace('\\','/')

# print(str2)
# 测试replace