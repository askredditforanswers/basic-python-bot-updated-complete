import time
import random
# dont know if math is needed or not but better safe than sorry
import math
start = 1
while start == 1:
    name = input("hello welcome to my test application please state your name =p ")
    if name == (""):
        print("")
        print("you have to put a name")
        print("")
    elif name == "no":
        print(" ")
        print("gfys")
        print("")
    else:
        print(" ")
        start += 1
    print("hello nice to meet you", name , "hope you enjoy this little test of my skill so far");time.sleep(1)

print("you are gonna get a choice on what you want to do");time.sleep(0.9)
print("")
print("1st, multiply two numbers ")
print("")
print("2nd i can tell you a story =P ")
print("")
print("3rd you can guess if its heads or tales")
print("")
    # probaly not the best solution for making else not skip but it works and should not cause any promblems
option = 1
while option == 1:
    choice = input("choose which option you would like to pick ")
    if choice == ("1"):
        option +=1
    elif choice == ("2"):
        option += 1
    elif choice == ("3"):
        option += 1
    else:
        print("try again")
n3 = 0 
answer = 0
int(answer)
    # omg this took so long ): and i had to google it but no AI was used :D i hate AI
if choice == ("1"):
    n1 = int(input("select the first number "))
    print("")
    n2 = int(input("select your second number "))
    answer = n1 * n2
    print(answer); time.sleep(3)
    print("")
    print("welp thats it for this section try one of the other options :D")
    # this was super easy because its just print tho ill probaly add more story stuff  
elif choice == ("2"):
    print("")
    print("there once was a robot in the year 3077");time.sleep(1)
    print("")
    print("it was full of wonder on what it was like in the 2000's");time.sleep(2.5)
    print("")
    print("the robot always wanted to know what humans were like and what trees looked like");time.sleep(2.5)
    print("")
    print("but saddly, they would never be able to sense humans wiped them self out because of polution ");time.sleep(2.5)
    print("")
    print("and trees were wiped out by human so the robot could only wonder what we were truely like");time.sleep(2.5)
    print("")
    # option 3 has been the most chalenging in the sense that i havint looked anything up its my brain only but this has taken the longest
elif choice == ("3"):
    num = 0
    object1 = "you shouldit see this"
    str(object1)
    while num == 0:
        rn = random.randint(1,2)
        print(rn)
        grn = input("guess the side head or tales ")
        if grn == ("head"):
            num += 1
        elif grn == ("tales"):
            num += 2
        else:
            num += 2
        # this section below is to assign a number to a word so it can tell you what the answer is  
        if num == 1:
            object1 = "heads"
        elif num == 2:
            object1 = "tales"
        if num == rn:
            print(" you got it correct it was ", object1)
        elif num != grn:
            print("you got it wrong it was ", object1)