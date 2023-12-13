import datetime


def add_date(year, month, day, hour, minute, second):
    date_time = datetime.datetime(year, month, day, hour, minute, second)
    return date_time