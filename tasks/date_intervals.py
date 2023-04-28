"""
Given a list of dates sorted in ascending order and a date
that lies between the minimum and maximum values from this list.
The function determines the nearest dates from the list
surrounding the given date
"""

date_list = ['2023-01-01', '2023-01-07', '2023-02-23', '2023-03-08', '2023-05-01',
             '2023-05-09', '2023-06-12']
date = '2023-04-01'


def find_date_neighbors(sorted_list, date):
    result = []
    for i, curr_date in enumerate(sorted_list[:-1]):
        if curr_date <= date <= sorted_list[i+1]:
            result.append(curr_date)
            result.append(sorted_list[i+1])
            return result
    return result


print(*find_date_neighbors(date_list, date))

