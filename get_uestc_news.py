# coding:utf-8
import requests
from bs4 import BeautifulSoup
import re


def get_clicks(news_href):  # 获取点击量的子函数
    son_text = requests.get(news_href).text  # 获取子页面源码
    click = re.findall('\d+(?= *</span>)', son_text)[0]  # 得到点击量数据
    return click


outfile = './news_clicks.csv'
open(outfile, 'w').close()  # 将输出文件清空
url = 'http://www.uestc.edu.cn/'
res = requests.get(url)  # 使用requests获取网页
text = res.text  # 获取网页源码
soup = BeautifulSoup(text, 'lxml')  # 创建Beautifulsoup对象
newsblock = soup.find('div', class_='news-block')  # 找到新闻模块
# print newsblock
news = newsblock.ul.find_all('a')  # 找到新闻模块中的<ul>标签，再找到其下的<a>标签
for new in news:  # 对于找到的所有<a>进行处理
    # print new
    title = new.contents[0].strip()  # 去掉空格后的标题
    href = new['href']  # 得到新闻的网址
    click = get_clicks(href)  # 进入子函数，获取点击量
    print title, click  # 打印标题和点击量
    f = open(outfile, 'a')  # 以add方式打开输出文件
    f.write(title.encode('GBK') + ',' + str(click) + '\n')  # 输出需要的字符串
    f.close()  # 关闭输出文件
