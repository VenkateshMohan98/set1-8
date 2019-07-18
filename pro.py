num=int(input())
lis=[]
for i in range(num):
    c=input()
    lis.append(c)
lis1=[]
for i in zip(*lis):
  if(i.count(i[0])==len(i)):
    lis1.append(i[0])
  else:
    break
print(''.join(lis1))
