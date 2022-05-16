import requests
from bs4 import BeautifulSoup

headers = {'user-agnet':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15'}

try:
    response = requests.get('https://www.bbc.com/zhongwen/trad/topics/c32p4kj2yzqt',
                headers = headers, timeout = 10)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.find('span', {'class': 'lx-stream-post__header-text gs-u-align-middle'})

        if title:
            result = title.getText()
            print (result)
        else:
            print("None")
    else:
        print('No 200')
except Exception as e:
    print(str(e))