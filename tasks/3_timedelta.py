from datetime import timedelta
from datetime import datetime


def date_range(start_date, end_date):
    """The function returns a list of dates in the range from start_date to end_date.
    It accepts dates in YYYY-MM-DD format. If the format is wrong
    or if start_date > end_date, returns an empty list.
    """
    dates = []
    if start_date > end_date:
        print('Некорректные границы периода')
        return dates

    try:
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        print('Неверный формат дат')
        return dates

    dates.append(start_date_dt.strftime('%Y-%m-%d'))
    while start_date_dt < end_date_dt:
        start_date_dt += timedelta(days=1)
        dates.append(start_date_dt.strftime('%Y-%m-%d'))

    return dates


def main():
    start_date = '2023-04-25'
    end_date = '2023-05-01'
    print(*date_range(start_date, end_date))


main()
