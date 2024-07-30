# prompt the user to enter the first integer numbers
# prompt the user to enter the second integer numbers
# prompt the user to enter the third integer numbers
# Compute the collected integer numbers in arranged order 
# Sort the integer numbers using the .sort KEYWORD to re-arrange the integer numbers
# Display the sorted integer numbers 



print('\n Program that Collect Three Integer number and Displays Them in Increasing Order ')
print()


index = int(input("Enter the first integer number: "))
index2 = int(input("Enter the second integer number: "))
index3 = int(input("Enter the third integer number: "))


numbers = [index, index2, index3]
numbers.sort()

print("\n Your Integer Numbers in increasing orders : ", numbers)
