bill = 0 

while(True):
    userInput = input("Enter the number or q to quit the calculation : ")

    if(userInput.isnumeric()):
        bill = bill + int(userInput)
        print(f"At this point of bill is {bill} ")
    elif (userInput == "q"):
        print(f"Your total bill is: {bill}")
        print("Thanks for shopping")
        break;