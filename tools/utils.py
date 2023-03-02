import datetime
import random


def unique_time_stamp(num: int = 1, range_start: int = 0, range_end: int = 99999,):
    """
    Returns a unique string. Using a timestamp guarantees that a string cannot be repeated
    :param: num is positive number, this is a number of a random string to return, e.g.
     unique_time_stamp(1) - one random string will be generated and the first one will be returned
     unique_time_stamp(5) - five random strings will be generated and the 5th one will be returned
    :return: the current UTC time stamp + a random integer from [0; 999] range
    :rtype: str
    """
    random_numbers = random.sample(range(range_start, range_end), num)
    return [datetime.datetime.utcnow().strftime('%m%d%y%H%m%S') + str(i) for i in random_numbers][num - 1]


