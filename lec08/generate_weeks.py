import datetime

start_date = '2020-01-01'
end_date = '2020-12-31'


def date_range(start, end):
    dates = []
    dt = datetime.datetime.strptime(start, "%Y-%m-%d")
    date = start[:]

    seq = 1
    kilo = 0
    week_start = date

    weeks = []

    while date <= end:
        dates.append(date)
        if dt.weekday() == 0:
            week_start = date
            # print('[{}'.format(date))
        elif dt.weekday() == 6 or (dt.month == 12 and dt.day == 31):
            week_end = date
            weeks.append((seq, kilo, week_start, week_end))
            seq = seq + 1

        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y-%m-%d")

    return weeks


if __name__ == '__main__':
    weeks = date_range(start_date, end_date)
    for week in weeks:
        print(week)