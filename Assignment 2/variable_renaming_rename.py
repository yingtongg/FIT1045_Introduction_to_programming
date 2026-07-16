"""
This program allows user to write a code.
The user can choose if they want to print the code out, list the variables in the code, change the variable to snake_case form or rename the variables.
"""
# Import the keyword module for the keyword list
import keyword

def program(code):
    """
    Print the code that the user wrote.
    """ 
    print("Program:")
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
        word = i.split(" ")
        for j in word:
            valid_word = ""
            for char in j:
                #To cancel out the operators and only leave the variables with alphabets and "_"
                if char.isalpha() or char == '_':
                    valid_word += char
            #To cancel out the words that are in the keyword list
            if valid_word and valid_word[0].isalpha() and valid_word not in keyword.kwlist:
                #If valid is True and the variable is not in the variables list, it will append the new variable to the list.
                if valid_word not in variables:
                    variables.append(valid_word)

    print("Variables:")
    for var in sorted(variables):
        print(var)

def convert_to_snake_case(name):
    """
    This function loops through each character of the var_name.
    If the char is uppercase, must add "_" in front of it and convert to lower case which is snake_case version of the varname. 
    """
    # Initialize an empty list to hold characters
    snake_case_name = []
    
    # Convert the first character to lowercase and add it to the list
    first_char = name[0].lower()
    snake_case_name.append(first_char)
    
    for char in name[1:]:
        if char.isupper():
            # If the character is uppercase, append an underscore before it
            snake_case_name.append('_')
            # Convert the uppercase character to lowercase and append it
            lower_char = char.lower()
            snake_case_name.append(lower_char)
        else:
            # If the character is not uppercase, append it directly
            snake_case_name.append(char)
    
    result = ""
    
    # Build the result string from the list of characters
    for char in snake_case_name:
        result += char
    
    return result

def replace_var_names(code, var_name,variables):
    """
    This function allows the user to select a variable from the list of variables found in the code and converts it to snake_case.
    The variable will convert to snake_case and replace the old variable in the code. 
    """
    for a in variables:

        if a == var_name:
            snake_case_name = convert_to_snake_case(var_name)
    n = 0
    for line in code:
        # split line into individual word with spaces
        old_line = line.split(' ')
        x = 0 
        # loop through each var in split line
        for old_var in old_line:
            if old_var == var_name:
                # replace old_name with new_name
                old_line[x] = snake_case_name
                x += 1
            else:
                x += 1
        # Join word to single line
        new_line = ' '.join(old_line)
        code[n] = new_line
        # move to next line
        n += 1
    return code

def format_variables(code):
    """
    Allows user to select the variable which is from list of variables and converts it to snake_case.
    After store the list of var, user prompt to pick a variable, then the var format to snake_case version.
    """
    variables = []
    #Split the variables in "line"
    for line in code:
        words = line.split(' ')
        #Keep the variables that are alphabet or "_" in "valid_word"
        for word in words:
            valid_word = ""
            for char in word:
                #If the character is an alphabet or "_", put it in "valid_word"
                if char.isalpha() or char == '_':
                    valid_word += char
            if valid_word and valid_word[0].isalpha() and valid_word not in keyword.kwlist:
                if valid_word not in variables:
                    variables.append(valid_word)

    while True:
        var_name = input("Pick a variable:\n")
        for a in variables:
            # Check if the selected variable exists
            if a == var_name and len(a) == len(var_name):
                replace_var_names(code, var_name,variables)
                return code  
        print("This is not a variable name.") 

def replace_new_names(code, old_name, new_name):
    """
    This def function is to replace old var name to new var name.
    The code is updated from old_name to new_name, replace the old_name to new_name if old_var same with old_name.
    """
    #initialize to track the current line
    i = 0
    # loop through each word in the split line
    for line in code:
        old_line = line.split(' ')
        x = 0 
        for old_var in old_line:
            if old_var == old_name:
                old_line[x] = new_name
                # move to next var
                x += 1
            else:
                x += 1
        new_line = ' '.join(old_line)
        code[i] = new_line
        # move to next line
        i += 1
    return code

def rename(code):
    """
    This def is to ask the user to pick an existing variable to rename and provide a new variable name.
    Ensure that the new_name is not already in use and is not a python keyword.
    """
    variables = []
    
    # Extract all variables in the code
    for line in code:
        words = line.split()
        for word in words:
            valid_word = ""
            for char in word:
                if char.isalpha() or char == '_':
                    valid_word += char
            if valid_word and valid_word[0].isalpha() and valid_word not in keyword.kwlist:
                if valid_word not in variables:
                    variables.append(valid_word)
    # Let the user pick a variable to rename
    while True:
        old_name = input("Pick a variable:\n")
        if old_name in variables:
            break
        else:
            print("This is not a variable name.")
    
    while True:
        new_name = input("Pick a new variable name:\n")
        if new_name not in variables and new_name not in keyword.kwlist:
            replace_new_names(code, old_name, new_name)
            return code
            break
        else:
            print("This is already a variable name.")

def main():
    """
    The main function that allows user to choose which choice they want.
    Allows user to write their code.
    User can choose to print the code, list the variables, format to snake case or rename the variables.
    """
    #User type their code
    code=[]
    print("Enter the Python program to analyze, line by line. Enter 'end' to finish.")
    while True:
        coding=input()
        #If user type "end", it means that the user has typed finish their code and will break the loop.
        if coding=="end":
            break
        code.append(coding)

    #It will repeat until the user input a number from 0 to 4
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Print program.")
        print("2. List.")
        print("3. Format.")
        print("4. Rename.")
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

        elif choice == "4":
            rename(code)

        elif choice == "0":
            break
        
        else:
            continue

main()
