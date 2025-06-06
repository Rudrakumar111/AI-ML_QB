unit = int(input("Enter the number of unit consumed: "))

if unit <=100:
    print("you have no bill to pay !")
elif unit <=100 and unit >=200:
    unit=unit*5
    print("your bill is ",unit)
else :
    unit=unit*10
    print("youur bill is",unit)