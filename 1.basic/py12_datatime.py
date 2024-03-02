from datetime import datetime
from datetime import timedelta
from pandas import Series
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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


def time_serise_base():
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
    print(ts['20240601'])  # 传入一个可以解析成日期的字符串


def time_serise_slice():
    ts = Series(np.arange(1000), index=pd.date_range('2024/01/01', periods=1000))

    print(ts)
    print(ts['2025'])
    print(ts['2025/09'])
    print(ts['2025/08':'2025/09'])
    print(ts[datetime(2025, 9, 20)])
    print(ts[998:])


def time_serise_plot():
    ts = Series(np.random.randn(120), index=pd.date_range('2024/01/01', periods=120))
    ts.plot()
    plt.show()


time_serise_plot()