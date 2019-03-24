"""
    作者：Allen
    版本：5.0
    日期：2019/03/24
    功能：输入某年某月某日，判断这一天是这一年的第几天？
    重点：datetime库提供的格式化方法
"""

from datetime import datetime


def main():
    """
    主函数
    """
    input_date_str = input("请输入日期(yyyy/mm/dd): ")
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    print(input_date)

    print('这是第{}天。'.format(datetime.strftime(input_date, '%j')))


if __name__ == "__main__":
    main()

