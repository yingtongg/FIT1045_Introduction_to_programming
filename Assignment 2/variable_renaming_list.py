"""
This program allows user to write a code.
The user can choose if they want to print the code out or list the variables in the code.
"""
# Import the keyword module for the keyword list
import keyword

def program(code):
    """
    Print the code that the user wrote.
    """ 
    print("Program:")
    # Print the code
    for i in code:
        print(i)

def listing(code):
    """
    List out the variables that contain in the code.
    The code is split into words based on spaces. 
    Each word is checked for a valid variable and to eliminate the keywords using the keyword module.
    """
    variables = []

    for i in code:
        # Split current line into words and operators by spaces
        word = i.split(" ")
        # Extract valid variable names from each word
        for j in word:
            valid_word = ""
            for char in j:
                # To cancel out the operators and only leave the variables with alphabets and "_"
                if char.isalpha() or char == '_':
                    valid_word += char
            # To cancel out the words that are in the keyword list
            if valid_word and valid_word[0].isalpha() and valid_word not in keyword.kwlist:
                # If valid is True and the variable is not in the variables list, it will append the new variable to the list.
                if valid_word not in variables:
                    variables.append(valid_word)

    print("Variables:")
    # Sort the variables in alphabetical order
    for var in sorted(variables):
        print(var)
        
def main():
    """
    The main function that allows user to choose which choice they want.
    Allows user to write their code.
    User can choose to write their code,choose to print the code or list the variables.
    """
    # User type their code
    code=[]
    print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
    while True:
        coding=input()
        # If user type "end", it means that the user has typed finish their code and will break the loop.
        if coding=="end":
            break
        code.append(coding)

    # It will repeat until the user input a number from 0 to 2
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Print program.")
        print("2. List.")
        print("0. Quit.")
        print("==================================")
        choice = input()
        # User make a choice 
        if choice == "1":
            program(code)

        elif choice == "2":
            listing(code)

        elif choice == "0":
            break

        else:
            continue

main()
