
bill = 0

while(True):
    x = input("Enter item price you want or You want to exit Enter q \n")

    if (x !="q"):
        bill = bill + int(x)
        print(f"Your order total soffar is : {bill} ")

    else:
        print(f"You Total bill is : {bill}")
        print("Thanks for shopping")
        break;