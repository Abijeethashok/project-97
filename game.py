import random 

number = random.randint(1, 9)
chances = 0
while chances < 5:
    guess = int(input("guess a number 1 to 9"))
    if guess == number:
        print("you win")
        break
    elif guess < number:
        print("your guess is low, guess higher number")
    elif guess > number:
        print("your guess is high, guess a lower number")   
    chances = chances + 1 
if chances == 5:
    print("you lose")





