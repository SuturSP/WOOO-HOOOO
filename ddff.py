def subtract(a, b):
    return a - b


def add(a, b):
    return a + b


def isbigger(a, b):
    return a > b


def inclusion(a, b):
    a.append(b)
    return a


def exclusion(a, b):
    if b in a:
        a.remove(b)
    return a


def equality(a, b):
    if len(b) < len(a):
        b = (len(a) - len(b)) * '0' + b
        return b
    else:
        a = (len(b) - len(a)) * '0' + a
        return a
