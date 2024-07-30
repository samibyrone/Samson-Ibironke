# collect an input of integer from the user between 0 and 1000
# Initialize the sum_digit variable
# Print the output value of the  sum_digits




print('\n Program that reads an integer between 0 and 1000 and add all the digit in the integer ')


sum_digit = 0

number = int(input("\n Enter an integer between 0 and 1000: "))

while number:
    digit = number % 10
    sum_digit += digit
    number //= 10

print(f"\n Sum of digits: {sum_digit}")


