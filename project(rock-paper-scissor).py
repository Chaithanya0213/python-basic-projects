import random
user_choice=int(input("Enter your choice: (Type 0 for Rock, 1 for paper, 2 for scissor): "))
index_number=random.randint(0,2)
list_item=["rock","paper","scissor"]
""""
list_item=["rock","paper","scissor"]
computer_chose=random.choice(list_item)
print(computer_chose)
computer_choice=list_item.index(computer_chose)
print(computer_choice)
"""

computer_chose=list_item[index_number]
print("Computer chose:")
print(computer_chose)
computer_choice=list_item.index(computer_chose)


if computer_choice==user_choice:
    print("It's a draw")
elif computer_choice==0 and user_choice==2:
    print("You lose")
elif user_choice==0 and computer_choice==2:
    print("You win")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win")


