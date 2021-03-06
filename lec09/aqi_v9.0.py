"""
    功能：空气质量指数
    作者：Allen
    版本：9.0
    说明：v9.0 使用pandas库进行如下操作：
        1）csv操作
        2）数据统计
    日期：2019/04/07
"""
import pandas


def main():
    splitter = '--------------------------------------------'
    """
        主函数
    """
    # 基本信息
    aqi_data = pandas.read_csv('output_data/v8.0_pm25in_city_aqi.csv')
    print('基本信息：\n' + splitter)
    print(aqi_data.info())
    print(splitter)

    # 数据预览
    print('数据预览\n' + splitter)
    print(aqi_data.head())
    print(splitter)

    # 基本统计
    print('AQI最大值', aqi_data['AQI'].max())
    print('AQI最小值', aqi_data['AQI'].min())
    print('AQI平均值', aqi_data['AQI'].mean())
    print(splitter)

    # top 10
    top10_cities = aqi_data.sort_values(by=['AQI']).head(10)
    print('AQI排名前十: ')
    print(top10_cities)
    print(splitter)

    # bottom 10
    # bottom10_cities = aqi_data.sort_values(by=['AQI']).tail(10)
    bottom10_cities = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print('AQI排名最差前十：')
    print(bottom10_cities)
    print(splitter)

    # 保存CSV文件
    top10_cities.to_csv('output_data/v9.0_top10_aqi.csv', index=False)
    bottom10_cities.to_csv('output_data/v9.0_bottom10_aqi.csv', index=False)


if __name__ == '__main__':
    main()
