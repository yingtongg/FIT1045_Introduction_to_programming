def keyboard_layouts():
#Returns list of keyboard layouts
    return [["abcdefghijklm", "nopqrstuvwxyz"],["789", "456", "123", "0.-"],["chunk", "vibex", "gymps", "fjord", "waltz"],["bemix", "vozhd", "grypt", "clunk", "waqfs"]]

def calculate_moves(keyboard, user_input):
# Calculates the sequence of moves needed to type the user_input on the given keyboard layout.
    current_row, current_col = [0, 0]
#initialize starting position
    action = ""
#Check if the character is present on the keyboard
#Iterate over each character in the user_input
    for char in user_input:
#Check if the character is present on the keyboard
        if not any(char in row for row in keyboard):
            return None  #Character not found on this keyboard

        target_row, target_col = None, None
        for row_index in range(len(keyboard)):
            if char in keyboard[row_index]:
                target_row = row_index
                target_col = keyboard[row_index].index(char)
                break
        
        if target_row is None:
#If the character is not found, return None
            return None # Character not found on this keyboard 
#Determine horizontal movements (left or right)
        if target_col > current_col:
            action += 'r' * (target_col - current_col)
        elif target_col < current_col:
            action += 'l' * (current_col - target_col)
#Determine vertical movements (up or down)
        if target_row > current_row:
            action += 'd' * (target_row - current_row)
        elif target_row < current_row:
            action += 'u' * (current_row - target_row)
#Add the key press action       
        action += 'p'
        current_row, current_col = target_row, target_col
    
    return action

def print_keyboard(keyboard):
#Prints the keyboard layout with a border
    longest_row = max(len(row) for row in keyboard)
    print("-" * (longest_row + 4))
    for row in keyboard:
        print(f"| {row.ljust(longest_row)} |")
    print("-" * (longest_row + 4))

def main():
#Main function to find the keyboard layout with the minimum number of moves
    keyboards = keyboard_layouts()
#Retrieve all available keyboard layouts
    
    user_input = input("Enter a string to type: ")
#Initialize variables to track the best move sequence and its corresponding keyboard
    min_moves_sequence = None
    keyboard_with_min_moves = None
#Use a very large number to start
    fewest_moves = float('inf')

#Repeat over each keyboard layout to find the one with the minimum number of moves  
    for index, keyboard in enumerate(keyboards):
#calculate the movements required for the present keyboard arrangement.
        action = calculate_moves(keyboard, user_input)
#Check if the calculated move sequence is valid    
        if action is not None:
            move_count = len(action)#Determine the number of moves

#Update the min move sequence if the current is more efficient
            if move_count < fewest_moves:
                fewest_moves = move_count
                min_moves_sequence = action
                keyboard_with_min_moves = index
#If the current sequence has the same number of moves as the best one found so far and no keyboard has been selected yet

            elif move_count == fewest_moves and keyboard_with_min_moves is None:
                min_moves_sequence = action
                keyboard_with_min_moves = index
#Check if a valid move sequence was found    
    if min_moves_sequence is not None:
        print("Configuration used:")
#Print the layout of the keyboard_with_min_moves
        print_keyboard(keyboards[keyboard_with_min_moves])
#Print the sequence of moves for the robot to type the input
        print(f"The robot must perform the following operations:\n{min_moves_sequence}")
    else:
#inform the user if no valid sequence was found
        print("The string cannot be typed out.")


main()
















    
