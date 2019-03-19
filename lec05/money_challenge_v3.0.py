"""
    功能：52周存钱挑战
    版本：3.0
    作者：Allen
    日期：2019-03-18
    Focus: for, range
"""
import math


def main():
    money_per_week = 10  # 每周存入
    increase_money = 10  # 递增的金额
    total_week = 52  # 总周数

    money_list = []

    for i in range(total_week):
        seq = i + 1
        money_list.append(money_per_week * seq)
        saving = math.fsum(money_list)

        # 输出信息
        print('第({})周, 存入({})元, 账户累计({})元'.format(seq, money_list[i], saving))


if __name__ == '__main__':
    main()
