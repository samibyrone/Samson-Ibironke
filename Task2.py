# prompt user for input to collect number of feet
# convert meters to foot
# convert inches to foots
# display output result  


print("\n This program will convert number that is given in feet and convert it to meters. ")
print()

feet = float(input("\n Enter number in feet: "))

meters_feet = feet
meters = (feet / 12) * feet
inches = (meters / feet % 1) * 12


print("One foot is",meters, "meters")

