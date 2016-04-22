import random

your_number = int(raw_input("Please enter your number (between 1 and 10):"))
print("Your number is %i" % your_number)

number = random.randint(1, 10)

if int(your_number) < number:
    print("Your number is smaller then the random number.")
    your_number2 = int(raw_input("Guess again: "))
    if int(your_number2) == number:
        print("You've guessed correctly the random number!")
    else:
        print("Even your second guess is wrong!")

elif your_number > number:
    print("Your number is bigger then the random number.")
    your_number2 = int(raw_input("Guess again: "))
    if your_number2 == number:
        print("You've guessed correctly the random number!")
    else:
        print("Even your second guess in wrong!")
else:
    print("You've guessed correctly the random number!")

print("The random number is %i" % number)
