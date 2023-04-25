from datetime import datetime

moscowtimes_dt = datetime.strptime('Wednesday, October 2, 2002', '%A, %B %d, %Y')
moscowtimes_str = moscowtimes_dt.strftime('%A, %B %-d, %Y')
print(moscowtimes_dt, moscowtimes_str)

guardian_dt = datetime(2013, 10, 11)
guardian_str = guardian_dt.strftime('%A, %d.%m.%y')
print(guardian_dt, guardian_str)

dailynews_dt = datetime.strptime('Thursday, 18 August 1977', '%A, %d %B %Y')
dailynews_str = dailynews_dt.strftime('%A, %d %B %Y')
print(dailynews_dt, dailynews_str)
