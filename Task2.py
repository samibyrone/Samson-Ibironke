# create a parameter for letters and digit
# collect input from to check user
# calculate the number of letters and digits from the input collected
# print the result 

print('\n Program that accept a sentence and calculate the numbers of letters and digits in the sentence. ')
print()

def count_letters_and_digits(sentence):

    letters = 0
    digits = 0

    for char in sentence:

        if char.isalpha():

            letters += 1

        elif char.isdigit():

            digits += 1


    return letters, digits

sentence = input("Enter a sentence: ")

letters, digits = count_letters_and_digits(sentence)

print(f"\n Number of letters in the sentence is: {letters}")
print(f"\n Number of digits in the sentence is: {digits}")
