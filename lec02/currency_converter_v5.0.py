"""
作者：Allen
功能：人民币美元换算
"""


def main():
    USD_VS_RMB = 6.77

    input_value = input('请输入换算金额, 输入（Q）进行退出：')

    # 输入人民币金额
    currency = input_value[-3:]
    value_str = input_value[:-3]

    value = eval(value_str)

    print('即将转换的货币类型为：', currency)

    if currency == 'USD':
        rate = USD_VS_RMB
    elif currency == 'CNY':
        rate = 1 / USD_VS_RMB
    else:
        rate = -1

    exchange_rate = lambda x: x * rate

    value = exchange_rate(value)

    print('*****************************************************')

    print('转换金额：', currency, value)
    print('程序已退出')


if __name__ == '__main__':
    main()
