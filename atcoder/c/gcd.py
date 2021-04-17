import math
a, b = map(int, input().split())
max_l = 0

for i in range(a, b):
  for j in range(i+1, b+1):
    x = math.gcd(i , j)
    if x > max_l:
      max_l = x

print(max_l)