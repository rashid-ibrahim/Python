"""
Problem statement found at: https://www.hackerrank.com/challenges/python-time-delta/problem

When users post an update on social media,such as a URL, image, status update etc., other users in their network are
able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many
hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two
timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.


Print/return the absolute difference (t1 - t2) in seconds.
"""

from datetime import datetime
from datetime import timedelta

def time_delta(t1, t2):
    t1 = datetime.strptime(t1[4:], '%d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(t2[4:], '%d %b %Y %H:%M:%S %z')

    diff = abs(t1-t2)
    diff = str(int(timedelta(days=diff.days, seconds=diff.seconds).total_seconds()))

    return diff


if __name__ == '__main__':
    # x = time_delta('Sun 10 May 2015 13:54:36 -0700', 'Sun 10 May 2015 13:54:36 -0000')
    x = time_delta('Sat 02 May 2015 19:54:36 +0530', 'Fri 01 May 2015 13:54:36 -0000')
    print(x)
