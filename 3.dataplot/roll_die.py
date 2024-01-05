from random import randint
from plotly.graph_objects import Bar, Layout
from plotly import offline

import matplotlib.pyplot as plt


class Die:
    def __init__(self, sides=6) -> None:
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)


def rool_die():
    die = Die()

    results = []
    for roll_num in range(1000):
        results.append(die.roll())

    frequencies = [results.count(p) for p in range(1, die.sides+1)]
    # for point in range(1, die.sides+1):
    #     frequencies.append(results.count(point))

    point = list(range(1, die.sides+1))
    data = [Bar(x=point, y=frequencies)]

    x_axis = {'title': 'point'}
    y_axis = {'title': 'frequency'}

    layout = Layout(title="die result", xaxis=x_axis, yaxis=y_axis)
    offline.plot({'data': data, 'layout': layout}, filename='die.html')


# rool_die()


def rool_2dies():
    die1 = Die()
    die2 = Die()

    results = []
    for roll_num in range(1000):
        results.append(die1.roll() + die2.roll())

    freqs = {}
    for p in range(2, die1.sides*2+1):
        freqs[p] = results.count(p)

    data = [Bar(x=list(freqs.keys()), y=list(freqs.values()))]

    x_axis = {'title': 'point', 'dtick': 1}  # 显示所有刻度
    y_axis = {'title': 'frequency'}

    layout = Layout(title="die result", xaxis=x_axis, yaxis=y_axis)
    offline.plot({'data': data, 'layout': layout}, filename='two_dies.html')


rool_2dies()


def draw():
    die1 = Die()
    die2 = Die()

    results = []
    for roll_num in range(1000):
        results.append(die1.roll() + die2.roll())

    freqs = {}
    for p in range(2, die1.sides*2+1):
        freqs[p] = results.count(p)

    plt.style.use(plt.style.available[20])

    fig, ax = plt.subplots(figsize=(12, 8))  # 单位：英寸

    x = list(freqs.keys())
    y = list(freqs.values())

    # ax.scatter(x, y, s=10, c=x, cmap=plt.cm.Blues)
    ax.plot(x, y, linewidth=1)

    plt.show()


# draw()
