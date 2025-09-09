a=int(input("enter '1 for day to hours','2 for hours to minute','3for minute to second':"))
if a==1:
    b=int(input("enter no. of days:"))
    print(b,"days=",b*24,"hours")
elif a==2:
    b=int(input("enter no. of hours:"))
    print(b,"hrs=",b*60,"min")
elif a==3:
    b=int(input("enter no. of minutes:"))
    print(b,"mins=",b*60,"secs")
else:
    print("error")
