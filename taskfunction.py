		[ task 9 ]

def calculate_payroll():
    # Get employee information
    employee_name = input("Enter employee's name: ")
    hours_worked = float(input("Enter number of hours worked in a week: "))
    hourly_pay_rate = float(input("Enter hourly pay rate: "))
    federal_tax_rate = float(input("Enter federal tax withholding rate (as a decimal): "))

    # Calculate gross pay
    gross_pay = hours_worked * hourly_pay_rate

    # Calculate federal tax
    federal_tax = gross_pay * federal_tax_rate

    # Calculate net pay
    net_pay = gross_pay - federal_tax

    # Print payroll statement
    print("\nPayroll Statement")
    print(f"Employee Name: {employee_name}")
    print(f"Hours Worked: {hours_worked}")
    print(f"Pay Rate: ${hourly_pay_rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Federal Tax Withholding: ${federal_tax:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")

# Run the payroll calculation
calculate_payroll()




		[ task 10 ]
def collect_and_sort_numbers():
    # Collect three integer numbers from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    
    # Store the numbers in a list
    numbers = [num1, num2, num3]
    
    # Sort the list in ascending order
    numbers.sort()
    
    # Display the sorted numbers
    print("The numbers in increasing order are:", numbers)

# Call the function
collect_and_sort_numbers()






		[ task 11 ]
