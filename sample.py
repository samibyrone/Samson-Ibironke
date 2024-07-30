def display_table(number, limit):
    print(f"Multiplication Table for {number} up to {limit}:")
    for i in range(1, limit + 1):
        print(f"{number} x {i} = {number * i}")

# Example usage
num = int(input("Enter the number for the multiplication table: "))
limit = int(input("Enter the range for the multiplication table: "))
display_table(num, limit)