"""
This program allows users to list tables, display tables and duplicate tables.
"""
# Import CSV module for the CSV files
import csv
# Import the tabulate module to display the tables
from tabulate import tabulate

def load(filenames: list, tables: list) -> list:
    """
    Reset the tables list and load the table data from the provided CSV files.
    It returns the updated tables list.
    """
    tables = []

    #Open the CSV file and put it in a new table list
    for filename in filenames:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            tables.append(list(reader))

    return tables

def list_tables(tables: list):
    """
    To list out the index, number of columns and rows for the table.
    """
    # To store index, column count, and row count for each table
    table_summary = []
    
    # Repeat over all tables in the list
    for index, table in enumerate(tables):
        # Ensure the index is in the table index
        if table is not None:
            num_columns = len(table[0])
            num_rows = len(table)
            # Add the table info to the table_summary list
            table_summary.append([index, num_columns, num_rows])
    
    print(tabulate(table_summary, headers=["Index", "Columns", "Rows"], tablefmt="simple", numalign="right", stralign="right"))

def display(tables: list):
    """
    To displays the user's selected table.
    It will repeat until the user input the correct table index.
    """
    while True:
        index = int(input("Choose a table index (to display):\n"))
        # Ensure the index is in the range and in the table index
        if 0 <= index and index < len(tables) and tables[index] is not None:
            # Display the selected table in a simple format without showing the index
            print(tabulate(tables[index], headers='firstrow', tablefmt='simple', showindex=False))
            break
        else:
            print("Incorrect table index. Try again.")

def duplicate(tables: list) -> list:
    """
    Duplicate a table based on the user's selection.
    It will repeat until the user input the correct table index.
    It returns the updated tables.
    """
    while True:
        index = int(input("Choose a table index (to duplicate):\n"))
        # Ensure the index is in the range and in the table index
        if 0 <= index and index < len(tables) and tables[index] is not None:
            original_table = tables[index]
            new_table = []
            # Duplicate the selected table by appending the new table to the list.
            for row in original_table:
                copied_row = row[:]                   
                # Append the copied row to the new table.
                new_table.append(copied_row)
            #Append the new table to the tables list.    
            tables.append(new_table)
            break
        else:
            print("Incorrect table index. Try again.")
    
    return tables

def main():
    """
    The main function that allows the user to choose their action.
    User can choose to list tables, display tables or duplicate tables.
    """
    filenames = ['grades.csv', 
                'class_students.csv', 
                'rabbytes_club_students.csv', 
                'rabbytes_data.csv']
                
    # Load the tables from the CSv files
    tables = load(filenames, [])
    # Initialize an empty list for the table that have been deleted.
    deleted_tables = []
    
    # It will repeat until the user input a number from 0 to 7
    while True:
        print("==================================")
        print("Enter your choice:")
        print("1. List tables.")
        print("2. Display table.")
        print("3. Duplicate table.")
        print("0. Quit.")
        print("==================================")
        
        # User makes a choice
        choice = input()

        if choice == "1":
            list_tables(tables)

        elif choice == "2":
            display(tables)

        elif choice == "3":
            duplicate(tables)

        elif choice == "0":
            break

        else:
            continue

main()
