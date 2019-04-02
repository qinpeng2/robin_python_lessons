"""
    功能：掷骰子
    作者：Allen
    版本：1.0
    说明：v1.0 投掷一个骰子，并统计结果
         v2.0 投掷两个个骰子，并统计结果与概率
         v3.0 可视化投掷两个骰子的结果
         v4.0 直方图可视化结果
         v5.0 科学计算，numpy
    功能：matplotlib中文
    日期：2019/03/30
"""
import matplotlib.pyplot as plt
import numpy as np


def main():

    """
        Main Function
    """
    total_times = 10000

    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)

    print(roll1_arr)
    print(roll2_arr)
    result_arr = roll1_arr + roll2_arr
    print(result_arr)

    plt.hist(result_arr, bins=range(2, 14), normed=1, edgecolor='black', linewidth=1, rwidth=0.8)

    # diagram setting
    tick_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    tick_pos = np.arange(2, 13) + 0.5

    plt.xticks(tick_pos, tick_labels)

    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('概率')
    plt.show()


if __name__ == "__main__":
    main()

