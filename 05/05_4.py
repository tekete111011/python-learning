def fibonacci(N):
  if N==1:
    return 1
  elif N==0:
    return 0
  else:
    return fibonacci(N-1)+fibonacci(N-2)

n=int(input())
print(fibonacci(n))