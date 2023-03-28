import time
print('Year of birth.')
c = int(input())
print('Month of birth.')
b = int(input())
print('Day of birth.')
a = int(input())
m = time.struct_time((c,b,a,0,0,0,0,200,0))
l = (time.time() - time.mktime(m)) / 86400
print(l)
