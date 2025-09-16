def filter(a):
    b=[i+2 for i in a]
    return b
a=[2,3,4,5,6,5,7]
c=filter(a)
print(c)