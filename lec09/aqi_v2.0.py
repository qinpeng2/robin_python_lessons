"""
    功能：空气质量指数
    作者：Allen
    版本：2.0
    说明：v2.0 json操作
    日期：2019/04/06
"""
import json


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
    top5_list = city_list[:5]

    # 写入结果到
    f = open('output_data/v2.0_top5_aqi.json', mode='w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    main()
