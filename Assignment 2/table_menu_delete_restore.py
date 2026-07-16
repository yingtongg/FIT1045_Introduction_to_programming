"""
This program allow user to list table, display table, duplicate table, create table, delete table, delete columns and restore table.
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

def create(tables: list) -> list:
    """
    To create a new DataFrame based on the selected columns from an existing DataFrame.
    It will repeat until the user input the correct table index.
    It returns the updated tables.
    """
    while True:
        index = int(input("Choose a table index (to create from):\n"))
        # Ensure the table index is in the range and in the table index.
        if 0 <= index and index < len(tables) and tables[index] is not None:
            break
        else:
            print("Incorrect table index. Try again.")

    cols = input("Enter the comma-separated indices of the columns to keep:\n")
    
    selected_columns = []

    # Split the input string by commas to get each column index as a string
    column_indices_str = cols.split(',')
    
    # Convert each column index from string to integer and append to the list
    for col_str in column_indices_str:
        col_int = int(col_str)
        selected_columns.append(col_int)

    valid_indices = True
    # Validate all selected column index exist in the DataFrame
    for col in selected_columns:
        if col < 0 or col >= len(tables[index][0]):
            valid_indices = False
            break

    if not valid_indices:
        return tables
    
    # Create a new table for the columns that the user selected
    new_table = []
    new_table.append([tables[index][0][col] for col in selected_columns])
    for row in tables[index][1:]:
        new_table.append([row[col] for col in selected_columns])
        
    #Append the new table to the table list
    tables.append(new_table)
    return tables

def delete_table(tables: list, deleted_tables: list) -> list:
    """
    Removes a table from the list by setting its value to `None`.
    It will repeat until the user input the correct table index.
    It returns the updated tables.
    """
    while True:
        index = int(input("Choose a table index (for table deletion):\n"))
        # Ensure the table index is in the range and in the table index
        if 0 <= index < len(tables) and tables[index] is not None:
            # Add the deleted table to the list of deleted tables
            deleted_tables.append((index, tables[index]))
            #To count the table as deleted
            tables[index] = None  
            break
        else:
            print("Incorrect table index. Try again.")

    return tables

def delete_column(tables: list) -> list:
    """
    Removes a column from a specified DataFrame.
    It will repeat until the user input the correct table index.
    It returns the updated tables.
    """
    while True:
        index = int(input("Choose a table index (for column deletion):\n"))
        # Ensure the table index is in the range and in the table index
        if 0 <= index < len(tables) and tables[index] is not None:
            col_index = int(input("Enter the index of the column to delete:\n"))
            if 0 <= col_index < len(tables[index][0]):                    
                # Initialize a new table
                new_table = []                    
                # Loop each row in the table that the user selected
                for row in tables[index]:
                    new_row = row[:col_index] + row[col_index + 1:]
                    new_table.append(new_row)
                        
                # Replace the original table with the new table
                tables[index] = new_table
                break  
            else:
                print("Invalid column index. Try again.")
        else:
            print("Incorrect table index. Try again.")

    return tables

def restore(tables: list, deleted_tables: list) -> list:
    """
    Restores a previously deleted table to its original index.
    It will repeat until the user input the correct table index.
    """
    if not deleted_tables:
        return tables

    while True:
        index = int(input("Choose a table index (for restoration):\n"))
        table_restore = False
        # Iterate through the deleted tables
        for i in range(len(deleted_tables)):
            if index == deleted_tables[i][0] and tables[index] is None:
                tables[index] = deleted_tables[i][1]
                updated_deleted_tables = []
                for j in range(len(deleted_tables)):
                    if j != i:
                        updated_deleted_tables.append(deleted_tables[j])
                # Update list of the deleted tables
                deleted_tables[:] = updated_deleted_tables
                table_restore = True
                break
        # Check whether the table was successfully restored
        if table_restore:
            return tables
        else:
            print("Incorrect table index. Try again.")

    return tables

def main():
    """
    The main function that allows user to choose which choice they want.
    User can choose to list table, display table, duplicate table, create table, delete table, delete columns or restore table.
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
        print("4. Create table.")
        print("5. Delete table.")
        print("6. Delete column.")
        print("7. Restore table.")
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

        elif choice == "4":
            create(tables)

        elif choice == "5":
            delete_table(tables, deleted_tables)

        elif choice == "6":
            delete_column(tables)
            
        elif choice == "7":
            restore(tables, deleted_tables)

        elif choice == "0":
            break

        else:
            continue

main()
