import datetime


def time_from_pattern(time_, pattern_):
    dt_ = datetime.datetime.fromtimestamp(time_)
    return dt_.strftime(pattern_)