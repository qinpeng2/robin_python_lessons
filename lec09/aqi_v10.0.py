"""
    功能：空气质量指数
    作者：Allen
    版本：10.0
    说明：v10.0 Pandas数据清洗，生成统计图与图片
    日期：2019/04/08
"""
import pandas
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


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

    # 清洗数据
    aqi_data = aqi_data[aqi_data['AQI'] > 0]

    # 基本统计
    print('AQI最大值', aqi_data['AQI'].max())
    print('AQI最小值', aqi_data['AQI'].min())
    print('AQI平均值', aqi_data['AQI'].mean())
    print(splitter)

    # top 10
    top50_cities = aqi_data.sort_values(by=['AQI']).head(50)
    top50_cities.plot(kind='bar', x='City', y='AQI',
                      title='空气质量全国前50', figsize=(20, 10))

    # 生成统计图，以及图片
    plt.savefig('output_data/v10.0_top50_aqi_bar.png')
    plt.show()


if __name__ == '__main__':
    main()
