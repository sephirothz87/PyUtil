#-*-coding:utf-8-*-
from __future__ import print_function
import codecs
from util.logger import logger
import re

# f = open("thread.txt","r",encoding="utf-8")

# # 没用
# # content=f.read().decode("utf-8").encode("utf-8")
# # logger.info(content)

# # line = f.readline()
# line = f.readline().decode("utf-8", errors="ignore").encode("utf-8")
# # line = f.readline().decode("gbk", errors="ignore").encode("utf-8")

# for i in range(0,20):
# # while line:
#     l = line
#     l = line.decode("utf-8").encode("utf-8")
#     # l = line.decode("gb2312").encode("gb2312")
#     # logger.info(line)
    
#     # print(l)
#     # logger.info(l)

#     # line = f.readline()
#     line = f.readline().decode("utf-8", errors="ignore").encode("utf-8")
#     # line = f.readline().decode("gbk", errors="ignore").encode("utf-8")

# f.close()



#解析日志生成json
regThreadId = r"(?<=id = ).*$"
regThreadName = r"(?<=name = ).*$"

res=[]
# oneTimeData = {"time":"","threads":[]}
threads=[]
thread = {"id":"","name":""}
with codecs.open("thread.txt","r",encoding="utf-8") as f:
    cnt = 0
    for line in f:
        logger.info(line.strip())

        if "test log" in line:
            # oneTimeData = {"time":line[:14],"threads":[]}
            # res.append(oneTimeData)

            threads = []
            res.append({"time":line[:14],"threads":threads})

        if "name = " in line:
            thread = {"id":"","name":""}
            threads.append(thread)
            thread["name"] = re.search(regThreadName,line.strip(),flags=0).group()
            continue

        if "id = " in line:
            thread["id"] = re.search(regThreadId,line.strip(),flags=0).group()
            continue

        cnt=cnt+1
        # if cnt>100:
        #     break

logger.info(res)
#解析日志生成json