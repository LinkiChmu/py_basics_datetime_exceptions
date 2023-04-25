from datetime import datetime


def is_date_correct(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return False
    return True


stream = ['2018-04-02', '2018-02-29', '2018-19-02']
print([is_date_correct(date) for date in stream])
