# coding:utf-8
import uuid
import requests
import unicodedata
from lxml import html
import douban_sql


def list_douban_top250():
    print("正在获取豆瓣TOP250影片信息并存入数据库......")
    movies = []
    index: int = 1
    page_count = 1
    for i in range(page_count):
        url = f'https://movie.douban.com/top250?start={i * 25}&filter='
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/90.0.4430.72 Safari/537.36 '
        }
        url_content = requests.get(url, headers=headers).content
        # 内容节点
        doc = html.fromstring(url_content)
        for y in doc.xpath('//div[@class="info"]'):
            # 影片名称
            name = y.xpath("div[@class=\"hd\"]/a/span[@class=\"title\"]/text()")[0]
            # 影片详情
            movie_content = y.xpath('div[@class="bd"]/p[1]/text()')
            content = ''.join(movie_content)
            # 导演演员信息
            actor = movie_content[0].replace(" ", "").replace("\n", "")
            # 上映日期
            date = movie_content[1].replace(" ", "").replace("\n", "").split("/")[0]
            # 制片国家
            country = movie_content[1].replace(" ", "").replace("\n", "").split("/")[1]
            # 影片类型
            types = movie_content[1].replace(" ", "").replace("\n", "").split("/")[2]
            # 评分
            rate = y.xpath('div[@class="bd"]/div[@class="star"]/span[2]/text()')[0]
            # 评论人数
            com_count = y.xpath('div[@class="bd"]/div[@class="star"]/span[4]/text()')[0]
            # 点开单个url找到简介
            # 单个url0
            url0 = y.xpath('div[@class="hd"]/a/@href')
            # 爬取简介
            url0_content = requests.get(url0[0], headers=headers).content
            doc0 = html.fromstring(url0_content)
            introduction = doc0.xpath('div[@class="article"]/div[@class="related-info"]/div[@class="indent"]/span['
                                      '2]/text()')
            quote = y.xpath('div[@class="bd"]/p[2]/span[1]/text()')
            # id
            movie_id = str(index)
            # 执行log
            print("TOP%s---%s---评分%s---人数%s" % (str(index), name, rate, com_count.replace('人评价', '')))
            movie = (movie_id, str(name), str(content), str(actor), str(date), str(country),
                     str(types), str(rate), str(com_count), str(quote), str(url0), str(introduction))

            # 加入数组
            index += 1
            movies.append(movie)
    douban_sql.insert_movies(movies)


# 调用函数
list_douban_top250()
