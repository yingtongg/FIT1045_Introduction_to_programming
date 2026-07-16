# Define the keyboard layout
keyboard = ["abcdefghijklm", "nopqrstuvwxyz"]

# Initialize starting position
current_row, current_col = [0, 0]

# Get the user input
user_input = input("Enter a string to type: ")

# Initialize the command list
action = ""

# Flag to check if the string is valid
valid_input = True

# Check if the input contains only valid characters
for char in user_input:
    if char not in 'abcdefghijklmnopqrstuvwxyz':
        valid_input = False
        break
    
    # Find the position of the character on the keyboard
    target_row, target_col = None, None
    for row_index in range(len(keyboard)):
        if char in keyboard[row_index]:
            target_row = row_index
            target_col = keyboard[row_index].index(char)
            break
    
    if target_row is None:
        valid_input = False
        break
    
    # Create the commands to move Robbie to the target character

    if target_col > current_col:
        action += 'r' * (target_col - current_col)
    elif target_col < current_col:
        action += 'l' * (current_col - target_col)
    
    if target_row > current_row:
        action += 'd' * (target_row - current_row)
    elif target_row < current_row:
        action += 'u' * (current_row - target_row)
    
    # Add the press command
    action += 'p'
    
    # Update Robbie's current position
    current_row, current_col = target_row, target_col

# Output the result
if valid_input:
    print("The robot must perform the following operations:")
    print(action)
else:
    print("The string cannot be typed out.")






