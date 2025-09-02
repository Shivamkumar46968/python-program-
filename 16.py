lis=["shivam","abhishek","sonu"]
lis.append("saurabh")
print(lis[::3])
#method2
for i in range(0,len(lis),3):
    print(lis[i])