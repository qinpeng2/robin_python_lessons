"""
    作者：Allen
    版本：3.0
    日期：2019/03/24
    功能：输入某年某月某日，判断这一天是这一年的第几天？
    重点：set
         -- 将月份划分为不同的集合再操作
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

    _30_days_month_set = {4, 6, 9, 11}
    _31_days_month_set = {1, 3, 5, 7, 8, 10, 12}

    days = day

    for i in range(1, month):
        if i in _30_days_month_set:
            days += 30
        elif i in _31_days_month_set:
            days += 31
        else:
            # 判断闰年
            if is_leap_year(year):
                days += 29
            else:
                days += 28

    print('这是第{}天。'.format(days))


if __name__ == "__main__":
    main()

