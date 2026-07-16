"""
This program allows user to choose which choice they want to choose.
User can create a rabbit, choose their age, list the rabbits out, create parental relationship and list the family out.
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

def parental(parent,rabbit, kitten):
    """
    User input parent name and kitten name to have a parental relationship.
    If both names have not yet exist, that name will be created.
    """
    # If the parent name is not found, then it will output as Unknown
    parent_name=input(f"Input the parent's name:\n")
    if parent_name not in rabbit:
        rabbit[parent_name]="Unknown"

    # If the kitten name is not found, then it will output as Unknown
    kitten_name=input(f"Input the kitten's name:\n")
    if kitten_name not in rabbit:
        rabbit[kitten_name]="Unknown"
        
    # If the parent name that the user inputted not yet exist, the name will go to parent list.
    if parent_name not in parent:
        parent[parent_name] = []
    parent[parent_name].append(kitten_name)
    
    # If the kitten name that the user inputted not yet exist, the name will go to kitten list.
    if kitten_name not in kitten:
        kitten[kitten_name] = []
    kitten[kitten_name].append(parent_name)

def family(rabbit, parent, kitten):
    """
    To know which parent have which child and which child have which parents.
    User need to enter a name that exist in the database.
    """
    while True:
        # User input rabbit name
        rabbit_name=input("Input the rabbit's name:\n")

        # If the rabbit in the database, then it will print the rabbit's parents
        if rabbit_name in rabbit:
            print(f"Parents of {rabbit_name}:")

            # Sort the parents names
            if rabbit_name in kitten and kitten[rabbit_name]:
                for parent_name in sorted(kitten[rabbit_name]):
                    print(parent_name)

            print(f"Kittens of {rabbit_name}:")

            # Sort the kittens names
            if rabbit_name in parent and parent[rabbit_name]:
                for kitten_name in sorted(parent[rabbit_name]):
                    print(kitten_name)
            break
        
        else:
            print("That name is not in the database.")
 
def main():
    """
    The main function that allows user to choose which choice they want.
    User can choose to create a rabbit, choose their age, list the rabbits out, create parental relationship or list the family out.
    """
    rabbit = {}
    kitten={}
    parent={}
    while True:
        # It will repeat until the user input a number from 0 to 5
        print("==================================")
        print("Enter your choice:")
        print("1. Create a Rabbit.")
        print("2. Input Age of a Rabbit.")
        print("3. List Rabbytes.")
        print("4. Create a Parental Relationship.")
        print("5. List Direct Family of a Rabbit.")
        print("0. Quit.")
        print("==================================")
        
        # User make a choice
        choice = input()

        if choice == "1":
            create(rabbit)

        elif choice == "2":
            age(rabbit)

        elif choice == "3":
            rabbytes(rabbit)

        elif choice == "4":
            parental(parent,rabbit, kitten)

        elif choice == "5":
            family(rabbit, parent, kitten)

        elif choice == "0":
            break

        else:
            continue

main()
