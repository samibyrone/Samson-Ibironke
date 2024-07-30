# Delcare a variable with a fixed conversion rate for both currency
# Choose your conversion type based on your currency
# Prompt the user to choose the from option of what currency to convert
# Prompt the user to enter the conversion amount based on the currency
# Convert the user input amount to the fixed conversion rate 
# Display the currency conversion amount


print('\n program that prompt the user to enter the amount in naira or Dollars to be converted Based on Your Prefrence at Current. ')
print()


naira_dollar_rate = 0.000633579
dollar_naira_rate = 1,585.9658


print("\nChoose the type of Currency of Your Choice You Will Like to Convert Conversion :")
print("1: Convert From Nigerian Niara to US Dollar ")
print("2: Convert From US Dollar to Nigerian Naira ")
currency = input("\nEnter 1 or 2: ")


if currency == "1":
    naira = float(input("\n Enter the amount in Naira: "))
    dollar = naira * naira_dollar_rate
    print(f"\n {naira} Naira is equal to {dollar:.2f} Dollar")

elif currency == "2":
    dollar = float(input("\n Enter the amount in Dollar: "))
    naira = dollar * dollar_naira_rate
    print(f"\n {dollar} Dollar is equal to {naira:.2f} Naira")

else:
    print("\n Invalid Input. Please Try Again Later.")

