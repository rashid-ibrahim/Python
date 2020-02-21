import time


def make_readable(seconds):
    minutes, sec = divmod(seconds, 60)
    hour, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hour, minutes, sec)


x = make_readable(359999)

print(x)
