"""
    功能：空气质量指数
    作者：Allen
    版本：7.0
    说明：v7.0 获取城市列表，自动获取所有城市数据
    日期：2019/04/07
"""
import requests
from bs4 import BeautifulSoup


def request_url(url):
    """
        获取url的请求结果
    """
    r = requests.get(url, timeout=30)
    return r.text


def city_aqi(city):
    """
        根据城市拼音获取AQI
    """
    url = "http://www.pm25.com/city/{}.html".format(city)
    url_result = request_url(url)
    soup = BeautifulSoup(url_result, 'lxml')
    # 解析
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


def get_all_cities():
    """
        获取所有城市
    """
    url = "http://www.pm25.com/rank.html"
    result = request_url(url)
    soap = BeautifulSoup(result, 'lxml')
    # Parse the cities
    city_list = []
    a_list = soap.find_all('a', class_="pjadt_location")
    for a in a_list:
        city_name = a.text.strip()
        city_alias = a['href']
        city_alias = city_alias[6:len(city_alias) - 5]
        city_list.append((city_name, city_alias))
    # Return result
    return city_list


def main():
    """
        主函数
    """
    city_list = get_all_cities()

    print("start")
    for city in city_list:
        city_name, city_alias = city
        print(city_name, city_aqi(city_alias))
    print("done")


if __name__ == '__main__':
    main()
