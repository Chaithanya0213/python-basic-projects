numbers=input("Enter list of numbers seperated by space: ")
numbers_list=numbers.split()
count=0
for i in numbers_list:
    count+=1
print(f"The length of numbers_list is: {count}")
for i in range(count):
    numbers_list[i]=int(numbers_list[i])
print(numbers_list)
maximum_number=numbers_list[0]
for number in numbers_list:
    if number>maximum_number:
        maximum_number=number
print(f"The maximum number from the list of numbers is: {maximum_number}")