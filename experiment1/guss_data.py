import random

the_number = random.randint(1, 10)
count = 0
while True:
    guess = int(input("enter the number you guess"))
    count += 1
    if guess == the_number:
        print("you guessed the number")
        break
    elif guess > the_number:
        print("too high")
    elif guess < the_number:
        print("too low")
print("run out of guesses, game over")
