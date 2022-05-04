def instructions():
    print("when the quiz starts you will be asked ten questions")
    print("they will be asked in maori and will be a number from 1 to ten")
    print("you will translate the number to english \nand type it before pressing ender to continue with the quiz")


yes_no = input("do you need instructions\n ")
if yes_no == "yes":
    instructions()
else:
    print(".")
