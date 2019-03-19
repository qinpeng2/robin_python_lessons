"""
    功能：52周存钱挑战
    版本：1.0
    作者：Allen
    日期：2019-03-18
"""


def main():
    i = 1                        # 当前周
    money_per_week = 10          # 每周存入
    increase_money = 10          # 递增的金额
    total_week = 52              # 总周数
    saving = 0                   # 账户统计

    while i <= total_week:
        saving += money_per_week*i

        #输出信息
        print('第({})周, 存入({})元, 账户累计({})元'.format(i, money_per_week*i, saving))

        i+=1


if __name__ == '__main__':
    main()

