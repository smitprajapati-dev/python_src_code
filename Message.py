
# time = input("Enter current time to display message")

# if time >= 6 and time <= 11:
#     print("Good Morning! Smit")
# elif time >= 12 and time <= 16:
#     print("Good AfterNoon! Smit")
# elif time >= 17 and time <= 20 :
#     print("Good Evening! Smit")
# elif time >=21 and time <24:
#     print("Good Night! Smit, have sweet dream")

import time

name = input("Enter your name ")

racentTime= time.strftime('%H:%M:%S')

RaceTime = int(time.strftime('%H'))

if(4<=RaceTime<12):
    print(f"Good Morning! {name},It's {racentTime}")

elif(12>=RaceTime<=17):
    print(f"Good Afternoon! {name.capitalize}, {racentTime}")
elif(18>=RaceTime <=21):
    print(f"Good Evening! {name}, it's {racentTime}")
else:
    print(f"Good Night! {name}, It's {racentTime}")