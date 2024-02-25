#To check whether leap year or not
Year=int(input("Enter Year: "))
if Year%4==0:
    if Year%100==0:
        if Year%400==0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
         print("Leap year")        
else:
    print("Not a leap year")
