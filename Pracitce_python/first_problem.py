
bill = 0

while(True):
    x = input("Enter item price you want or You want to exit Enter q")

    if x.isnumeric():
        bil = bil + int(x)

    elif(x == "q"):
        print("You total bill is : ", bil)
    
    else:
        print("Error You enter wrong digit or you enterd word expect for \"q\"")
        break;