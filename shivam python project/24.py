a,b=-1,1
l=[]
sum=0
for i in range(0,10):
    c=a+b
    l.insert(i,c)
    a,b=b,c
print(l)
for i in range(0,10):
    if i%2==0:
       sum=sum+l[i]
print(sum)