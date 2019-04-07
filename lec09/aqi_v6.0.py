"""
    功能：空气质量指数
    作者：Allen
    版本：6.0
    说明：v6.0 BeautifulSoup 解析DOM
    日期：2019/04/06
"""
import requests
from bs4 import BeautifulSoup


def request_url(url):
    """
        获取url的请求结果
    """
    r = requests.get(url, timeout=30)
    return r.text


def parse_aqi(url_result):
    """
        从请求结果中解析出AQI
    """
    soup = BeautifulSoup(url_result, 'lxml')

    div_list = soup.find('div', class_='cbo_left').find_all('div')
    city_aqi = []
    for i in range(len(div_list)):
        div_content = div_list[i]
        a_list = div_content.find_all('a')
        # 构建数据到元祖中
        caption = a_list[0].text.strip()
        value = a_list[1].text.strip()
        city_aqi.append((caption, value))

    return city_aqi


def main():
    """
        主函数
    """
    city_name = input("请输入城市拼音:")

    url = "http://www.pm25.com/city/{}.html".format(city_name)

    url_result = request_url(url)

    aqi = parse_aqi(url_result)

    print('[{}]的空气质量为：{}'.format(city_name, aqi))


if __name__ == '__main__':
    main()
