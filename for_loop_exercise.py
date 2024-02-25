heights=input("Enter all heights seperated by space: ")
height_list=heights.split()
count=0
for height in height_list:#for finding length
    count=count+1
print(count)
for i in range(count):#for type conversion
    height_list[i]=int(height_list[i])
total=0
for person in height_list:#for sum of heights
    total=total+person
print(total)
avg=total/count
print("average height is: ",round(avg))