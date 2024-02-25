#pizza order program 
size=input("which size of pizza do you want(S/M/L)?")
amount_payabel=0

if size=='S' or size=='s':
    amount_payabel+=100
    print(f"The price of small pizza is {amount_payabel}")
elif size=='M' or size=='m':
    amount_payabel+=200
    print(f"The price for medium pizza is {amount_payabel}")
elif  size=='L' or size=='l':
    print(f"The price for large pizza is {amount_payabel}")
pepperoni=input("Do you want pepperoni? y/n:")
if pepperoni=="y" or pepperoni=="Y":
    if size=='S' or size=='s':
        amount_payabel+=20
    else:
        amount_payabel+=50

extra_cheese=input("Do you want extra cheese? y/n:")
if extra_cheese =="y" or extra_cheese == "Y":
    amount_payabel+=20

print(f"Your  total payable amount is {amount_payabel}")