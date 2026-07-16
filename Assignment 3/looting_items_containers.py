"""
This program allow user to choose which container they want to pick.
User can choose to loot the items they want and list the looted items.
The item can fit in the container until capacity is full.
"""
# Import CSV module for the CSV files
import csv

class Items:
    """
    A representation of an item.
    """
    def __init__(self, name, weight):
        """
        Initialize an item with the name and weight.
        """
        # To ensure no extra spaces for name and weight
        self.name = name.strip()
        self.weight = int(weight.strip())

    def __str__(self):
        """
        Returns a string representating of the item.
        """
        # Return a string of the name and weight of the item
        return f"{self.name} (weight: {self.weight})"

class Containers:
    """
    A representation of a container.
    """
    def __init__(self, name, empty_weight, max_weight_capacity):
        """
        Initialize a Containers with the name, empty_weight and capacity.
        Arguments: name (str): The name of the container.
        empty_weight (float): The weight of the container when it is empty.
        max_weight_capacity (float): The maximum weight capacity the container can hold.
        """
        # Set the container's name, empty_weight, capacity and looted_items
        self.name = name.strip()
        self.empty_weight = empty_weight
        self.max_weight_capacity = max_weight_capacity
        self.looted_items = []  
        self.current_weight = 0

    def add_item(self, item) -> bool:
        """
        Return a string representation of the container.
        Arguement :  Item to be added which has 'weight'
        Returns -> bool: True if the item was successfully added. If the item's weight + the current container weight not exceed the container's maximum weight capacity
        """
        # Check if the container has enough capacity to add items, if enough return True, if not return False
        if (self.max_weight_capacity >= self.current_weight + item.weight):
            # If successful, update the current weight and add the item to the looted list.
            self.current_weight += item.weight
            self.looted_items.append(item)  
            return True
        return False

    def list_items(self, container_format: bool = False)-> str:
        """
        Creates a string to list all looted items stored in the container.
        Arguments: container_format (bool): If True, each item will be indented with spaces. Otherwise, items will be listed without indentation.
        Returns: str-> A formatted string that contains all looted items. Each item will be separated by a newline, with indentation if container_format is True.
        """
        items_list = "" 
        # List all looted items in the container
        for i in range(len(self.looted_items)):
            item = self.looted_items[i]
            # if container_format is True, add indent for better formatting
            if container_format:
                items_list += "   "
            items_list += f"   {item}"
            # Add a new line between looted items if i < len(self.looted_items) - 1 
            if i < len(self.looted_items) - 1:
                items_list += "\n"
        return items_list

    def __str__(self):
        """
        Returns a string representating of the container.
        """
        # Returns a string of name, total weight, empty_weight and capacity
        return f"{self.name} (total weight: {self.current_weight + self.empty_weight}, empty weight: {self.empty_weight}, capacity: {self.current_weight}/{self.max_weight_capacity})"

def loot_items(selected_container):
    """
    Allow user to loot an item and append it to the selected container.
    Arguements: select_container (Container): The container where the user wants to store the item.
    Return:If the item is found and can be added to the selected container, the item will be stored and a success message will be printed. Otherwise, a failure message will be print.
    """
    items = load_items('items.csv')
    selected_item = None
    while True:
        item_choice = input("Enter the name of the item: ")
        # Search for the item in the loaded items
        for item in items:
            if item.name == item_choice:
                selected_item = item
                break
        # If the item is found, try to add the item to the selected container
        if selected_container.add_item(selected_item):
            print(f'Success! Item "{selected_item.name}" stored in container "{selected_container.name}".')
            break
        else:
            print(f'Failure! Item "{selected_item.name}" NOT stored in container "{selected_container.name}".')
            break

def load_items(file):
    """
    Load items from a CSV file and return a list of Item objects.
    Arguements -> file (str): The path to the CSV file containing item data.
    Returns: A list of Item objects created from the CSV file.
    """
    loaded_items = []
    # Read the name and weight of the item in the Items CSV file
    with open(file, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        # Append the name and weight to the loaded_items list
        for row in reader:
            name, weight = row
            loaded_items.append(Items(name, weight))
    # Return the loaded_items list
    return loaded_items

def load_containers(file):
    """
    This function reads a CSV file containing container data and initializes Container objects.
    Arguement -> file(str):The CSV file containing container data.
    Return: A list of Container objects created from the CSV file, each initialized with its name, empty weight and weight capacity.
    """
    containers = []
    # Read the name, empty_weight and capacity of the container in the Containers CSV file
    with open(file, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        # Append name, empty_weight and capacity to the containers list
        for row in reader:
            name, empty_weight, max_weight_capacity = row
            containers.append(Containers(name, int(empty_weight.strip()), int(max_weight_capacity.strip())))
    return containers

def main():
    """
    The main function to start the program, load all items and containers, prompt the user to select a container,
    and then display a menu to choose an action for the selected container.
    """
    items = load_items('items.csv')
    containers = load_containers('containers.csv')
    print(f'Initialised {len(items) + len(containers)} items including {len(containers)} containers.\n')

    selected_container = None

    while True:
        container_choice = input("Enter the name of the container: ")

        # Find the container that the user inputted
        for container in containers:
            if container.name == container_choice:
                selected_container = container
                break

        # It will repeat until the user input a number from 0 to 2
        while True:
            print("==================================")
            print("Enter your choice:")
            print("1. Loot item.")
            print("2. List looted items.")
            print("0. Quit.")
            print("==================================")

            # User makes a choice
            choice = input()

            if choice == '1':
                loot_items(selected_container)

            elif choice == '2':
                print(selected_container)
                item_list_string = selected_container.list_items()
                # Check if there are looted items to print out
                if item_list_string:
                    print(item_list_string)

            elif choice == '0':
                return

            else:
                continue

main()
