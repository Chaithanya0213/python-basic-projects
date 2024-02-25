num=0
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("fizzBuzz")  
    elif i%3==0:
        print("fizz")  
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
#another way with switch