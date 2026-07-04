"""
    功能：空气质量指数
    作者：Allen
    版本：8.0
    说明：v8.0 获取城市列表，自动获取所有城市数据，写入CSV文件
         切换为原课程中的pm25.in的站点，不再使用pm25.com
    日期：2019/04/07
"""
import requests
import csv
from bs4 import BeautifulSoup


def query_followers():
    """
        根据城市拼音获取AQI
    """
    up_id = 3829313
    offset = 1
    limit = 20
    direction = 'desc'

    headers = {
        'User-Agent':
            ''
    }

    url = "https://api.bilibili.com/x/relation/followers?vmid=3829313&pn=1&ps=20&order=desc&jsonp=jsonp&callback=__jp11"\
        .format(up_id, offset, limit, direction)
    url_result = requests.get(url, timeout=30).text
    # soup = BeautifulSoup(url_result, 'lxml')
    # # 解析
    # div_list = soup.find_all('div', class_='span1')
    # city_aqi_list = {}
    # for i in range(len(div_list) - 1):
    #     div_content = div_list[i]
    #     caption = div_content.find('div', class_="caption").text.strip()
    #     value = div_content.find('div', class_="value").text.strip()
    #     # 构建数据到元祖中
    #     city_aqi_list[caption] = value
    print(url_result)
    return ''


def main():
    """
        主函数
    """
    query_followers()


if __name__ == '__main__':
    main()
