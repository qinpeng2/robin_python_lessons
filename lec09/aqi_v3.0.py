"""
    功能：空气质量指数
    作者：Allen
    版本：3.0
    说明：v3.0 json操作
    日期：2019/04/06
"""
import json
import csv


def process_json_file(file_path):
    """
        解析json文件
    """
    f = open(file_path, mode='r', encoding='utf-8')
    city_list = json.load(f)
    f.close()
    return city_list


def main():
    """
        主函数
    """
    file_path = input('请输入文件名(beijing_aqi.json, shanghai_aqi.json): ')
    city_list = process_json_file('input_data/' + file_path)
    city_list.sort(key=lambda city: city['aqi'])

    lines= [city_list[0].keys()]

    for city in city_list:
        lines.append(list(city.values()))

    # 写入结果到
    f = open('output_data/v3.0_city_aqi.csv', mode='w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()


if __name__ == '__main__':
    main()
