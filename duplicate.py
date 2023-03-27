def duplicate(a):
    b = set(a)
    c = list(b)
    for i in range(len(c)):
        a.remove(c[i])
    if len(a) == 0:
        print("There are no duplicates.")
    else:
        print("There are some duplicates.")
x = list(input().split())
duplicate(x)