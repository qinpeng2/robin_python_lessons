"""
    功能：空气质量指数
    作者：Allen
    版本：8.0
    说明：v8.0 获取城市列表，自动获取所有城市数据，写入CSV文件
         切换为原课程中的pm25.in的站点，不再使用pm25.com
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


if __name__ == '__main__':
    main()
