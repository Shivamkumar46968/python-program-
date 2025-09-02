a=int(input("enter '1 for celcius to fahreinheit','2 for fahtrenheit to celcius':"))
if a==1:
    b=int(input("enter celcius  :"))
    print(b,"celcius=",(b*9/5)+32,"fahreinheit")
elif a==2:
    b=int(input("enter fahreinheit :"))
    print(b,"fahrenheit=",(b-32)*5/9,"celcius")
else:
    print("error")