# Prompt the user to enter a number integer
# Check if the number is divisible by both 5 and 6
# Check if the number is divisible by both 5 or 6
# Display the output result



print('\n Program that prompt the user for an integer and checks whether the number is divisible by both 5 and 6 ')
print()



number = int(input("\n Enter an Number : "))


if number % 5 == 0 and number % 6 == 0:
	print(f"\n {number} is divisible by 5 and 6 ")

elif number % 5 == 0 or number % 6 == 0:
	print(f"\n {number} is divisible by 5 or 6 ")

else: print(f"\n {number} is not divisible by both 5 and 6.")


