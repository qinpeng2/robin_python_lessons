"""
    功能：掷骰子
    作者：Allen
    版本：1.0
    说明：v1.0 投掷一个骰子，并统计结果
         v2.0 投掷两个个骰子，并统计结果与概率
         v3.0 可视化投掷两个骰子的结果
         v4.0 直方图可视化结果
    功能：matplotlib中文
    日期：2019/03/30
"""
import random
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def roll_dice():
    return random.choice(range(1, 7))


def prepare_data():
    roll_times = 10000

    print(list(range(2, 14)))

    roll_list = []

    for i in range(roll_times):
        dice1 = roll_dice()
        dice2 = roll_dice()

        roll_list.append(dice1 + dice2)

    return roll_list


def main():
    data = prepare_data()
    plt.hist(data, bins=range(2, 14), normed=1, edgecolor='black', linewidth=1)
    plt.title('骰子点数统计直方图')
    plt.xlabel('两次点数')
    plt.ylabel('概率')
    plt.show()


if __name__ == "__main__":
    main()

