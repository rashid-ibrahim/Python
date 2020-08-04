"""
Problem Statement Found at: https://www.hackerrank.com/challenges/30-nested-logic/problem
"""
from datetime import datetime


def calc_fine(rdate, edate):
    if rdate <= edate:
        print(0)
        return

    if rdate.year != edate.year:
        print(10000)
        return
    elif rdate.month != edate.month:
        fine = rdate.month - edate.month
        modifier = 500
    else:
        fine = rdate.day - edate.day
        modifier = 15

    print(modifier*fine)


date_returned = [int(i) for i in input().split(" ")]
date_returned = datetime(year=date_returned[2], month=date_returned[1], day=date_returned[0])

expected_return = [int(i) for i in input().split()]
expected_return = datetime(year=expected_return[2], month=expected_return[1], day=expected_return[0])

calc_fine(date_returned, expected_return)
