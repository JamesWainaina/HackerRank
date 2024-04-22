#!/usr/bin/python3

"""
Your local library needs your help! Given the expected and actual return dates for a library book,
create a program that calculates the fine (if any). The fee structure is as follows:
1. If any book is returned on or before the expected return date, no fine will be charged.
2. If any book is returned after the expected return day but still within the same calendar month,
the fine is 15 hackos per day.
3.If any book is returned after the expected return month but still within the same calendar year,
the fine is 500 hackos per month.
4. If any book is returned after the calendar year, there is a fixed fine of 10000 hackos.
"""

return_day, return_month, return_year =[int(a) for a in input().strip().split(' ')]
due_day, due_month, due_year = [int(a) for a in input().strip().split(' ')]

if return_year < due_year:
    print(0)
elif return_year == due_year:
    # check month
    if return_month < due_month:
        print(0)
    elif return_month == due_month:
        #check day
        if return_day < due_month:
            print(0)
        else:
            print(15 * (return_day - due_day))
    else:
        print(500 * (return_month - due_month))
else:
    print(10000)

