# Calculator method one
result = 0;
while(True):
    number = input("Enter number you want to calculate  or If you want to quit press \"q\" : ")
    usersInput = input("Enter one of these you want to calculate : / * + -")
    if(usersInput == "/"):
        result /= int(number)
    elif(usersInput == "*"):
        result *= int(number)
    elif(usersInput == "+"):
        result += int(number)
    elif(usersInput == "-"):
        result -= int(number)
    elif(usersInput == "q"):
        print("Your Total calculation is :" , result)
        break;
    print(result)

# Calculator methos two, which is very simple
# userInut = input("Enter one of these you want to calculate : / * + -")

# num1 = int(input("Enter first number you want : "))
# num2 = int(input("Enter second number you want : "))
# result = 0
# if(userInut == "/"):
#     result = num1 / num2
# elif(userInut == "*"):
#     result  = num1 * num2
# elif(userInut == "+"):
#     result  = num1 + num2
# elif(userInut == "-"):
#     result  = num1 - num2 
# else:
#     print("You enter wrong calculative method")

# print("You total result is : ", result)