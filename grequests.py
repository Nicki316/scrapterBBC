import grequests
from bs4 import BeautifulSoup
import time 
import urllib3
urllib3.disable_warnings()

startime = time.time()

links = [f'https://www.bbc.com/zhongwen/trad/topics/c32p4kj2yzqt/page/{page}' for page in range(1,4)]

reqs = (grequests.get(link) for link in links)
resps = grequests.imap(reqs, grequests.Pool(3))

for index, resp in enumerate(resps):
    soup = BeautifulSoup(resp.text,'lxml')
    titles = soup.find_all(
        'span',{'class':"lx-stream-post__header-text gs-u-align-middle"}
    )

    titlelist = []
    for title in titles:
        titlelist.append(title.getText())
        
    
    urls = soup.find_all('a', {'class': 'qa-heading-link lx-stream-post__header-link'})
    sublinks = ['https://www.bbc.com'+ url.get('href') for url in urls]
    subreqs = (grequests.get(sublink) for sublink in sublinks)
    subresps = grequests.imap(subreqs, grequests.Pool(10)) 

    taglist = []
    for subresp in subresps:
        sub_soup = BeautifulSoup(subresp.text,'lxml')
        tags = sub_soup.find_all('li',{'class':'bbc-1msyfg1 e1hq59l0'})
        for tag in tags:
            taglist.append(tag.getText())
    
    print(f"第{index+1}頁")
    print(titlelist)
    print(taglist)

endtime = time.time()
print(f"花費{endtime - startime}秒")    