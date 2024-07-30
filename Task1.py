# Prompt user to collect input of radius and length
# Intialize pi as 3.14
# Calculate the area of the cylinder by multiplying pi and the radius collected from the user and then raise to power of two
# Calculate the volume of the cylinder by multiplying the answer gotten from the area of the cylinder by the length collected from the user
# Print the calculated values of the area and length



print('\n Application that check the volume to a cicle and radius ')



pi = 3.14
radius = int(input('Enter the radius of a cylinder: '))
length = int(input('Enter the length of the cylinder: '))


area = (pi*radius)**2
volume = area * length

print(f'\n The area of the cylinder is {area}')
print(f'\n The volume of the cylinder is {volume}')
