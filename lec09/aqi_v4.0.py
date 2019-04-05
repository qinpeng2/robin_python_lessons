"""
    功能：空气质量指数
    作者：Allen
    版本：4.0
    说明：v4.0 OS，with，json与csv文件的读取
    日期：2019/04/05
"""
import os
import json
import csv


def read_json_file(file_path):
    """
        解析json文件
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        data_list = json.load(f)
    print(data_list)


def read_csv_file(file_path):
    """
        解析csv文件
    """
    with open(file_path, mode='r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(",".join(row))


def main():
    """
        主函数
    """
    file_path = input("请输入文件名:")

    # 查看文件是否存在
    if not os.path.exists(file_path):
        print("对不起，文件不存在！")
        return

    # 获取文件名和文件后缀
    file_name, file_ext = os.path.splitext(file_path)

    if file_ext == '.json':
        read_json_file(file_path)
    elif file_ext == '.csv':
        read_csv_file(file_path)
    else:
        print('不支持的文件格式')


if __name__ == '__main__':
    main()
