# # Calculate the factorial of given number

def factorial(number):
    if(number == 0 or number ==1):
        return 1
    else:
        return number * factorial(number - 1)

def factorialTrailingZero(number):
    count = 0
    i = 5
    while(number//i !=0):
        count += int(number/i)
        i = i* 5
    # fac = factorial(number)
    # print(fac)
    # count = 0
    # while(fac%10 == 0):
    #     count = count + 1
    #     fac = fac / 10
    # return count

if __name__ == '__main__':
    number = int(input("Enter a number \n"))
    fac = factorial(number)
    print(f"The factorial is {fac}")
    print(factorialTrailingZero(number))
            
    


# import math

# n = int(input("Enter you number"))
# fac_base =str(math.factorial(n))
# print(fac_base)


# import math
# number = int(input("Enter you Number: "))

# result = math.factorial(number)
# print(result)