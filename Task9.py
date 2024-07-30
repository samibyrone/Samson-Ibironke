# Prompt the user to enter name of employee
# Prompt the user to enter number of hours worked in a week
# Prompt the user to enter hourly pay rate
# Prompt the user to enter federal withholding tax rate
# Prompt the user to enter state withholding tax rate
# compute payroll informations
# display payroll statements



print('\n Program that read information of employee and print out a payroll statement ')
print()

name = input("\n Enter Your Employee's Name: ")
working_hour = int(input('\n Enter Number of Hours Worked In a Week: '))
pay_rate = float(input('\n Enter Hourly Pay Rate: '))
federal_tax_rate = float(input('\n Enter Federal Tax Withholding Rate: '))
state_tax_rate = float(input('\n Enter State Tax Withholding Rate: '))


gross_pay = working_hour * pay_rate
federal_withholding_tax_rate = gross_pay * federal_tax_rate
state_withholding_tax_rate = gross_pay * state_tax_rate
total_deductions = gross_pay - ( federal_withholding_tax_rate + state_withholding_tax_rate )
net_pay = gross_pay + total_deductions
print()


print("\n Payroll Statement ")
print("-" * 20)
print(f"\n Your Employee Name is : {name}")
print(f"\n Hours Worked in a Week is : {working_hour}")
print(f"\n Hourly Pay Rate : ${pay_rate:.2f}")
print(f"\n Gross Pay : ${gross_pay:.2f}")
print()

print("\n Deductions: ")
print("-" * 12)
print(f"\n Federal Withholding Tax ({federal_tax_rate * 100}%) : ${federal_withholding_tax_rate:.2f}")
print(f"\n State Withholding Tax ({state_tax_rate * 100}%) : ${state_withholding_tax_rate:.2f}")
print(f"\n Total Deduction : ${federal_withholding_tax_rate + state_withholding_tax_rate:.2f}")
print(f"\n Net Pay : ${total_deductions:.2f}")

