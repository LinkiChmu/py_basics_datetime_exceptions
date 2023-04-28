from datetime import timedelta
from datetime import datetime


def date_range(start_date, end_date):
    """The function returns a list of dates in the range from start_date to end_date.
    It accepts dates in YYYY-MM-DD format. If the format is wrong
    or if start_date > end_date, returns an empty list.
    """
    if start_date > end_date:
        return []

    try:
        start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
        end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError:
        return []

    days_diff = (end_date_dt - start_date_dt).days + 1  # to include end_date
    return [(start_date_dt + timedelta(days=x)).strftime('%Y-%m-%d')
            for x in range(days_diff)]


def main():
    start_date = '2023-04-25'
    end_date = '2023-05-01'
    print(*date_range(start_date, end_date))


main()
