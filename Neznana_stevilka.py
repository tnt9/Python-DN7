import random

your_number = int(raw_input("Please enter your number (between 1 and 10): "))
print("Your number is %i" % your_number)
number = random.randint(1, 10)
n = 1

if n < 2:
    if your_number < 1:
        print ("Chosen number is not in the range between 1 and 10. It is smaller.")
        your_number = int(raw_input("Please, choose once again: "))
    n = n
    if your_number > 10:
        print("Chosen number is not in the range between 1 and 10. It is higher.")
        your_number = int(raw_input("Please, choose once again: "))
    n = n
    if your_number < number:
        print("Your number is smaller then the random number.")
        your_number2 = int(raw_input("Please, choose again: "))
        if your_number2 < number:
            print("Your number is still smaller then the random number.")
        elif your_number2 > number:
            print("Your number is bigger then the random number.")
        else:
            print ("You've guessed correctly the random number!")
    elif your_number > number:
        print("Your number is bigger then the random number.")
        your_number2 = int(raw_input("Please, choose again: "))
    else:
        print("You've guessed correctly the random number!")
    n = n + 1

print("The random number is %i" % number)
