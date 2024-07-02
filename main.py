# This application is a password generator with at least a single number and a single special character.
# The user decides the length of the password, along with if numbers and special characters will be included
import random
import string

# User input on how long they want the password and what characters are to be included
length = int(input("Please provide the number of characters you want for your password. "))
inc_numbers = input("Would you like to include numbers in the password? (y / n) ").lower() == "y"
inc_special = input("Would you like to include special characters in the password? (y / n) ").lower() == "y"

# Method to generate the password
def generate(length, inc_numbers = True, inc_special = True):
    letters = string.ascii_letters
    numbers = string.digits
    special = string.punctuation

    # Letters will always be included. Number and special characters will only be included if requested by the user
    characters = letters
    if inc_numbers == True:
        characters += numbers
    if inc_special == True:
        characters += special

    while True:
        # Generate the random characters at the length speficied by the user
        selected_char = random.choices(characters, k=length)

        # Boolean variables - Checking if a single or more numbers and a single or more special characters are included in the randomly generated password
        has_number = any(char in numbers for char in selected_char)
        has_special = any(char in special for char in selected_char)

        # If numbers are not requested or generated characters have number it in
        # and special characters not requested or special character is in generated characters
        if (not inc_numbers or has_number) and (not inc_special or has_special):
            break

    # Returns the password as a String
    return "".join(selected_char)

password = generate(length,inc_numbers,inc_special)
print("Your password is:",password)

