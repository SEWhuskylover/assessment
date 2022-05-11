# this is the final version which will ask the user for instructions and then test them they then get a mark
# out of then and are asked if they want to play again if not they are thanked before the program ends


# this function prints out the instructions for the game when run

def instructions():
    print("when the quiz starts you will be asked ten questions")
    print("they will be asked in maori and will be a number from 1 to ten")
    print("you will translate the number to english \nand type it before pressing ender to continue with the quiz")


# when run this function asks the user 10 questions and grades them based on how well they do

def quiz():
    # this variable keeps track of the users score during the test
    score = 0
    # the answers are printed for the user and they have as much time as they need to memorize it
    print("the quiz has starting")
    print("here are a look of the answers")
    print(" 1 Tahi\n 2 rua\n 3 toru\n 4 wha\n 5 rima\n 6 ono\n 7 whitu\n 8 waru\n 9 iwa\n 10 tekau")
    input("enter to start the quiz")
    # the questions that will be asked in the quiz
    print("toru")
    answer = input("")
    if answer == "3":
        print("correct")
        score += 1
    else:
        print("wrong")
        print("the answer was 3")

    print("rima")
    answer = input("")
    if answer == "5":
        print("correct")
        score += 1
    else:
        print("wrong")
        print("the answer was 5")

    print("tekau")
    answer = input("")
    if answer == "10":
        print("correct")
        score += 1
    else:
        print("wrong")
        print("the answer was 10")

    print("tahi")
    answer = input("")
    if answer == "1":
        print("correct")
        score += 1
    else:
        print("wrong")
        print("the answer was 1")

    print("wha")
    answer = input("")
    if answer == "4":
        print("correct")
        score += 1
    else:
        print("wrong")
        print("the answer was 4")

    print("ono")
    answer = input("")
    if answer == "6":
        print("correct")
        score += 1
    else:
        print("wrong")
        print("the answer was 6")

    print("whitu")
    answer = input("")
    if answer == "7":
        print("correct")
        score += 1
    else:
        print("wrong")
        print("the answer was 7")

    print("iwa")
    answer = input("")
    if answer == "9":
        print("correct")
        score += 1
    else:
        print("wrong")
        print("the answer was 9")
    print("waru")
    answer = input("")
    if answer == "8":
        print("correct")
        score += 1
    else:
        print("wrong")
        print("the answer was 8")

    print("rua")
    answer = input("")
    if answer == "2":
        print("correct")
        score += 1
    else:
        print("wrong")
        print("the answer was 2")
    # prints the users score after the quiz ends
    print(f"yours score was {score} out of 10")


# this function will thank the user for playing and say goodbye

def thanks():
    print(" ********** ")
    print("***thanks***")
    print(" ********** ")
    print()
    print(":::::::::::::")
    print(":::::for:::::")
    print(":::::::::::::")
    print()
    print("#############")
    print("###playing###")
    print("#############")


# main routine

# while loop stops the user entering answers other than yes or no after being asked if they need instructions
push_back = 0
while push_back == 0:
    yes_no = input("do you need instructions\n ")
    if yes_no == "yes":
        instructions()
        push_back = 1
    else:
        print(".")
        push_back = 1
    if yes_no == "yes" or yes_no == "no":
        print()
    else:
        print("please enter yes or no")
        push_back = 0

# this runs the quiz function
quiz()

# this while loop lets asks the user if they want to play again and stops them entering answers other than yes or no
forward = 0
while forward == 0:
    play_again = input("do you want to play again\n")
    if play_again == "yes" or play_again == "no":
        if play_again == "yes":
            quiz()
        else:
            forward = 1
    else:
        print("please enter yes or no")

# this runs the thanks function to thank the user for playing
thanks()
