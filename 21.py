list=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
lis=[]
for i in range(0,len(list)):
    if(list[i]==10):
        lis.append(i)
print(lis,list.count(10))