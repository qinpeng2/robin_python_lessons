"""
作者：Allen
功能：人民币美元换算
"""

USD_VS_RMB = 6.77

# 输入人民币金额
input_value = input('请输入换算金额：')

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

print('转换金额：', currency, value)
