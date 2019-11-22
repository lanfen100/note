a = [1,2,3,4,5,6,7,8,9,0]
n = 4
c = [a[i:i+n] for i in range(0, len(a), n)]

print(c)