"""
    作者：Allen
    版本：4.0
    日期：2019/03/24
    功能：输入某年某月某日，判断这一天是这一年的第几天？
    重点：dictionary
         -- 将月份及其对应天数通过字典表示
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

    month_day_dict = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    days = day

    for i in range(1, month):
        days += month_day_dict[i]
        if i == 2 and is_leap_year(year):
            days += 1

    print('这是第{}天。'.format(days))


if __name__ == "__main__":
    main()

