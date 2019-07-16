vk=int(input())
v=input()
k=list(map(int,v.split()))
if len(k)==vk:
  k.sort(reverse=True)
  v=[str(i) for i in k]
  m=int("".join(v))
  print(m)
