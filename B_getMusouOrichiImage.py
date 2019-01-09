import requests
import os
import sys
from lxml import etree
import time
from util import util

#下载无双大蛇所有图片
for i in range(171):
    # print(i)
    print('%03d' % i)
    s = '%03d' % i
    html = requests.get('https://www.gamecity.ne.jp/orochi3/img/character/chara_'+s+'_z.png', verify=False)#verify=False可以避免证书问题
    with open('t1_dimage/'+s+'_z.png', 'wb') as file:
        file.write(html.content)
    html = requests.get('https://www.gamecity.ne.jp/orochi3/img/character/chara_'+s+'_w.png', verify=False)
    with open('t1_dimage/'+s+'_w.png', 'wb') as file:
        file.write(html.content)