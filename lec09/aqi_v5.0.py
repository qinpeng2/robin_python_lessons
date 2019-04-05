"""
    功能：空气质量指数
    作者：Allen
    版本：5.0
    说明：v5.0 requests包，截取网页内容
    日期：2019/04/05
"""
import requests


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
    aqi_start_element = '''<a class="cbol_aqi_num" href="/news/385.html" target="_blank">'''
    aqi_end_element = '''</a>'''

    start_element_index = url_result.find(aqi_start_element)

    start_index = start_element_index + len(aqi_start_element)
    end_index = url_result.find(aqi_end_element, start_index)

    return url_result[start_index: end_index]


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
