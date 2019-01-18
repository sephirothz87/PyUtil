#coding:utf-8
import difflib
import Levenshtein


# seq = difflib.SequenceMatcher(None,str1,str2)
# ratio = seq.ratio()
# sim = Levenshtein.distance(str1, str2)

# print(ratio)
# print(sim)

# seq = difflib.SequenceMatcher(None,str1,str3)
# ratio = seq.ratio()
# sim = Levenshtein.distance(str1, str3)
# print(ratio)
# print(sim)


def doCompare(str1,str2):
    print(u"%s - %s 相似度计算"%(str1,str2))

    seq = difflib.SequenceMatcher(None,str1,str2)
    ratio = seq.ratio()

    # 相似度，最大是1
    # print(u"difflib 相似度")
    print((u"difflib 相似度：%s"%ratio))#可以
    # print(u"difflib 相似度："+str(ratio))#可以

    #编辑距离，越小越好，但无法体现长字符串的的相似情况
    sim = Levenshtein.distance(str1, str2)
    print(u"Levenshtein 编辑距离：%s"%sim)

    #测试与diff相同
    levenRatio = Levenshtein.ratio(str1,str2)
    print(u"Levenshtein 莱温斯坦比：%s"%levenRatio)

    #测试与diff相同
    sim = Levenshtein.seqratio(str1, str2)
    print(u"Levenshtein 相似率：%s"%sim)

    #越大越好，最大1
    jaro = Levenshtein.jaro(str1,str2)
    print(u"Levenshtein jaro距离：%s"%jaro)

    #越大越好，完全相同是1。出现很多次不完全相同，但结果还是1的情况
    #如果只是数字和符号的不同，会被认为是1
    jaroWinkler = Levenshtein.jaro_winkler(str1,str2)
    print(u"Levenshtein jaro_winkler距离：%s"%jaroWinkler)

    print("\n")


str1 = "thread-1"
str2 = "thread-2"
str3 = "hippy-1"
str4 = "hippy-2"
# doCompare(str1,str2)
# doCompare(str1,str3)


str5="KaraRecorder.RecordThread-1547039321216"
str6="KaraRecorder.ScheduleThread-1547039321061"
str7="KaraRecorder.EvaluateThread-1547039323866"
str8="KaraM4aPlayer-PlayThread-1547039321284"


# doCompare(str5,str5)
# doCompare(str5,str1)
# doCompare(str5,str6)
# doCompare(str5,str7)
# doCompare(str5,str8)


# 这里会计算一个类似于公共字符串的东西出来，以下几种情况都可能会出现
# print(Levenshtein.median([str1,str2]))#thread-1 是其中一个字符串的值
# print(Levenshtein.median([str1,str2,str3,str4]))#hhiead  是一个新造出来的值
# print(Levenshtein.median([str1,str2,str3,str4,str5,str6,str7,str8]))#KaraRea    是一部分最相似的字符串的公共部分

#这个方法看不出来有什么意义，结果都是thread-1
# print(Levenshtein.setmedian([str1,str2]))
# print(Levenshtein.setmedian([str1,str2,str3,str4]))
# print(Levenshtein.setmedian([str1,str2,str3,str4,str5,str6,str7,str8]))



# print(Levenshtein.quickmedian([str1,str2]))#thread-1
# print(Levenshtein.quickmedian([str1,str2,str3,str4]))#hippy-1
# print(Levenshtein.quickmedian([str1,str2,str3,str4,str5,str6,str7,str8]))#KrReodr.reaeTrad14733226


print(Levenshtein.matching_blocks([str1,str2]))
print(Levenshtein.matching_blocks([str1,str2,str3,str4]))
print(Levenshtein.matching_blocks([str1,str2,str3,str4,str5,str6,str7,str8]))






