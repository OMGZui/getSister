# url = 'https://www.pornhub.com/video?c=111'

from urllib import request
from bs4 import BeautifulSoup

with request.urlopen('http://www.slb2.com/') as f:
    data = f.read().decode('utf-8')

soup = BeautifulSoup(data, 'html.parser')

lists = soup.find('div', class_='list-videos').find_all('a')

# 拿到全部的url
item_list = list()
for item in lists:
    # item_dict = dict()
    # item_dict['url'] = item['href']
    item_list.append(item['href'])
print(item_list)
