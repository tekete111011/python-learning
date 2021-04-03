def my_max(A):
  max = 0
  for i in range(len(A)):
    if max < A[i]:
      max = A[i]
  return max

a = list(map(int, input().split()))
print(my_max(a))