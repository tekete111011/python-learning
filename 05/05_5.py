def gcd(A):
  a = max(A)
  b = min(A)
  r = a % b
  B = [b, r]
  if r == 0:
    return b
  else:
    return gcd(B)

a, b = map(int, input().split())
max_l = 0

for i in range(a, b):
  for j in range(i+1, b+1):
    l = [i, j]
    x = gcd(l)
    if x > max_l:
      max_l = x

print(max_l)