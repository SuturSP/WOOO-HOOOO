def palindrome(a):
    b = list(a)
    c = len(b) // 2
    d = b[0:c]
    b.reverse()
    f = b[0:c]
    if d == f:
        print("a is a palindrome.")
    else:
        print("a is not a palindrome.")
x = input()
palindrome(x)