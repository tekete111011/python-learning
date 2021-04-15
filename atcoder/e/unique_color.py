import copy
N = int(input)
C = list(map(int, input().split() ))
graph = [ [] for i in range(N)]
for i in range(N-1):
  u, v = map(int, input().split())
  
  u -= 1
  v -= 1

  graph[u].append(v)
  graph[v].append(u)

for i in range(N):
  for j in graph[i]:
    if C[i] != C[j-1]:
      print(C[i])