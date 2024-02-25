#paying bill randomly from group of friends in a restauent
import random
"""
without using choicess() method
names=input("Enter your friends names seperated by comma: ")
names_list=names.split(",")
length=len(names_list)
random_choice=random.randint(0,length-1)
print(f"{names_list[random_choice]} will pay the bill")
"""
#using choice()method
names=input("Enter your friends names seperated by comma: ")
names_list=names.split(",")
person_selected=random.choice(names_list)
print(f"{random.choice(names_list)} will pay the bill")
#print(f"{person_selected} will pay the bill")