day = int(input("Enter the day of the week (1-7):"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7: 
        print("Sunday")
    case _:
        print("Invalid day")


month = int(input("Enter the month (1-12):"))
match month :
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 days")
    case 4 | 6 | 9 | 11:
        print("30 days")
    case 2:
        print("28 days (29 in leap years)")
    case _:
        print("Invalid month")