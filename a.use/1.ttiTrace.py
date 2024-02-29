import pandas as pd
from pandas import DataFrame, Series
import matplotlib.pyplot as plt


tti_file = 'D:/1_Michael/python/OFF_dl.csv'
tti_dataframe = pd.read_csv(tti_file, low_memory=False)
# print(tti_dataframe)

buffer = DataFrame({'xsfn': tti_dataframe['sfn']*10 + tti_dataframe['slot'],
                    'rnti': tti_dataframe['rnti'],
                    'rrmBufferedDataDlTotal': tti_dataframe['dlFdSchedData.rrmBufferedDataDlTotal']})
buffer = buffer.dropna(axis=0, how='any')  # 去除 Nan 行

grouped = buffer.groupby(buffer['rnti'])
grouped_buffer = grouped['rrmBufferedDataDlTotal']  # buffer['rrmBufferedDataDlTotal'].groupby(buffer['rnti'])
grouped_xsfn = grouped['xsfn']  # buffer['xsfn'].groupby(buffer['rnti'])
rntis = list(grouped.groups.keys())

fig = plt.figure(figsize=(12, 8))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)

rntis_to_plot = rntis[17:20]
rntis_to_plot_df = {}
for rnti in rntis_to_plot:
    s = Series(list(grouped_buffer.get_group(rnti)), index=grouped_xsfn.get_group(rnti))
    s.plot(ax=ax1, label=rnti)
    rntis_to_plot_df[rnti] = grouped_buffer.get_group(rnti)

ax1.set_xlabel("xsfn", fontsize=16)
ax1.set_ylabel("buffer", fontsize=16)
ax1.legend(loc='best')


df = DataFrame({rntis[17]: list(grouped_buffer.get_group(rntis[17]))}, index=list(grouped_xsfn.get_group(rntis[17])))
df18 = DataFrame({rntis[18]: list(grouped_buffer.get_group(rntis[18]))}, index=list(grouped_xsfn.get_group(rntis[18])))

df = df.add(df18, fill_value=0)
# df = df.fillna(0)
# df = df.dropna(axis=0, how='any')  # 去除 Nan 行

print(df[rntis[17]][0:20])
df.plot(ax=ax2)

plt.show()
