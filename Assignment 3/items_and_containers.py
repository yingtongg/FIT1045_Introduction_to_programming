"""
The program is to reads items and containers by loading their data from CSV files and sorting them and displayed their name and weight for the items.
For the containers, displayed their name, empty weight and weight capacity
"""
# Import CSV module for the CSV files
import csv 

class Items:
    """
    Class to represent an item with a name and weight.
    """
    def __init__(self, name: str, weight: int):
        """
        Create a new instance of the Items class.
        Arguement -> name (str): The name of the item.
        weight (int): The weight of the item.
        """
        # Remove any extra spaces in item name
        self.name = name.strip()
        # Convert the weight to an integer 
        self.weight = int(weight)

    def __str__(self):
        """
        Return a string representation of the item.
        """
        return f"{self.name} (weight: {self.weight})"


class Containers:
    """
    Class to represent a container with a name, empty weight, and weight capacity.
    """
    def __init__(self, name: str, empty_weight: int, weight_capacity: int):
        """
        Initialize a Containers instance.
        Arguement -> name (str): The name of the container.
        empty_weight (int): The empty weight of the container.
        weight_capacity (int): The weight capacity of the container.
        """
        # removing extra spaces
        self.name = name.strip()
        # Store the empty weight as an integer
        self.empty_weight = int(empty_weight)
        # Store the weight capacity as an integer
        self.weight_capacity = int(weight_capacity)

    def __str__(self):
        """
        Return a string representation of the container.
        """
        return (f"{self.name} (total weight: {self.empty_weight}, "
                f"empty weight: {self.empty_weight}, "
                f"capacity: 0/{self.weight_capacity})")


def load(filenames: list) -> list:
    """
    Load CSV files and return their content as a list of tables.
    Arguement -> filenames (list): A list of CSV filenames to load.
    Return: A list of tables representing the content of the CSV files.
    """
    # Create an empty list to store the content (rows) of each CSV file
    tables = []
    for filename in filenames:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            # Convert the CSV data into a list of rows and append it to tables
            tables.append(list(reader))
    return tables

def sort_items(items: list) -> list:
    """
    Sort the list of items by their name.
    Arguement -> A list of Items objects to sort.
    Return -> A sorted list of Items objects.
    """
    sorted_items = []
    while items:  
        smallest = items[0]
        # Iterate through all items to find the smallest
        for item in items:
            # Compare names to find the smallest item
            if item.name < smallest.name:  
                smallest = item  
        # Add the smallest item to the sorted list
        sorted_items.append(smallest)  
        new_items = []
        # Loop through the items, if current item is not the smallest, add it to the new list
        for item in items:  
            if item != smallest: 
                new_items.append(item)
        items = new_items  
    return sorted_items 

def sort_containers(containers: list) -> list:
    """
    Sort the list of containers by their name.
    Arguement -> A list of Containers objects to sort.
    Return: A sorted list of Containers objects.
    """
    sorted_containers = []  
    # Repeat sorting until there are no more containers
    while containers:  
        smallest = containers[0]
        # Iterate through all containers to find the smallest
        for container in containers:  
            if container.name < smallest.name:  
                smallest = container  

        sorted_containers.append(smallest) 
        
        # Create a new list of containers exclude the smallest container
        new_containers = []
        # Loop through the original containers
        for container in containers:
            if container != smallest:  
                new_containers.append(container)  
        # Update the original containers list to be the new list
        containers = new_containers  

    return sorted_containers  

def main():
    """
    Main function that loads items and containers from CSV files and displays them.
    """
    filenames = ['containers.csv', 'items.csv'] 

    tables = load(filenames)  
    # Extract the items data from the loaded tables
    items_data = tables[1]  
    items = []  
    # Iterate through each row of items data, starting from the second row
    for row in items_data[1:]:
        # Get item name and weight from the row
        name, weight = row[0].strip(), row[1].strip()  
        items.append(Items(name, weight)) 

    containers_data = tables[0]  
    containers = []  
    # Iterate through each row of containers data, starting from the second row
    for row in containers_data[1:]:  
        name, empty_weight, weight_capacity = row[0].strip(), row[1].strip(), row[2].strip()
        # Create a Containers object and add it to the list
        containers.append(Containers(name, empty_weight, weight_capacity))  

    print(f"Initialised {len(items) + len(containers)} items including {len(containers)} containers.")

    print("\nItems:")  
    sorted_items = sort_items(items)
    # Iterate through the sorted items and print each of the item
    for item in sorted_items:  
        print(item)

    print("\nContainers:") 
    sorted_containers = sort_containers(containers)
    # Iterate through the sorted containers and print each of the containers
    for container in sorted_containers: 
        print(container)

    print("")  
main()
