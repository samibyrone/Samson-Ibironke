# set a number range for iterating 
# iterate each number on set on the list
# check condition to be true
# display the result

print('\n Program that display the even numbers between 1000 and 3000. ')
print()


def display_even_number(numbers):

for index in range(1000, 3001):

number = int(input())
	if index % 2 == 0:

		print(index, end=", ")
