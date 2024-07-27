# Prompt the user to enter the number of minutes
# Convert the minutes to years and days
# set a variable to calculate minutes and divide it by minutes in a year
# Display the output result to the user

print('Program that prompt user to enter minutes and display the number of years and days for the minutes')


daily_minutes = 60 * 24
minutes_to_years = daily_minutes * 365

minutes = int(input("Enter the number of minutes: "))

years = daily_minutes
days = (minutes % minutes_to_years)

print(f"\n {minutes} minutes is will be: {years} years with {days} days altogether. ")
