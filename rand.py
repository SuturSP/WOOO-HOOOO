import random


def gen(n):
    a = [random.random() for i in range(n)]
    return a


print(gen(6))
