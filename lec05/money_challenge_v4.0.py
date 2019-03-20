"""
    功能：52周存钱挑战
    版本：4.0
    作者：Allen
    日期：2019-03-20
    Focus: input, convert, function
"""
import math


def save_money(money_per_week, increase_money, total_week):
    money_list = []

    for i in range(total_week):
        money_list.append(money_per_week)
        money_per_week += increase_money
    return money_list


def main():
    total_week = int(input("总周数:"))  # 总周数
    money_per_week = float(input("每周存入:"))  # 每周存入
    increase_money = float(input("递增的金额:"))  # 递增的金额

    money_list = save_money(money_per_week, increase_money, total_week)
    saving = math.fsum(money_list)
    # 输出信息
    print('共({})周, 账户累计({})元'.format(total_week, saving))


if __name__ == '__main__':
    main()
