import random
num=random.randint(1,9)
print(num)
while(True):
    guess=int(input("Enter your guess:"))
    if guess==num:
        print("Well Guessed")
        break