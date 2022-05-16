import requests
from bs4 import BeautifulSoup
import time 
import urllib3
urllib3.disable_warnings()
import concurrent.futures

def scrape(links):
        response = requests.get(links)
        soup = BeautifulSoup(response.text,'lxml')
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
        
        
        print(titlelist)
        print(taglist)

startime = time.time()
links = [f'https://www.bbc.com/zhongwen/trad/topics/c32p4kj2yzqt/page/{page}' for page in range (1,4)]
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(scrape, links)

endtime = time.time()
print (f'花費{endtime - startime}')