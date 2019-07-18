v=int(input())
k=v
sum=0
while v>0:
  sum+=((v%10)**3)
  v=v//10
if (sum==k):
  print("yes")
else:
  print("no")
