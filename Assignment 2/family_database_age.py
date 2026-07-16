"""
This program allows user to choose which choice they want to choose.
User can create a rabbit, choose their age and list it out.
"""

def create(rabbit):
    """
    Allow user to name the rabbit. 
    If the name already exist, user need to choose another name.
    """
    # It will repeat until the user input a name that have not exist in the database.
    while True:
        # User input a rabbit name
        name=input(f"Input the new rabbit's name:\n")
        # If the name is not yet exist, the name that the user just inputted will go into the database.
        if name not in rabbit:
            rabbit[name] = "Unknown"
            break
 
        # The name has already exist in the database
        else:
            print("That name is already in the database.")
 
def age(rabbit):
    """
    Allow user to enter the rabbit's age.
    User cannot enter the age until the rabbit's name is in the database.
    """

    # It will repeat until the user enter a name that is in the database.
    while True:
        name=input(f"Input the rabbit's name:\n")

        # If the name is in the database, user can input the rabbit's name.
        if name in rabbit:
            age=input(f"Input {name}'s age:\n")
            rabbit[name] = age
            break

        # If name not in rabbit, the program will tell the user that the name is not in the database.
        else:
            print("That name is not in the database.")
 
def rabbytes(rabbit):
    """
    Prints the name and the age of the rabbit.
    If the user has not inputted the age of the rabbit, then the rabbit's age will remain unknown.
    """
    print("Rabbytes:")
    # It will print the name and age of the rabbit.
    for name, age in rabbit.items():
        print(f"{name} ({age})")
 
def main():
    """
    The main function that allows user to choose which choice they want.
    User can choose to create a rabbit, put the age of the rabbit or list the rabbits.
    """
    rabbit = {}

    # It will repeat until the user input a number from 0 to 3
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. Create a Rabbit.")
        print("2. Input Age of a Rabbit.")
        print("3. List Rabbytes.")
        print("0. Quit.")
        print("==================================")
        choice = input()
        
        # User make a choice 
        if choice == "1":
            create(rabbit)

        elif choice == "2":
            age(rabbit)

        elif choice == "3":
            rabbytes(rabbit)

        elif choice == "0":
            break

        else:
            continue

main()
