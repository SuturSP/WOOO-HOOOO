def season(n):
    if n >= 13:
        print("There are only twelve months.")
    elif 3 <= n <= 5:
        print("Spring.")
    elif 6 <= n <= 8:
        print("Summer.")
    elif 9 <= n <= 11:
        print("Autumn.")
    else:
        print("Winter.")
