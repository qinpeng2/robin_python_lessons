"""
    功能：空气质量指数
    作者：Allen
    版本：1.0
    说明：v1.0 计算公式
    日期：2019/04/08
"""


def cal_linear(iaqi_hi, iaqi_lo, bp_hi, bp_lo, cp):
    """
        范围缩放，线性变换
    """
    return (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo


def cal_pm_iaqi(pm25):
    """
        计算PM2.5的IAQI
    """
    if 0 < pm25 <=35:
        pm25_iaqi = cal_linear(50, 0, 35, 0, pm25)
    elif 35 < pm25 <= 75:
        pm25_iaqi = cal_linear(100, 50, 75, 35, pm25)
    elif 75 < pm25 <= 115:
        pm25_iaqi = cal_linear(150, 100, 115, 75, pm25)
    else:
        pm25_iaqi = 0
    return pm25_iaqi


def cal_co_iaqi(co):
    """
        计算CO的IAQI
    """
    if 0 < co <=5:
        co_iaqi = cal_linear(50, 0, 5, 0, co)
    elif 5 < co <= 10:
        co_iaqi = cal_linear(100, 50, 10, 5, co)
    elif 10 < co <= 35:
        co_iaqi = cal_linear(150, 100, 35, 10, co)
    else:
        co_iaqi = 0
    return co_iaqi


def cal_aqi(param):
    """
        AQI计算
    """
    pm25 = param[0]
    co = param[1]

    iaqi_list = [cal_pm_iaqi(pm25), cal_co_iaqi(co)]
    aqi = max(iaqi_list)
    return aqi


def main():
    """
        主函数
    """
    print('请输入以下信息：')
    input_str = input('(1) PM2.5 (2) CO:')
    pm25 = float(input_str.split(' ')[0])
    co = float(input_str.split(' ')[1])

    aqi = cal_aqi([pm25, co])
    print('空气质量指数为: {}'.format(aqi))


if __name__ == '__main__':
    main()

