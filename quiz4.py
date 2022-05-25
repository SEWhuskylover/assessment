# this component will test the user with a quiz and keep track of their marks
import random


def quiz():
    score = 0
    print("the quiz has starting")
    print("here are a look of the answers")
    print(" 1 Tahi\n 2 rua\n 3 toru\n 4 wha\n 5 rima\n 6 ono\n 7 whitu\n 8 waru\n 9 iwa\n 10 tekau")
    input("enter to start the quiz")
    questions = ["toru", "rima", "tahi", "iwa", "rua", "waru", "tekau", "ono", "wha", "whitu"]
    answer = ["3", "5", "1", "9", "2", "8", "10", "6", "4", "7"]
    loop = 0
    while loop != 10:
        number_choice = random.randint(0, 1)
        current_q = questions.pop(number_choice)
        current_a = answer.pop(number_choice)
        print(current_q)
        user_a = input()
        if current_a == user_a:
            print("correct")
            score += 1
        else:
            print(f"the answer was {current_a}")
        loop += 1
    print(f"yours score was {score} out of 10")


# main routine
quiz()
