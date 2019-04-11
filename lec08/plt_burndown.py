import matplotlib.pyplot as plt
import pandas


def read_personal_data():
    week_data = pandas.read_csv('data.csv')
    return week_data['km']


def main():
    target = 1000
    weeks = 52
    week_target = []
    week_actual = []
    # target list
    for i in range(weeks):
        week_target.append(target - target/weeks * i)
    # actual list
    personal_data = read_personal_data()

    total_km = 0
    for km in personal_data:
        total_km += km
        week_actual.append(target - total_km)

    plt.title('Burn Down Chart')
    plt.plot(week_target)
    plt.plot(week_actual)
    plt.plot()
    plt.show()


if __name__ == '__main__':
    main()
