import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


tti_file = 'D:/1_Michael/python/OFF_dl.csv'
tti_dataframe = pd.read_csv(tti_file, low_memory=False)
# print(tti_dataframe)

buffer = DataFrame({'rnti': tti_dataframe['rnti'],
                    'rrmBufferedDataDlTotal': tti_dataframe['dlFdSchedData.rrmBufferedDataDlTotal']})
buffer = buffer.dropna(axis=0, how='any')  # 去除 Nan 行
# print(buffer)

grouped_buffer = buffer['rrmBufferedDataDlTotal'].groupby(buffer['rnti'])
# print(type(grouped_buffer))
# print(grouped_buffer.ngroups)
print(grouped_buffer.size())
# print(grouped_buffer.get_group(793))


fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(2, 2, 1)
grouped_buffer.get_group(793).plot(ax=ax1)
grouped_buffer.get_group(1361).plot(ax=ax1)
# grouped_buffer.get_group(60809).plot(ax=ax1)

ax2 = fig.add_subplot(2, 2, 2)
df = DataFrame({'793': grouped_buffer.get_group(793),
                '1361': grouped_buffer.get_group(1361)})
df.plot(ax=ax2)

plt.show()