import math
def roundd(n,m):
    i = n//m
    c = i + 0.5
    if n / m >= c:
        return i+1
    else:
        return i

n,m = map(int, input().split())
f = math.floor(n/m)
c = math.ceil(n/m)
r = roundd(n,m)
print(f'floor {n} / {m} = {f}')
print(f'ceil {n} / {m} = {c}')
print(f'round {n} / {m} = {r}')
