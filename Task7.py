# Prompt the user to input amount for initial deposit
# prompt user for annual interest rate in percentage
# Prompt the user for number of years the initial amount wil be deposit 
# compute the deposit amount with the annual percentage and years of savings 
# Display the output result


print('\n Program That Deposit a Certain Amount of Money to a Savings Account With a Fixed Annual Interest Rate')
print()


deposit_amount = float(input('\n Enter the amount to deposit into a savings account: $'))

annual_interest_rate = int(input('\n Enter your annual interest rate on your deposit: %'))

number_of_years = int(input('\n Enter the number of years for your deposit: '))



final_account_value = deposit_amount * (1 + annual_interest_rate / 100) ** number_of_years


print(f'\n At The End of {number_of_years} Years, Your Total Amount in Your Savings Account is: ${final_account_value}')

