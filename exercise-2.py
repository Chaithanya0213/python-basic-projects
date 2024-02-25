#find out how many days, weeks, months we have left. If we have until 90 years old.
age=int(input("Enter your age: "))
Years_left=90-age
days_left=Years_left*365
months_left=Years_left*12
weeks_left=Years_left*52

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")
 