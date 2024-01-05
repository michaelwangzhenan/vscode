import matplotlib.pyplot as plt
from collections import namedtuple


def get_data():
    x = [i for i in range(0, 11)]  # 列表推导式
    y = [i**2 for i in range(0, 11)]
    Ret = namedtuple('Ret', 'x y')  # 可以⽤名字来访问namedtuple中的数据
    return Ret(x=x, y=y)


def plt_plot(inputs):
    plt.style.use(plt.style.available[0])
    figure, ax = plt.subplots()

    ax.plot(inputs.x, inputs.y, linewidth=3)  # ⽤名字来访问namedtuple中的数据

    ax.set_title("Squares", fontsize=28, color="purple")
    ax.set_xlabel("value", fontsize=18)
    ax.set_ylabel("square", fontsize=18)
    ax.tick_params(axis="both", labelsize=12)  # 刻度字体大小

    plt.show()


plt_plot(get_data())


def plt_scatter(inputs):
    plt.style.use(plt.style.available[4])
    figure, ax = plt.subplots()

    ax.scatter(inputs.x, inputs.y, s=10, c=inputs[1], cmap=plt.cm.Blues)  # 也可以用index来访问

    ax.set_title("Squares", fontsize=28, color="red")
    ax.set_xlabel("value", fontsize=18)
    ax.set_ylabel("square", fontsize=18)
    ax.tick_params(axis="both", which='major', labelsize=12)  # 刻度字体大小

    plt.show()
    # plt.savefig('scatter.png')
    # plt.savefig('scatter2.png', bbox_inches='tight')


plt_scatter(get_data())
