





print('\n program that prompt the user to input three digit numbr and determine whether the user win according to the exact order')





a, b, c = [int(x) for x in input("Please enter the numbers: ").split()]


import random

# Generate a random three-digit number
lottery_number = random.randint(100, 999)

# Prompt the user to enter a three-digit number
user_input = int(input("Enter a three-digit number: "))

# Check if the user's input matches the lottery number in the exact order
if user_input == lottery_number:
    print("Congratulations! You win $10,000!")
else:
    print(f"Sorry, you lose. The winning number was {lottery_number}.")



import random

# Generate a random three-digit lottery number
lottery_number = random.randint(100, 999)

# Prompt the user to enter a three-digit number
user_input = int(input("Enter a three-digit lottery number: "))

# Check if the user's input matches the lottery number in exact order
if user_input == lottery_number:
    print("Congratulations! You have won the lottery!")
else:
    print(f"Sorry, the winning lottery number was {lottery_number}. Better luck next time!")




# Function to check if all digits in the number are the same
def all_digits_match(number):
    digits = str(number)
    return digits[0] == digits[1] == digits[2]

# Prompt the user to enter a three-digit number
user_input = input("Please enter a three-digit number: ")

# Check if the input is a valid three-digit number
if user_input.isdigit() and len(user_input) == 3:
    number = int(user_input)
    if all_digits_match(number):
        print("All digits match!")
    else:
        print("The digits do not match.")
else:
    print("Invalid input. Please enter a three-digit number.")




# Function to check if the guessed digit is in the number
def check_digit(number, guess):
    return guess in str(number)

# Prompt the user to input a three-digit number
number = input("Enter a three-digit number: ")

# Ensure the input is a three-digit number
while not (number.isdigit() and len(number) == 3):
    number = input("Invalid input. Please enter a three-digit number: ")

# Prompt the user to guess a digit
guess = input("Guess a digit in the number: ")

# Ensure the guess is a single digit
while not (guess.isdigit() and len(guess) == 1):
    guess = input("Invalid input. Please guess a single digit: ")

# Check if the guessed digit is in the number
if check_digit(number, guess):
    print("Congratulations! The digit is in the number.")
else:
    print("Sorry, the digit is not in the number.")



import random

# Generate a random three-digit lottery number
lottery_number = random.randint(100, 999)

# Prompt the user to enter a three-digit number
user_number = int(input("Enter a three-digit lottery number: "))

# Check if the user's number matches the lottery number
if user_number == lottery_number:
    print("Congratulations! You have won $10,000!")
elif sorted(str(user_number)) == sorted(str(lottery_number)):
    print("Congratulations! You have won $3,000!")
elif any(digit in str(lottery_number) for digit in str(user_number)):
    print("Congratulations! You have won $1,000!")
else:
    print("Sorry, no match. Better luck next time!")

print(f"The lottery number was: {lottery_number}")

