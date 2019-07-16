v=int(input())
k=input(" ")
k=list(k.split(' '))
a={}
for i in k:
   if i in a:
      a[i]+=1
   else:
      a[i]=1
for key,value in a.items():
  if value==1:
     print(key)
