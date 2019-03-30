"""
    功能：掷骰子
    作者：Allen
    版本：1.0
    说明：v1.0 投掷一个骰子，并统计结果
         v2.0 投掷两个个骰子，并统计结果与概率
         v3.0 可视化投掷两个骰子的结果
    功能：
    日期：2019/03/29
"""
import random
import matplotlib.pyplot as plt


def roll_dice():
    return random.choice(range(1, 7))


def main():
    roll_times = 100
    roll_no = list(range(2, 13))
    roll_counter = [0] * 12

    dict_result = dict(zip(roll_no, roll_counter))

    print(roll_counter)

    dice1_list = []
    dice2_list = []

    for i in range(roll_times):
        dice1 = roll_dice()
        dice2 = roll_dice()

        dice1_list.append(dice1)
        dice2_list.append(dice2)

        dict_result[dice1 + dice2] += 1

    total_roll_times = 0
    for i, x in dict_result.items():
        print("投掷出{}的次数={}，概率={}".format(i, dict_result[i], dict_result[i] / roll_times))
        total_roll_times += dict_result[i]

    print("投掷总次数为:{}".format(total_roll_times))

    x = range(1, total_roll_times + 1)

    plt.scatter(x, dice1_list, c='red', alpha=0.5)
    plt.scatter(x, dice2_list, c='green', alpha=0.5)
    plt.show()


if __name__ == "__main__":
    main()
