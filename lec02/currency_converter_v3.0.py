"""
作者：Allen
功能：人民币美元换算
"""

USD_VS_RMB = 6.77

input_value = input('请输入换算金额, 输入（Q）进行退出：')

i = 0

while input_value != 'Q':
    # 输入人民币金额
    currency = input_value[-3:]
    value_str = input_value[:-3]

    value = eval(value_str)

    print('即将转换的货币类型为：', currency)

    if currency == 'USD':
        value = value * USD_VS_RMB
    elif currency == 'CNY':
        value = value / USD_VS_RMB
    else:
        print('非法输入')

    print('*****************************************************', i)

    print('转换金额：', currency, value)

    i = i + 1

    input_value = input('请输入换算金额, 输入（Q）进行退出：')

print('程序已退出')
