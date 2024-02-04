import matplotlib.pyplot as plt
import numpy as np
from pandas import Series, DataFrame


def fig_addsubplot():
    fig = plt.figure(figsize=(12, 8))

    ax2 = fig.add_subplot(2, 2, 2)  # 2x2 的fig, 这里加上第2个
    ax3 = fig.add_subplot(2, 2, 3)  # 2x2 的fig, 这里加上第3个

    plt.plot([1, 5, 3, 9])  # 默认在最后一个 subplot上绘图,此时是ax3
    ax2.plot([1, 5, 3, 9], 'k--')  # 在指定的 subplot 上绘图, k--表示黑色虚线

    ax1 = fig.add_subplot(2, 2, 1)  # 2x2 的fig, 这里加上第1个
    ax1.hist([1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4], bins=20)  # 柱状图/直方图

    ax4 = fig.add_subplot(2, 2, 4)  # 2x2 的fig, 这里加上第4个
    ax4.scatter(np.arange(1, 5), [1, 5, 3, 9])  # 散列图

    # TBD: plot/hist/scatter 函数的深入研究

    plt.show()


def style_color():
    fig, axes = plt.subplots(2, 3, figsize=(16, 9))  # 直接生成 2x3 的fig

    axes[0, 0].plot([1, 5, 3, 9])  # 按坐标指定其中的一个subplot
    axes[0, 1].plot(np.random.randn(30).cumsum(), 'g--')  # 绿色虚线
    axes[0, 2].plot(np.random.randn(30).cumsum(), color='k', linestyle='--')  # 黑色虚线
    axes[1, 0].plot(np.random.randn(30).cumsum(), 'ro--')  # 红色虚线，加标记点

    data = np.random.randn(30).cumsum()
    axes[1, 1].plot(data, 'r-', label='default')
    axes[1, 1].plot(data, 'g--', label='steps', drawstyle='steps-post')  # 同一 subplot 画第二根线
    axes[1, 1].legend(loc='upper left')  # ！这样label 才显示

    plt.show()


# style_color()


def xy_axis():
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(1, 1, 1)
    data1 = np.random.randn(100).cumsum()
    data2 = np.random.randn(100).cumsum()
    ax.plot(data1, 'r-', label='default')
    ax.plot(data2, 'g--', label='steps', drawstyle='steps-post')
    # ax.legend(loc='upper left')
    ax.legend(loc='best')  # 自动找个没遮挡的地方

    # ax.set_xlim([-10, 120])
    ax.set_title("This is Title", fontsize=24, color="purple")
    ax.set_xlabel("H direction", fontsize=16)
    ax.set_ylabel("V direction", fontsize=16)
    ax.set_xticks([0, 20, 40, 60, 80, 100])  # x轴刻度
    ax.set_xticklabels(['a0', 'b20', 'c40', 'd60', 'e80', 'f100'])  # x轴刻度的文字
    ax.text(x=10, y=3, s="Hello~~", fontsize=18, color='blue')  # x, y：文字的坐标, s: 文字内容
    ax.annotate(text='annotate', xy=(50, 0), xytext=(52, 2),  # text:注释内容，xy:被注释点坐标， xytext:注释文字坐标
                arrowprops=dict(facecolor='yellow'))  # 箭头，从注释指向被注视点，参数是一个数据字典，有多个属性可设置

    plt.show()


# xy_axis()


def series_plot():
    s = Series(np.random.randn(10).cumsum(), index=np.arange(10))
    s.plot()

    plt.show()


# series_plot()


def dataframe_plot():
    df = DataFrame(np.arange(3*5).reshape((5, 3)), columns=['apple', 'banana', 'cap'])
    df['apple'] = [2, 5, 77, 110, 66]
    df['banana'] = [1, 66, 36, 50, 38]
    df['cap'] = [63, 34, 84, 22, 65]
    df.plot()  # DataFrame plot 为每列画一条线，并创建图例

    plt.show()


dataframe_plot()