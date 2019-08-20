# -*- coding: UTF-8 -*-
import requests

# 指定要抓取的網頁URL
url = "https://www.ptt.cc/bbs/hotboards.html"

r = requests.get(url)
web_content = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(web_content, 'lxml')
boardNameElements = soup.find_all('div', class_="board-name")

boardNames = [e.text for e in boardNameElements]
pupularityElements = soup.find_all('div', class_="board-nuser")
pupularities = [int(e.text) for e in pupularityElements]

print(len(boardNames), len(pupularities))

for bn, popu in zip(boardNames, pupularities):
    print(popu, bn)

import pandas as pd
from datetime import datetime
now = datetime.now()
curretdt = now.strftime("%Y-%m-%d %H:%M:%S")
df = pd.DataFrame(
{"boardNames" : boardNames,
 "pupularities" : pupularities,
 "timestamp" : [curretdt]*len(pupularities)
})
df.head()

import os
path = os.getcwd()
dt2 = now.strftime("%Y%m%d_v%H%M")
filename = os.path.join(path,'ppt_pop_{}.csv'.format(dt2))
df.to_csv(filename)
