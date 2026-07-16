"""
This program allow user to choose which container they want to pick.
User can choose to loot the items they want and list the looted items.
The list of looted items will have compartments to loot more items. If the items fit in multiple compartments then it will place in the first compartment.
This program includes magic containers which function like standard containers but maintain weight regardless of the items stored inside them.
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
        Initialize a Container with the name, empty_weight and capacity.
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
        Returns -> bool: True if the item was successfully added. If the item's weight + the current container weight 
        not exceed the container's maximum weight capacity
        """
        # Check if the container has enough capacity to add items
        if self.max_weight_capacity >= self.current_weight + item.weight:
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

class Multi_Containers(Containers):
    """
    A representation of a container with multiple compartments.
    """

    def __init__(self, name, compartments):
        """
        Initializes a Multi_Containers
        Arguement -> name (str): The name of the multi-container.
        compartments (list of Containers): A list of individual container compartments 
        within the multi-container.
        """
        # Set the multi_container's name, compartments, current_weight, empty_weight and capacity.
        self.name = name
        self.compartments = compartments  
        self.current_weight = 0
        # Sum up the empty weights of all compartments
        self.empty_weight = sum(compartment.empty_weight for compartment in compartments)  
        self.max_weight_capacity = 0

    def add_item(self, item) -> bool:
        """
        Add an item to any compartment within the multi-container.
        Arguement: item (Item): The item to be added, which has a weight information
        Returns bool->: return True if the item was successfully added to one of the compartments.
        """
        # Loop through each compartment in the list of compartments
        for compartment in self.compartments:
            # Check if the item can be added to the compartment
            if compartment.add_item(item):
                # Update the total weight of the multi-compartment container
                self.current_weight += item.weight
                return True  
        return False 

    def list_items(self):
        """
        The method loops through compartments in a multi-container and create a formatted string
        that lists each compartment and its items.
        It initializes an empty string, iterates over each compartment, and appends items and separate them with line breaks.
        Returns ->str: A formatted string listing all compartments and their items.        
        """
        items_list = ""
        # Loop through each compartment and list items in each
        for i, compartment in enumerate(self.compartments):
            items_list += f"   {compartment}"
            # Call the compartment's list_items method to display items
            item_list_string = compartment.list_items(True)
            #  If the list of items from the current compartment exist, append it.
            if item_list_string:
                items_list += "\n"
                items_list += item_list_string
            # Go to a new line between the compartments
            if i < len(self.compartments) - 1:
                items_list += "\n"  
        return items_list

    def __str__(self):
        """
        Returns a string representating of the container.
        """
        # Return a string of name, total weight, empty_weight and capacity
        return f"{self.name} (total weight: {self.current_weight + self.empty_weight}, empty weight: {self.empty_weight}, capacity: 0/{self.max_weight_capacity})"

class Magic_Containers(Containers):
    """
    A class representing a MagicContainer
    """
    def __init__(self, name, empty_weight, max_weight_capacity):
        """
        Initialize a magic container, calling the Containers class constructor.
        Arguements -> name(str) : The name of the magic container.
        empty_weight (float): The weight of the empty container.
        max_weight_capacity (float): The maximum weight capacity of the container.            
        """
        # Set Containers name, empty_weight and capacity
        Containers.__init__(self, name, empty_weight, max_weight_capacity)

    def add_item(self, item) -> bool:
        """
        Add an item to the magic container, but maintain the total weight
        Arguement: item (Item): The item to be added to the container.
        Returns True if the item is successfully added otherwise return False.
        """
        # Check if adding the item exceeds the maximum weight capacity
        if self.max_weight_capacity >= self.current_weight + item.weight:
        # Update the current weight of the container by adding the item's weight
            self.current_weight += item.weight  
            self.looted_items.append(item)
            return True
        return False

    def __str__(self):
        """
        Returns a string of the MagicContainer.
        """
        # Total weight remains equal to the empty weight regardless of looted items' weight
        return f"{self.name} (total weight: {self.empty_weight}, empty weight: {self.empty_weight}, capacity: {self.current_weight}/{self.max_weight_capacity})"

def loot_items(selected_container):
    """
    Allow user to loot an item and append it to the selected container.
    Arguements: select_container (Container): The container where the user wants to store the item.
    Return:If the item is found and can be added to the selected container, the item will be stored and a success message will be printed.
    Otherwise, a failure message will be print
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
    Arguements -> :file (str): The CSV file containing item data.
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
    Arguement-> file(str):The CSV file containing container data.
    Return: A list of Container objects created from the CSV file, each initialised with its name, empty weight and weight capacity.
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

def load_multi_containers(file, containers):
    """
    Load multi-compartment containers from a CSV file and create multi_container objects.
    Arguements -> containers (list): A list of available container objects to match compartments.
    file (str): The CSV file that contain the magic multi-compartment container data.
    Return: A list of MultiContainers objects created from the CSV file. Each MultiContainers object is initialized with its name and the its compartments.
    """
    multi_compartments_list = []
    # Read the name and compartments of the item in the Containers CSV file
    with open(file, newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            compartments = []
            name = row[0]  
            # Loop through the compartment names listed in the CSV
            for compartment_name in row[1:]:
                compartment = compartment_name.strip()  
                for container in containers:
                    if container.name == compartment:
                        compartments.append(Containers(compartment, container.empty_weight, container.max_weight_capacity))
            # Add the new Multi_Containers to the list
            multi_compartments_list.append(Multi_Containers(name, compartments))  
    return multi_compartments_list

def load_magic_containers(file, containers):
    """
    Load magic containers from a CSV file and return a list of Magic_Containers objects.
    Arguements -> file (str): The CSV file containing magic container data.
    containers (list): A list of available Container objects to match with base containers.
    Returns:A list of Magic_Containers objects created from the CSV file, each initialized with its name and base container's weight.
    """
    magic_containers = []
    # Read the name and containers of the item in the magic_container CSV file
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        # Iterate through each row in the CSV file
        for row in reader:
            name = row[0].strip()
            container_name = row[1].strip()
            
            # Find the base container that matches the container name
            for container in containers:
                if container.name == container_name:
                    # Use the empty weight and capacity of the base container
                    magic_containers.append(Magic_Containers(name, container.empty_weight, container.max_weight_capacity))
                    break
    return magic_containers

def main():
    """
    The main function that allow user to choose their action.
    User can select a container and choose to loot an item or list out the looted items in the container.
    """
    items = load_items('items.csv')
    containers = load_containers('containers.csv')
    multi_containers = load_multi_containers('multi_containers.csv', containers)
    magic_containers = load_magic_containers('magic_containers.csv', containers)

    all_containers = containers + multi_containers + magic_containers
    selected_container = None

    print(f"Initialised {len(items + containers + multi_containers + magic_containers)} items including {len(containers + multi_containers + magic_containers)} containers.\n")
    
    # It will repeat until the user choose 0 to quit the program
    while True:
        container_choice = input("Enter the name of the container: ")

        # Find the container that the user inputted
        for container in all_containers:
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
