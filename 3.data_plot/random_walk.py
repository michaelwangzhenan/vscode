import matplotlib.pyplot as plt
from random import choice


class Random_Walk:
    def __init__(self, steps=5000) -> None:
        self.steps = steps

        self.x = [0]
        self.y = [0]
        self.distance = [i for i in range(1, 10)]
        self.direction = [-1, 1]

    def walk(self):
        while len(self.x) < self.steps:
            x = self.x[-1] + self._get_steps()
            y = self.y[-1] + self._get_steps()

            self.x.append(x)
            self.y.append(y)

    def _get_steps(self):
        return choice(self.direction) * choice(self.distance)


def draw():
    rw = Random_Walk(5000)
    rw.walk()

    print(len(plt.style.available))
    plt.style.use(plt.style.available[20])

    fig, ax = plt.subplots(figsize=(12, 8))  # 单位：英寸

    steps = range(rw.steps)
    ax.scatter(rw.x, rw.y, s=10, c=steps, cmap=plt.cm.Reds, edgecolors="none")
    # ax.plot(rw.x, rw.y, linewidth=1)

    # ax.get_xaxis().set_visible(False)  # 隐藏坐标轴
    # ax.get_yaxis().set_visible(False)

    plt.show()


draw()
