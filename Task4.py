# Prompt the user to enter input for subtotal amount
# collect value input from user
# Promt the user to enter input for percentage value from the subtotal
# Collect the value for the user
# create a variable called gratuity
# calculate the total amount for subtotal with the percentage rate together
# print out value of percentage from the subtotal
# display the total sum of subtotal and the percentage together


print('\n Program that reads amount from user with the gratuity rate and display the sum total. ')
sub_total = int(input("\n Enter the Subtotal Amount: "))

rate = int(input("\n Enter your gratuity rate in percentage : "))
rate = rate / 100  

gratuity = sub_total * rate
total = sub_total + gratuity

print(f"\n Your Gratuity is : {gratuity}")

print(f"\n The Total Value with your Gratuity is : {total}")




