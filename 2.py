g=input("enter your gender")
s=int(input("enter your salary"))
if g=="male":
    if s>10000:
        print("your bonus:",5/100*s)
        print("your salary:",5/100*s+s)
    elif s<=10000 and s>=0:
        print("your bonus:",7/100*s+s)
        print("your salary:",7/100*s+s)
    else :
        print("invalid number")
elif g=="female":
    if s>=10000:
        print("your bonus:",10/100*s)
        print("your salary:",10/100*s+s)
    elif s<=10000 and s>=0:
        print("your bonus:",12/100*s+s)
        print("your salary:",12/100*s+s)
    else :
        print("invalid number")
else :
    print("invalid gender")