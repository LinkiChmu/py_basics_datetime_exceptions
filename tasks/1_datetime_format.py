from datetime import datetime

"""
The different date formats to convert to a datetime object.
"""

moscow_times_dt = datetime.strptime('Wednesday, October 2, 2002', '%A, %B %d, %Y')
moscow_times_str = moscow_times_dt.strftime('%A, %B %-d, %Y')
print(moscow_times_dt, moscow_times_str)

guardian_dt = datetime(2013, 10, 11)
guardian_str = guardian_dt.strftime('%A, %d.%m.%y')
print(guardian_dt, guardian_str)

daily_news_dt = datetime.strptime('Thursday, 18 August 1977', '%A, %d %B %Y')
daily_news_str = daily_news_dt.strftime('%A, %d %B %Y')
print(daily_news_dt, daily_news_str)
