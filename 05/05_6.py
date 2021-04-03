def buble_sort(A):
  N = len(A)
  for i in range(0,N-1):
    for j in range(1,N-i):
      #print(A[i], A[j])
      if A[j] <= A[j-1]:
        A[j], A[j-1]= A[j-1], A[j]
  return A

a = list(map(int, input().split()))
#print(a[0])
#print(a[1])
print(buble_sort(a))