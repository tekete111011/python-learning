def Euclidean_algo(A):
  a = max(A)
  b = min(A)
  r = a % b
  B = [b, r]
  if r == 0:
    return b
  else:
    return Euclidean_algo(B)

a = list(map(int, input().split()))
print(Euclidean_algo(a))