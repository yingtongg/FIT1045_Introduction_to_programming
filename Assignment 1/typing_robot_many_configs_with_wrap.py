def keyboard_layouts():
    # Returns list of keyboard layouts
    return [["abcdefghijklm", "nopqrstuvwxyz"], ["789", "456", "123", "0.-"], ["chunk", "vibex", "gymps", "fjord", "waltz"], ["bemix", "vozhd", "grypt", "clunk", "waqfs"]]

def calculate_moves(keyboard, user_input):
    # Calculates the sequence of moves needed to type the user_input on the given keyboard layout.
    current_row, current_col = 0, 0  # Initialize starting position
    action = ""
    
    for char in user_input:
        # Check if the character is present on the keyboard
        if not any(char in row for row in keyboard):
            return None  # Character not found on this keyboard

        # Find the target position of the character
        target_row, target_col = None, None
        for row_index in range(len(keyboard)):
            if char in keyboard[row_index]:
                target_row = row_index
                target_col = keyboard[row_index].index(char)
                break
        
        if target_row is None:
            return None  # Character not found on this keyboard 

        # Calculate row length and number of rows
        row_length = len(keyboard[current_row])
        num_rows = len(keyboard)

        # Determine horizontal movements (left or right) with wrapping
        right_moves = (target_col - current_col) % row_length
        left_moves = (current_col - target_col) % row_length
        if right_moves <= left_moves:
            action += 'r' * right_moves
        else:
            action += 'l' * left_moves + 'w'

        # Update current position after horizontal move
        current_col = target_col

        # Determine vertical movements (up or down) with wrapping
        down_moves = (target_row - current_row) % num_rows
        up_moves = (current_row - target_row) % num_rows
        if down_moves <= up_moves:
            action += 'd' * down_moves
        else:
            action += 'u' * up_moves + 'w'

        # Add the key press action
        action += 'p'
        current_row = target_row
    
    return action

def print_keyboard(keyboard):
    # Prints the keyboard layout with a border
    longest_row = max(len(row) for row in keyboard)
    print("-" * (longest_row + 4))
    for row in keyboard:
        print(f"| {row.ljust(longest_row)} |")
    print("-" * (longest_row + 4))

def main():
    # Main function to find the keyboard layout with the minimum number of moves
    keyboards = keyboard_layouts()
    user_input = input("Enter a string to type: ")
    
    min_moves_sequence = None
    keyboard_with_min_moves = None
    fewest_moves = float('inf')

    for index, keyboard in enumerate(keyboards):
        action = calculate_moves(keyboard, user_input)
        if action is not None:
            move_count = len(action)
            if move_count < fewest_moves:
                fewest_moves = move_count
                min_moves_sequence = action
                keyboard_with_min_moves = index
            elif move_count == fewest_moves and keyboard_with_min_moves is None:
                min_moves_sequence = action
                keyboard_with_min_moves = index

    if min_moves_sequence is not None:
        print("Configuration used:")
        print_keyboard(keyboards[keyboard_with_min_moves])
        print(f"The robot must perform the following operations:\n{min_moves_sequence}")
    else:
        print("The string cannot be typed out.")

main()

