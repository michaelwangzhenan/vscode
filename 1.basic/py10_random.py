import random as rd
import numpy as np


# 计算机不会产生绝对随机的随机数，计算机只能产生“伪随机数”
# 伪随机数是通过某种算法，获取随机值，不是真的很随机。
# 随机数种子是生成伪随机序列时所依赖的一个初始值。它的作用是确保每次生成的随机数序列是不同的。
# 对于一个伪随机数生成器，从相同的随机数种子出发，可以得到相同的随机数序列。
# 所以为了保证伪随机数生成器生成的数够随机，要让种子真随机

np.set_printoptions(suppress=True)
N = 10
rdlist = np.zeros((7, N), dtype=np.float32)

for i in range(N):
    # 1. random.random() 用于生成一个0-1的随机浮点数：0<=n<1.0
    rdlist[0, i] = rd.random()

    # 2. random.uniform(a,b) 用于生成一个指定范围内的随机浮点数，两个参数中，一个是上限，一个是下限，位置可以互换。
    # if a<b,则生成的随机数n：a<=n<b；else 同理。
    rdlist[1, i] = rd.uniform(0, 100)

    # 3. random.randint(a,b) 用于声场一个指定范围内的整数。其中，参数a是下限，b是上限，生成的随机数n：a<=n<=b。
    rdlist[2, i] = rd.randint(100, 200)

    # 4. random.randrange([start],stop,[step]) 从指定范围中，按指定基数递增的集合中获取一个随机数。
    # 参数必须为整数，start默认为0，step默认为1，所以，写单个参数时，最小是1，不然会报错哦。
    rdlist[3, i] = rd.randrange(200, 300, 5)

    # 5. random.choice(sequence) 从序列中获取一个随机元素，参数sequence表示一个有序类型，
    input_list = range(200, 300)
    rdlist[4, i] = rd.choice(input_list)

    rdlist[5, i] = i
    rdlist[6, i] = i

# 6. random.shuffle(x,[random]) 用于将一个列表中的元素打乱，即将列表中的元素随机排列。
rd.shuffle(rdlist[5, :])
print(rdlist)

# 7. random.sample(sequence,k) 从指定序列中随机获取指定长度的片段。sample函数不会修改原有的序列。
print(rd.sample(list(rdlist[6]), 5))
