import math
n = int(input())
i, res = 2, True

while i <= math.sqrt(n):
    if n % i == 0:
        res = False
        break
    i += 1

if res:
    print(1)
else:
    print(0)