#-*-coding:utf-8-*-
from __future__ import print_function
import codecs
from util.logger import logger
from util.logger import lg
import re
import json
import Levenshtein

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
# regThreadId = r"(?<=id = ).*$"
# regThreadName = r"(?<=name = ).*$"

# res=[]
# # oneTimeData = {"time":"","threads":[]}
# threads=[]
# thread = {"id":"","name":""}
# with codecs.open("thread.txt","r",encoding="utf-8") as f:
#     cnt = 0
#     for line in f:
#         logger.info(line.strip())

#         if "test log" in line:
#             # oneTimeData = {"time":line[:14],"threads":[]}
#             # res.append(oneTimeData)

#             threads = []
#             res.append({"time":line[:14],"threads":threads})

#         if "name = " in line:
#             thread = {"id":"","name":""}
#             threads.append(thread)
#             thread["name"] = re.search(regThreadName,line.strip(),flags=0).group()
#             continue

#         if "id = " in line:
#             thread["id"] = re.search(regThreadId,line.strip(),flags=0).group()
#             continue

#         cnt=cnt+1
#         # if cnt>100:
#         #     break

# logger.info(res)
#解析日志生成json


#解析json文件
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
#解析json文件

#解析json+计算相似度


#jaro = Levenshtein.jaro(str1,str2)
#Levenshtein.median([str1,str2,str3,str4,str5,str6,str7,str8])


f = open("thread_analyzed.json")
j = f.read()

p = json.loads(j)

f.close()

lastGroups = {}

for key,data in p.items():
    # logger.info("k1")
    # logger.info(k1)
    # logger.info("v1")
    # logger.info(v1)

    for otRes in data:
        lg(u"========================单次上报检测start========================")
        logger.info(otRes["time"])

        # logger.info("threads")
        # for thread in otRes["threads"]:
        #     logger.info("%s : %s"%(thread["id"],thread["name"]))

        # i=0
        # j=0
        # for i in range(len(otRes["threads"])-1):
        #     for j in range(i+1,len(otRes["threads"])):
        #         jaro = Levenshtein.jaro(otRes["threads"][i],otRes["threads"][j])
        #         logger.info("对比：%s - %s - 相似度：%s"%(otRes["threads"][i],otRes["threads"][j],jaro))

        #         if jaro > 0.85:

        i = 0
        threads = otRes["threads"]
        groups = {}
        while i < len(threads):
            group = []
            strGroup = []#用于快速统计字符串公共部分
            # lg(u"对比 - %s"%threads[i]["name"])
            j = i+1
            while j < len(threads):
                # base = threads[i]["name"]
                jaro = Levenshtein.jaro(threads[i]["name"],threads[j]["name"])
                # logger.info(u"对比：%s - %s - 相似度：%s"%(threads[i]["name"],threads[j]["name"],jaro))
                if jaro > 0.85:
                    if len(group) == 0:
                        # lg(u"第一次，两个值都加入group")
                        group.append({"name":threads[i]["name"],"id":threads[i]["id"]})
                        strGroup.append(threads[i]["name"])
                    group.append({"name":threads[j]["name"],"id":threads[j]["id"]})
                    strGroup.append(threads[j]["name"])
                    del(threads[j])
                else:
                    j=j+1#光标控制
            if len(group) == 0:
                # lg(u"group为空，下一次")
                i=i+1#光标控制
            else:
                del(threads[i])
                # lg(u"当前")
                # lg(group)
                # lg(u"共通分析：%s"%Levenshtein.median(strGroup))
                # lg(u"共通分析：%s"%Levenshtein.setmedian(strGroup))

                # lg(u"共通分析：%s"%Levenshtein.quickmedian(strGroup))
                key = Levenshtein.quickmedian(strGroup)
                # groups.append({key:group})
                groups[key] = group

                    
        lg(u"最终结果")
        lg(groups)
        lg(u"========================单次上报检测end========================")

        if len(lastGroups) > 0:
            for k,group in groups.items():
                if lastGroups.has_key(k):
                    lg("key = %s"%k)
                    if len(lastGroups[k]) != len(group):
                        lg(u"有变化")
                        lg(lastGroups[k])
                        lg(groups[k])
                    # else:
                        # lg(u"没有变化")
        lastGroups = groups



        #     lastGroups = groups





#解析json+计算相似度