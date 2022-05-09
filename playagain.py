# this component will ask the user if they want to play again and respond appropriatly

play_again = input("do you want to play again")
if play_again == "yes" or play_again == "no":
    if play_again == "yes":
        print("start quiz")
    else:
        print("dont start quiz")
else:
    print("please enter yes or no")
