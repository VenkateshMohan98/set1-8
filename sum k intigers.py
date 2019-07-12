d,k=input().split()
k=int(k)
v=list(map(int,input().split()))
num=0
for i in range(0,k):
  num+=v[i]
  print(num)
