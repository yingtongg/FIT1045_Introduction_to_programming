"""
This program allows user to write a code.
The user can choose if they want to print the code out, list the variables in the code or change the variable to snake_case form.
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
                # Cancel out the operators and only leave the variables with alphabets and "_"
                if char.isalpha() or char == '_':
                    valid_word += char
            # Cancel out the words that are in the keyword list
            if valid_word and valid_word[0].isalpha() and valid_word not in keyword.kwlist:
                # If valid is True and the variable is not in the variables list, it will append the new variable to the list.
                if valid_word not in variables:
                    variables.append(valid_word)

    print("Variables:")
    # Sort the variables in alphabetical order
    for var in sorted(variables):
        print(var)

def convert_to_snake_case(name):
    """
    This function loops through each character of the var_name.
    If the char is uppercase, must add "_" in front of it and convert to lower case which is snake_case version of the varname. 
    """
    snake_case_name = []
    
    # Convert the first character to lowercase and add it to the list
    first_char = name[0].lower()
    snake_case_name.append(first_char)
    
    # If the character is uppercase, it will add "_" infront of it and become lowercase. If lowercase, it will not change.
    for char in name[1:]:
        if char.isupper():
            snake_case_name.append('_')
            lower_char = char.lower()
            snake_case_name.append(lower_char)
        else:
            snake_case_name.append(char)
    
    result = ""
    
# Combine all characters from the snake_case_name list into a single string
    for char in snake_case_name:
        result += char
    
    return result

def replace_var_names(code, var_name):
    """
    This function allows the user to select a variable from the list of variables found in the code and converts it to snake_case.
    The variable will convert to snake_case and replace the old variable in the code. 
    """
    snake_case_name = convert_to_snake_case(var_name)
    
    for i in range(len(code)):
        # Get the current line of code from the list
        line = code[i]
        new_line = ""
        var_len = len(var_name) 
        line_len = len(line) 
        j = 0 

        # Loop through current line to check the occurence of the variables name
        while j < line_len:
            # Check if the line same as the var_name
            if line[j:j + var_len] == var_name:
                if j + var_len == line_len or not line[j + var_len].isalnum():
                    new_line += snake_case_name
                    j += var_len  
                else:
                    new_line += line[j]  
                    j += 1  
            else:
                new_line += line[j]
                j += 1 
        
        # Update the code with new_line
        code[i] = new_line

def format_variables(code):
    """
    Allows user to select the variable which is from list of variables and converts it to snake_case.
    After store the list of var, user prompt to pick a variable, then the var format to snake_case version.
    """
    variables = []
    # Loop through each line of the code
    for line in code:
        # Split the valid var name from each words in the line
        words = line.split()
        for word in words:
            valid_word = ""
            for char in word:
                # If the character is a letter or "_", add it to valid_word
                if char.isalpha() or char == '_':
                    valid_word += char
            if valid_word and valid_word[0].isalpha() and valid_word not in keyword.kwlist:
                # If the valid_word is not exist in the list, add it the list of variables
                if valid_word not in variables:
                    variables.append(valid_word)

    while True:
        var_name = input("Pick a variable:\n")
        if var_name in variables:
            replace_var_names(code, var_name)  
            break
        else:
            print("This is not a variable name.")

def main():
    """
    The main function that allows user to choose which choice they want.
    Allows user to write their code.
    User can write their code and choose to print the code or list the variables.
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

    # It will repeat until the user input a number from 0 to 3
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Print program.")
        print("2. List.")
        print("3. Format.")
        print("0. Quit.")
        print("==================================")
        choice = input()
        # User makes a choice
        if choice == "1":
            program(code)

        elif choice == "2":
            listing(code)

        elif choice == "3":
            format_variables(code)  

        elif choice == "0":
            break

        else:
            continue

main()
