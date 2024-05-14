name = input("Enter you Name : \n")
print(f"Welcome to KBC! Mr or Mrs: {name} We warmly welcome you \n")
print("Here is you questions \n")

questions = ["Which indian states is known as the heaven of the earth in world", "Who won 2011 world cup", "Who is very popular minister in India", "What is the value of PI"]

answers = ["Jambu", "India", "modi","3.14"]
a = 1000
b = 2000
c = 3000
d = 4000
answer1 = input(questions[0])
if(answer1 == answers[0]):
    print(f"Yes it is correct answer and you won {a} INR")
    answer2 = input(questions[1])
    if(answer2 == answers[1]):
        print(f"Yes it is correct answer and you won {b} INR")
        answer3 = input(questions[2])
        if(answer3 == answers[2]):
            print(f"Yes it is correct answer and you won {c} INR")
            answer4 = input(questions[3])
            if(answer4 == answers[3]):
                print(f"Yes it is correct answer and you won {d} INR")
            else:
                print(f"You got the wrong answer You will take {c} INR to home")    
        else:
            print(f"You got the wrong answer You will take {b} INR to home") 
    else:
        print(f"You got the wrong answer You will take {a} INR to home")
else:
    print("Sorry! to say that but You got the wrong answer, and unfortubately you did not win any money")
print(f"It was a good game Mr or Mrs {name}") 

