N, A, B = map(int, input().split())
sums = 0

for i in range(N):
  j = str(i)
  array = list(map(int, j))
  if A<=sum(array)<=B:
    sums += sum(array)

print(sums)