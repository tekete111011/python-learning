def average(A):
  return(sum(A)/len(A))

a = list(map(int, input().split()))
print(average(a))