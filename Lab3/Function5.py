import random

print("Hello! What is your name?")
name = input()
print("")
j = 1

number = random.randrange(1, 21)
print("Well," ,name + ", I am thinking of a number between 1 and 20.")
while 1:
    print("Take a guess.")
    g = int(input())
    print("")
    if g>number:
        print("Your guess is to high.")
    elif g<number:
        print("Your guess is to low.")
    elif g==number:
        print("Good job,", name + "! You guessed my number in", j, "guesses!")
        break
    j += 1
