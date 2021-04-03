def average(N,A):
  return(sum(A)/N)

n = int(input())
a = list(map(int, input().split()))
print(average(n,a))