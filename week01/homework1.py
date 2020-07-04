import requests
import lxml.etree
from scrapy.selector import Selector

# 爬取页面详细信息
requests.get('https://maoyan.com')

# 电影详细页面
url = 'https://maoyan.com/films?showType=3'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

# 声明为字典使用字典的语法赋值
Accept = '*/*'
ae = 'gzip, deflate, br'
al = 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6,ja;q=0.5'
Connection = 'keep-alive'
cl = '783'
ct = 'application/x-www-form-urlencoded'
Host = 'catfront.dianping.com'
Origin = 'https://maoyan.com'
Referer = 'https://maoyan.com/films?showType=3'
sfd = 'empty'
sfm = 'cors'
sfs = 'cross-site'



header = {}
header['user-agent'] = user_agent
header['Accept'] = Accept
header['Accept-Encoding'] = ae
header['Accept-Language'] = al
header['Connection'] = Connection
header['Content-Length'] = cl
header['Content-Type'] = ct
header['Host'] = Host
header['Origin'] = Origin
header['Referer'] = Referer
header['Sec-Fetch-Dest'] = sfd
header['Sec-Fetch-Mode'] = sfm
header['Sec-Fetch-Site'] = sfs


response = requests.get(url, headers=header)
response.encoding='utf-8'
print(response.text)
#f=open("/Users/dean/Desktop/1.htm").read()
#print(f)
# xml化处理
selector = lxml.etree.HTML(response.text)
film_name = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[2]/div[1]/div[2]/a/div/div[1]/span[1]')
#film_name = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[2]/div[1]/div[2]/a/div/div[1]/span[1]/text()')[0]
print(film_name)
for i in range(1,11,1):
    # 电影名称
    film_name = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[{}]/div[1]/div[2]/a/div/div[1]/span[1]/text()'.format(i))
    print(f'电影名称: {film_name}')

    # 上映日期
    plan_date = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[{}]/div[1]/div[2]/a/div/div[4]/text()'.format(i))
    print(f'上映日期: {plan_date}')

    # 类型
    film_type = selector.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd[{}]/div[1]/div[2]/a/div/div[2]/text()'.format(i))
    print(f'类型：{film_type}')

    mylist=[]
    mylist.append(film_name)
    mylist.append(film_type)
    mylist.append(plan_date)


import pandas as pd

movie1 = pd.DataFrame(data = mylist)

# windows需要使用gbk字符集
movie1.to_csv('./movie1.csv', encoding='utf8', index=False, header=False)
