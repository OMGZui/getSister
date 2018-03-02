# 爬取网页
from urllib import request
# 解析网页
from bs4 import BeautifulSoup
# 正则
import re
# 分词
import jieba
import pandas
# 统计
import numpy

with request.urlopen('https://movie.douban.com/nowplaying/hangzhou/') as f:
    data = f.read().decode('utf-8')
# print(html)

soup = BeautifulSoup(data, 'html.parser')
# print(soup.prettify())

lists = soup.find_all('li', class_='list-item')
# print(lists)

item_list = list()
for item in lists:
    item_dict = dict()
    item_dict['id'] = item['data-subject']
    item_dict['name'] = item.find('li', class_='stitle').find('a')['title']
    item_list.append(item_dict)

# print(item_list)

url = 'https://movie.douban.com/subject/' + item_list[0]['id'] + '/comments?status=P'

comment_list = list()
with request.urlopen(url) as f:
    war = f.read().decode('utf-8')
    war_soup = BeautifulSoup(war, 'html.parser')
    war_lists = war_soup.find_all('div', class_='comment')
    for war_item in war_lists:
        comment = war_item.find_all('p')[0].string
        if comment is not None:
            comment_list.append(comment)

# print(comment_list)

comments = str()
for k in range(len(comment_list)):
    comments = comments + (str(comment_list[k])).strip()

# print(comments)

pattern = re.compile(r'[\u4e00-\u9fa5]+')
filter_data = re.findall(pattern, comments)
cleaned_comments = ''.join(filter_data)

# print(cleaned_comments)

segment = jieba.lcut(cleaned_comments)
words_df = pandas.DataFrame({'segment': segment})

# print(words_df)

# quoting=3全不引用
stopwords = pandas.read_csv("stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                            encoding='utf-8')
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]

# print(words_df)

words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": numpy.size})
words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)

print(words_stat)
