
# create function to calculate the sum of numbers
# create two parameters for your integral, first and second
# take two integral numbers as strings format
# calculate the sum of your integral number
# print the sum total for you integral


print('\n A function that recieve two integral numbers in a string form and compute their sum and return result in string')
print()


first = "500"
second = "7000"

def compute_sum (index1, index2):
	counter = int(index1) + int(index2)
	return counter 

sum = compute_sum (first, second)

print ("\n Total Integral Sum is = ", sum)
