#coding:utf-8
import os
import time
import datetime
import random

DEF_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
FIL_DATETIME_FORMAT = '%Y-%m-%d-%H-%M-%S'

def getDateTime():
    return datetime.datetime.now().strftime(DEF_DATETIME_FORMAT)

def getDateRandomFileName():
    return datetime.datetime.now().strftime(FIL_DATETIME_FORMAT)+'-'+str(random.randint(0,999999)).zfill(6)
