"""
    功能：掷骰子
    作者：Allen
    版本：1.0
    说明：v1.0 投掷一个骰子，并统计结果
"""
import random


def roll_dice():
    return random.choice(range(1, 7))


def main():

    roll_times = 10000
    result = [0] * 6

    for i in range(roll_times):
        result[roll_dice() - 1] += 1

    total_roll_times = 0
    for i, x in enumerate(result):
        print("投掷出{}的次数={}，概率={}".format(i+1, result[i], result[i]/roll_times))
        total_roll_times += result[i]

    print("投掷总次数为:{}".format(total_roll_times))


if __name__ == "__main__":
    main()
