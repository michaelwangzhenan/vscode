import csv
from datetime import datetime
import matplotlib.pyplot as plt


def get_temperture():
    # filename = "data/sitka_weather_07-2018_simple.csv"
    filename = "data/death_valley_2018_simple.csv"
    with open(filename) as f:
        reader = csv.reader(f)
        head = next(reader)
        i_high = head.index('TMAX')  # 取 index
        i_low = head.index('TMIN')
        for index, title in enumerate(head):  # enumerate 函数可以为列表自动计数，取出 index
            print(index, title)

        dates, highs, lows = [], [], []
        for row in reader:
            try:
                date = datetime.strptime(row[2], '%Y-%m-%d')  # 这里要转成date, 否则当 string处理, 横坐标将有太多刻度
                high = int(row[i_high])/1.8-32  # 这里要转成int, 否则当 string处理， 纵坐标轴不会按大小排列
                low = int(row[i_low])/1.8-32
            except ValueError:
                print("data missing")
            else:
                dates.append(date)
                highs.append(high)
                lows.append(low)

    return dates, highs, lows


# get_temperture()


def plt_plot(inputs):
    plt.style.use(plt.style.available[0])
    figure, ax = plt.subplots(figsize=(15, 6))
    ax.plot(inputs[0], inputs[1], c='red', alpha=0.8)
    ax.plot(inputs[0], inputs[2], c='blue', alpha=0.3)

    ax.set_title("High-Low tTmperture", fontsize=32, color="purple")

    ax.set_xlabel("Date", fontsize=24)
    figure.autofmt_xdate()
    ax.set_ylabel("Temperture", fontsize=24)

    ax.tick_params(axis="both", which='major', labelsize=12)  # 刻度字体大小
    ax.fill_between(inputs[0], inputs[1], inputs[2], facecolor='pink', alpha=0.3)

    plt.ylim(-20, 50)  # 设置坐标轴刻度范围
    plt.show()


# plt_plot(get_temperture())


def try_csv():
    filename = "3.data_plot/data/death_valley_2018_simple.csv"
    with open(filename) as f:
        reader = list(csv.reader(f))
        head, data = reader[0], reader[1:]
        dict = {k: v for k, v in zip(head, zip(*data))}

    print(dict[list(dict.keys())[0]])
    # print(len(list(dict.values())[0]))


try_csv()
