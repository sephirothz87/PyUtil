#-*-coding:utf-8-*-
from __future__ import print_function
import codecs
from util.logger import logger

# f = open("thread.txt",'r',encoding="utf-8")

# # 没用
# # content=f.read().decode('utf-8').encode('utf-8')
# # logger.info(content)

# # line = f.readline()
# line = f.readline().decode("utf-8", errors='ignore').encode("utf-8")
# # line = f.readline().decode("gbk", errors='ignore').encode("utf-8")

# for i in range(0,20):
# # while line:
#     l = line
#     l = line.decode('utf-8').encode('utf-8')
#     # l = line.decode('gb2312').encode('gb2312')
#     # logger.info(line)
    
#     # print(l)
#     # logger.info(l)

#     # line = f.readline()
#     line = f.readline().decode("utf-8", errors='ignore').encode("utf-8")
#     # line = f.readline().decode("gbk", errors='ignore').encode("utf-8")

# f.close()

with codecs.open("thread.txt",'r',encoding="utf-8") as f:
    cnt = 0
    for line in f:
        logger.info(line)
        cnt=cnt+1
        if cnt>100:
            break

    # for i in range(0,10):
    #     logger.info(f[i])