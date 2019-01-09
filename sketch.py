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


#2019-1-7 20:55:20  测试正则
pattern = r'(?<=\/).*(?=\))'
pattern2 = r'(?<=\: ).*(?=\<)'

str_ori = 'commit 5a2ae6dade8bfc2da2e93bcc10b030caeb66486a (origin/6.0_bugfix_eddy)'
str_ori2 = 'Author: eddyyuan <eddyyuan@tencent.com>'

str_des = re.search(pattern,str_ori,flags=0)
str_des2 = re.search(pattern2,str_ori2,flags=0).group()

print(str_des.group())
print(str_des2)
# print(str_des[0])


#2019-1-7 20:55:20  测试正则

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