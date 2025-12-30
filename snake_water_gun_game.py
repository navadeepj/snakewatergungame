import random

chio = ["snake", "water", "gun"]
comp = random.choice(chio)

user = input("Enter your choise (snake/ water/ gun)").lower()

if user not in chio:
    print("Invalid choice!!")
else:
    print("Computer Choice is: " + comp)

if user == comp:
    print("Result: Draw!!")
elif (user == "snake" and comp == "water") or (user == "water" and comp == "gun") or (user == "gun" and comp == "snake"):
    print("Result: You Won!!")
else:
    print("Result: You lost")