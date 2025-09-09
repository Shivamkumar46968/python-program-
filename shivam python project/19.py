a=input("enter your full name:")
print(a[0],end="")
b=-1
c=a.count(" ")
for i in range(0,len(a)):
    b=a.find(" ",b+1)
    print(a[b+1],end="")
    if(b<0):
        break
