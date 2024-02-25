#calculate BMI
#weight/(height * height)
print("-----You can calculate your BMI here-----")
print("NOTE: Enter your weight in kilograms")
weight=int(input("enter your weight: "))
print("NOTE: enter your height in meters---")
height=float(input("enter your height: "))
BMI=(weight/height**2)

if BMI<18.5:
    print(f"Your BMI is {BMI} and Your weight is in normal range")
elif BMI<25:
    print(f"Your BMI is {BMI} and You are Overweight(pre-obese)")
elif BMI<30:
    print(f"Your BMI is {BMI} and You are in OBESE class")
elif BMI<35:
    print(f"Your BMI is {BMI} and You are clinically obese") 
