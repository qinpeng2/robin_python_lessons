"""
    作者：Allen
    功能：BMR计算器
    版本：3.0
    日期：03/17/2019
"""


def main():
    """
        主函数
    """
    while True:
        print('请输入如下信息：')
        input_str = input('性别  体重（kg)  身高（cm） 年龄')
        input_list = input_str.split(' ')

        gender = input_list[0]
        weight = float(input_list[1])
        height = float(input_list[2])
        age = int(input_list[3])

        if gender == '男':
            # 男性
            bmr = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
        elif gender == '女':
            # 女性
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print('您的性别：{}，体重：{}公斤，身高：{}厘米，年龄：{}岁'.format(gender, weight, height, age))
            print('您的基础代谢率：{}大卡'.format(bmr))
        else:
            print('暂不支持该性别')

        if input('是否退出程序(y/n)') == 'y':
            break


if __name__ == '__main__':
    main()
