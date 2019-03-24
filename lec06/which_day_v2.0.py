"""
    作者：Allen
    版本：2.0
    日期：2019/03/24
    功能：输入某年某月某日，判断这一天是这一年的第几天？
    重点：list
         -- 用列表代替元祖
         -- 提取判断是否为闰年的方法
"""

from datetime import datetime


def is_leap_year(year):
    """
    判断是否是闰年
    """
    is_leap = False
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        is_leap = True
    return is_leap


def main():
    """
    主函数
    """
    input_date_str = input("请输入日期(yyyy/mm/dd): ")
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')
    print(input_date)

    year = input_date.year
    month = input_date.month
    day = input_date.day

    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 判断闰年
    if is_leap_year(year):
        days_in_month_list[1] = 29

    days = sum(days_in_month_list[:month - 1]) + day

    print('这是第{}天。'.format(days))


if __name__ == "__main__":
    main()

