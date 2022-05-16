import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

res = requests.get('https://www.bbc.com/zhongwen/trad/topics/c32p4kj2yzqt', verify=False)
#print(res.text.find())

soup = BeautifulSoup(res.text,'lxml')
titles = soup.find_all(
    'span',{'class':"lx-stream-post__header-text gs-u-align-middle"}
)

titlelist = []
for title in titles:
    titlelist.append(title.getText())
    
taglist = []
urls = soup.find_all('a', {'class': 'qa-heading-link lx-stream-post__header-link'})
for url in urls:
    sub_response = requests.get('https://www.bbc.com'+ url.get('href'), verify = False)
    sub_soup = BeautifulSoup(sub_response.text,'lxml')
    tags = sub_soup.find_all('li',{'class':'bbc-1msyfg1 e1hq59l0'})
    for tag in tags:
        taglist.append(tag.getText())

print(taglist)