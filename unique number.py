v=int(input())
k=list(map(int,input().split()))
vk=[]
for i in k:
  if k.count(i)>1:
    if str(i) not in vk:
      vk.append(str(i))
if len (vk)==0:
  print("unique")
else:
  k.sort()
  print(" ".join(vk))
