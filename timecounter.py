import time
while True:
    print('Write a number.')
    x = int(input())
    if x >= 0:
        time.sleep(x)
    else:
        exit(0)
