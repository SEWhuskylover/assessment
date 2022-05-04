# this function prints the instructions when run

def instructions():
    print("when the quiz starts you will be asked ten questions")
    print("they will be asked in maori and will be a number from 1 to ten")
    print("you will translate the number to english \nand type it before pressing ender to continue with the quiz")


# main routine

# while loop stops the user entering answers other than yes or no
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
