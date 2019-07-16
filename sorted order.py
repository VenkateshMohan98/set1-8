v=int(input())
k=[int(i) for i in input().split()]
a=[]
for i in range(0,len(k)):
  if i==k[i]:
    a.append(k[i])
if len(a)==0:
  print("-1")
else:
  for x in range(len(a)):
     print(a[x],end=" ")
