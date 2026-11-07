runtime = 1
while runtime == 1:
    import time
    import random
# dont know if math is needed or not but better safe than sorry
    import math
    import sys
# sys is added so i can add an exit for this aplication without using windows X button
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
    print("4th you can make a list ")
    print('')
    print("5th you can view the credit :D ")
    print(" ")
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
        elif choice == ("4"):
            option += 1
        elif choice == ("5"):
            option += 1
        else:
            print("try again")
    n3 = 0 
    answer = 0
    int(answer)
        # omg this took so long ): for something so simple
    if choice == ("1"):
        n1 = int(input("select the first number "))
        print("")
        n2 = int(input("select your second number "))
        answer = n1 * n2
        print(answer); time.sleep(3)
        print("")
        print("welp thats it for this section try one of the other options :D")
    #    this was super easy because its just print tho ill probaly add more story stuff  
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
        object2 = "you shouldint see this ether"
        str(object2)
        correct_ans = "why can you see this??"
        str(correct_ans)
        while num == 0:
            rn = random.randint(1,2)
        # if you want to verify that it works all it does is print so just un hashtag the print(rn)
        #print(rn)      
            grn = input("guess the side head or tales ")
            if grn == ("heads"):
                num += 1
            elif grn == ("head"):
                num += 1
            elif grn == ("tales"):
                num += 2
            else:
                num += 2
        # this section below is to assign a number to a word so it can tell you what the answer is  
        # had to re write in order to make it tell you the correct answer also rembered "and" existed so that helped alot lol
            if num == 1:
                print("you selected heads")
            elif num == 2:
                print("you selected tales")
            if num == 1 and rn == 1:
                print("you got it correct it was heads")
            elif num == 2 and rn == 2:
                print("you got it correct it was tales")
            elif num == 1 and rn == 2:
                print("it was actually tales not heads")
            elif num == 2 and rn == 1:
                print("it was heads not tales")
            else:
                print("there has been an error")
        # This is the list part
        # if user wants it vertical then i should do print while if i want it hoirzontal then i should do the list command
        # so the solution ive came up with is that we will ask the user if they want it vertical or horizontal and that will determuine
        # which one is used tho it does mean i code it twice \:
    elif choice == ("4"):
        l_val = 0
        l_name = input("what would you like to name your list ")
        print("");time.sleep(0.6)
        l_ori = input("type 1 if you want your list horizontal or type 2 if you want your list vertical ")
        print("");time.sleep(0.6)
        l1 = input("what is your first item on your list ")
        print('')
        l2 = input("now what is your second item ")
        print('')
        l3 = input("what is your third item :3 ")
        print("")
        l4 = input("what is your fourth item ")
        print("")
        l5 = input("what is your fith item ")
        print("")
        print("now to create your list :D ")
        # l_val is just so the while loop end correctly and l_ori is the orientation on the list and l# is just the number of the list 
        while l_val == 0:
            if l_ori == ("1"):
                print(l_name," -made by ", name)
                print("")
                this_list = [l1,"",l2,"",l3,"",l4,"",l5]
                print(this_list); time.sleep(5)
                l_val += 1
            elif l_ori == ("2"):
                print(l_name, " made by " ,name )
                print("")
                print(l1)
                print(l2)
                print(l3)
                print(l4)
                print(l5) ;time.sleep(5)
                l_val += 1
        #option 5 litterly just credits :P
    elif choice == ("5"):
            print("thank you for selecting the credits im your lovly bot and i will tell you who made me");time.sleep(4)
            print("I was made by askreddit4name ");time.sleep(4)
            print("if you liked me and want to see more check out her youtube channel ");time.sleep(4)
            print("it is @grilledpotato5024 ");time.sleep(4)
            print("and her twitter is @grilledpotato18");time.sleep(4)
            print("and you can also find her on threads @askreddit4name");time.sleep(3)
            print("anyway thank you for checking out the credits :D");time.sleep(3)
    #print("test of restet probaly leave this in under hash tag for further testing");time.sleep(5)
    try_again = input("would you like to run the program all over again just type yes or no ")
    if try_again == "no":
        print("dang well i hope you enjoyed it and please check out the credit :P ");time.sleep(4)
        #sys.exit is not perminate sense i do plan to add more stuff past first screen and will make a diffrent menu and options for future stuff 
        sys.exit
    elif try_again == "yes":
        print("yay we will reset now and i will ask for your name ") 
    else:
        ("you did not select and option so we are gonna close out of the application hope you had fun :D ")
        sys.exit