s=input("enter a string:")
p=s[len(s)::-1]
if p==s:
    print(f"{s} is pallindrome")
else:
    print(p)