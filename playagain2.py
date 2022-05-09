# this component will ask the user if they want to play again and respond appropriatly
forward = 0
while forward == 0:
    play_again = input("do you want to play again\n")
    if play_again == "yes" or play_again == "no":
        if play_again == "yes":
            print("start quiz")
            forward = 1
        else:
            print("dont start quiz")
            forward = 1
    else:
        print("please enter yes or no")
