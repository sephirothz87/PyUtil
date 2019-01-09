# coding=utf-8
# -*- coding: utf-8 -*-
import os
import re

# dir = 'D:\\15_美剧\\The.Big.Bang.Theroy\\The.Big.Bang.Theory.S03.Season.3.Complete.720p.HDTV.x264-[maximersk]'
dir = 'D:\\12_电视剧\\琅琊榜之风起长林'

# start = 'The.Big.Bang.Theory.S03E'
# end = '.720p.HDTV.ReEnc-Max.srt'
start = '琅琊榜之风起长林'
end = '.1080p.mp4'



# pattern = r'H(.*)(\d{2}).1080p(.*)'
# pattern = r'(?i)The\.Big\.Bang\.Theory.S03E(\d{2})(.*).srt'
pattern = r'.*(\d{2}).1080p(.*).mp4'
replace = r'\1'


def listFile(dir, f_list):
    if (os.path.isfile(dir)):
        print('is dir return')
        return f_list
    else:
        for s in os.listdir(dir):
            print(s)
            f_dir = os.path.join(dir, s)
            if (os.path.isfile(f_dir)):
                f_list.append(f_dir)
    return f_list


print('start')
if (os.path.isfile(dir)):
    print('is file')
    print('quit')
    quit()

f_list = listFile(dir, [])

for f in f_list:
    rename = os.path.join(dir, re.sub(pattern, start + replace + end, f))
    if (f != rename):
        print(f)
        print(rename)
        # rename
        os.rename(f,rename)
