import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.bbc.com/zhongwen/trad/topics/c32p4kj2yzqt')
#print(res.text.find())

soup = BeautifulSoup(res.text,'lxml')
titles = soup.find_all(
    'span',{'class':"lx-stream-post__header-text gs-u-align-middle"}
)

titlelist = []
for title in titles:
    titlelist.append(title.getText())
    
print (titlelist)