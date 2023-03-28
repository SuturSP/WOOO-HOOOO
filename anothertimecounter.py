import time
from random import randint
import os

N = int(input())

l = time.time()

a = []
for i in range(N):
    a.append(randint(1, 99))
for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

m = (time.time() - l)
n = str(m)
g = time.strftime('%H:%M:%S %d.%m.%Y') + ".txt"
g = g[0:2] + " " + g[3:5] + " " + g[6:]
with open(g, 'w+') as f:
    f.write(n)
