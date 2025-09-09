def fahrenheit(l1):
    l=[]
    for i in range(0,len(l1)):
        l.append((l1[i]*9/5)+32)
    return(l)
l1=[36,37,38]
l=fahrenheit(l1)
print(l)