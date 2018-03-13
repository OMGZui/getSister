# 包
from urllib import request
from bs4 import BeautifulSoup
import pymysql
import time

start = time.time()


# 转义函数
def transfer_content(content):
    if content is None:
        return None
    else:
        string = ""
        for c in content:
            if c == '"':
                string += '\\\"'
            elif c == "'":
                string += "\\\'"
            elif c == "\\":
                string += "\\\\"
            else:
                string += c
        return string


# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "spider", use_unicode=True, charset="utf8")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

for i in range(10):
    # 爬取网页
    page = i * 25
    url = r"https://movie.douban.com/top250?start=%d&filter=" % page
    with request.urlopen(url) as f:
        html_top = f.read().decode('utf-8')

    # 解析网页
    soup = BeautifulSoup(html_top, 'html.parser')
    lists = soup.find_all('div', class_='item')

    # 存入list
    item_list = list()
    for item in lists:
        img = item.img.get('src')
        hd = item.find('div', class_='hd')
        title = transfer_content(hd.a.find_all('span')[0].string)
        link = hd.a.get('href')

        bd = item.find('div', class_='bd')
        rate = bd.div.find_all('span')[1].string
        num = bd.div.find_all('span')[3].string
        num = num[0:-3]
        quote = transfer_content(bd.find_all('p')[1].span.string)

        # SQL 插入语句
        sql = " insert into top_250 (`title`, `link`, `img`, `rate`, `num`, `quote`) values " \
              "('%s', '%s', '%s', '%s', '%s', '%s')" % \
              (title, link, img, rate, num, quote)
        cursor.execute(sql)
        db.commit()
        print("正在存入第%d页--《%s》" % (i + 1, title))

# 关闭数据库连接
db.close()
end = time.time()

s = end - start
print("总共花费%.2f秒" % s)
