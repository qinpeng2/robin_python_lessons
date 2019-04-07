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


def city_aqi(city):
    """
        根据城市拼音获取AQI
    """
    url = "http://pm25.in/{}".format(city)
    url_result = requests.get(url, timeout=30).text
    soup = BeautifulSoup(url_result, 'lxml')
    # 解析
    div_list = soup.find_all('div', class_='span1')
    city_aqi_list = {}
    for i in range(len(div_list) - 1):
        div_content = div_list[i]
        caption = div_content.find('div', class_="caption").text.strip()
        value = div_content.find('div', class_="value").text.strip()
        # 构建数据到元祖中
        city_aqi_list[caption] = value

    return city_aqi_list


def get_all_cities():
    """
        获取所有城市
    """
    url = "http://www.pm25.in/"
    result = requests.get(url, timeout=30).text
    soap = BeautifulSoup(result, 'lxml')
    # Parse the cities
    city_div = soap.find('div', class_="bottom")
    city_links = city_div.find_all('a')
    city_list = []

    for link in city_links:
        city_name = link.text.strip()
        city_alias = link['href'][1:]
        city_list.append((city_name, city_alias))
    # Return result
    return city_list


def main():
    """
        主函数
    """
    city_list = get_all_cities()

    header = ['City', 'AQI', 'PM2.5/1h', 'PM10/1h', 'CO/1h', 'NO2/1h', 'O3/1h', 'O3/8h', 'SO2/1h']

    with open('output_data/v8.0_pm25in_city_aqi.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i, city in enumerate(city_list):
            city_name, city_alias = city
            city_row = [city_name] + list(city_aqi(city_alias).values())
            writer.writerow(city_row)


if __name__ == '__main__':
    main()
