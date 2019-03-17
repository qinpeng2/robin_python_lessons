"""
    作者：Allen
    功能：BMR计算器
    版本：2.0
    日期：03/17/2019
"""


def main():
    """
        主函数
    """

    while True:

        gender = input('性别')
        weight = float(input('体重(kg)'))
        height = float(input('身高(cm)'))
        age = int(input('年龄'))

        if gender == '男':
            # 男性
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == '女':
            # 女性
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print('基础代谢率(大卡)：', bmr)
        else:
            print('暂不支持该性别')

        if input('是否退出程序(y/n)?') == 'y':
            break


if __name__ == '__main__':
    main()
