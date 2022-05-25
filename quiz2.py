# this component will test the user with a quiz and keep track of their marks


score = 0
print("the quiz has starting")
print("here are a look of the answers")
print(" 1 Tahi\n 2 rua\n 3 toru\n 4 wha\n 5 rima\n 6 ono\n 7 whitu\n 8 waru\n 9 iwa\n 10 tekau")
input("enter to start the quiz")

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

print(f"yours score was {score} out of 10")
