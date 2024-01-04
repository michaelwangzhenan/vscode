import decimal


def cal_pi(precision):
    # getcontext().prec 设定计算精度，+2 以确保计算的准确性
    decimal.getcontext().prec = precision + 2
    pi = decimal.Decimal(0)
    decimal.getcontext().prec = precision + 10

    for k in range(precision + 10):
        pi += (decimal.Decimal(-1) ** k) / (decimal.Decimal(2 * k + 1))

    return str(pi * 4)


print(cal_pi(1000000))
