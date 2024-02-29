from datetime import datetime
from datetime import timedelta
from pandas import Series
import numpy as np


def time_basic():
    now = datetime.now()
    print(now)
    print(now.year, now.month, now.day)
    print(now.date())
    print(now.time())

    someday = datetime(2022, 5, 3, 16, 48, 20, 123456)
    print(someday)

    delta = now - someday
    print(delta)
    print(delta.days, delta.seconds)

    later = now + timedelta(12, 10)  # 天 和 秒
    print(later)

    print(now)  # print的时候以及自动转换为str
    print(str(now))
    print(now.strftime("%Y.%m.%d"))
    print(now.strftime("%y.%m.%d"))
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


dates = [datetime(2024, 1, 1),
         datetime(2024, 3, 8),
         datetime(2024, 4, 5),
         datetime(2024, 5, 1),
         datetime(2024, 6, 1)]

ts = Series(np.arange(5), index=dates)
print(ts)
print(ts.index)
ti2 = ts.index[2]
print(ti2)
print(type(ti2))
print(ts[ti2])
